---
title: "Prácticas de Pruebas Automatizadas para el Producto de Recuperación ante Desastres Cloud-Nativo HyperBDR"
description: "Cómo el equipo de HyperBDR resolvió el reto de más de 10.000 combinaciones de casos de prueba usando Python, Terraform y pipelines de automatización."
date: 2023-02-06T14:28:40+08:00
slug: "cloud-native-migration-backup-dr-hyperbdr-automation-testing"
author: Ray Sun
tags:
  - Pruebas Automatizadas
  - Python
  - Terraform
categories:
  - I+D de Producto
draft: false
---

HyperBDR es un producto de migración y recuperación ante desastres construido sobre principios cloud-nativos. Su escenario de negocio principal consiste en sincronizar los datos del lado origen hacia el almacenamiento cloud-nativo a nivel de bloque mediante diferenciales incrementales. Actualmente soporta tanto Block Storage como Object Storage. Tras la sincronización, aprovecha la tecnología patentada Boot-in-Cloud para restaurar los sistemas de negocio a un estado operativo con un solo clic, explotando plenamente las capacidades de orquestación cloud-nativa para atender las distintas necesidades de los escenarios de migración y recuperación ante desastres.

HyperBDR actualmente soporta casi 10 familias principales de sistemas operativos en el lado origen (Windows / CentOS / Redhat / Ubuntu / SUSE / SO domésticos), con versiones menores que superan varios cientos, y ha añadido progresivamente soporte para casi 40 plataformas cloud de destino (nube pública, nube dedicada, nube privada, hiperconvergente, virtualización, etc.), una cifra que sigue creciendo. Si ejecutáramos una prueba de cobertura completa de todos los sistemas operativos origen contra cada plataforma de destino, los casos de prueba combinados podrían superar los 10.000.

A esta escala, depender exclusivamente del esfuerzo manual para lograr cobertura de pruebas es claramente inviable. Es imprescindible introducir pruebas automatizadas para cubrir los escenarios de negocio principales. Esto no solo satisface los requisitos de prueba automatizada, sino que también permite a los desarrolladores evaluar con prontitud el impacto de las nuevas funcionalidades sobre los flujos principales durante el desarrollo cotidiano, mejorando así la estabilidad y fiabilidad del producto.

## Análisis de Puntos de Dolor

Examinemos primero los principales puntos de dolor en las pruebas manuales de HyperBDR:

### Punto de Dolor 1: Demasiados Casos de Prueba, Recursos Humanos Insuficientes

Dada la escala de orígenes y destinos descrita, incluso una prueba de humo básica requiere más de cien combinaciones de escenarios por ejecución completa. Por ejemplo:

- Lado origen (19 variantes): CentOS (6/7/8), Redhat (6/7/8), SUSE (11/12), Ubuntu (14.04/16.04/18.04/20.04), Windows (2003/2008/2012/2016/2019), Oracle Linux, SO doméstico

- Lado destino (9 variantes): OpenStack, AWS, Alibaba Cloud, Tencent Cloud, Huawei Cloud, China Mobile Cloud, ZStack, producto hiperconvergente, producto hiperconvergente

Esto suma 171 combinaciones de escenarios por ejecución. Algunos podrían pensar que no son tantos y que no llevaría mucho tiempo ejecutarlos, pero eso nos lleva al segundo punto de dolor: la duración del ciclo de pruebas.

### Punto de Dolor 2: Ciclos de Prueba Prolongados

A diferencia de las pruebas funcionales de negocio, probar un único escenario de HyperBDR es extremadamente laborioso. Dejando de lado el tiempo de preparación de recursos y configuración, analicemos únicamente las fases de sincronización de datos y arranque:

- Sincronización de datos: En términos simples, la sincronización lee los datos efectivos (no la capacidad asignada) del SO origen a nivel de bloque y los escribe en el almacenamiento cloud-nativo del destino. La primera sincronización es completa; las siguientes son incrementales permanentes. Tomando Windows como ejemplo — supongamos 500 GB de datos efectivos. Al 80% de utilización de una red LAN gigabit, la velocidad de transferencia es aproximadamente 800 Mbps (unos 80 MB/s), lo que da un tiempo de transferencia de aproximadamente 1 hora y 8 minutos.

- Arranque del host: El tiempo de arranque varía considerablemente según el tipo de almacenamiento cloud-nativo. Para el Block Storage de Huawei Cloud, gracias a su mecanismo de snapshots y la capacidad de intercambiar discos del sistema, el tiempo de arranque es prácticamente independiente del volumen de datos y normalmente se puede mantener en menos de 5 minutos. Sin embargo, la mayoría de las plataformas cloud domésticas carecen de estas capacidades. Alibaba Cloud, por ejemplo, limita la lectura de volúmenes respaldados por snapshots a 40 MB/s, lo que alarga significativamente el tiempo de recuperación. Usando Object Storage como ejemplo — restaurar datos de Object Storage a Block Storage a través de una red interna para un disco con 500 GB de datos efectivos tarda aproximadamente 40 minutos.

Por tanto, una sola ejecución de prueba para un host individual requiere al menos 2 horas. Bajo los supuestos del escenario anterior, un día completo de pruebas puede no ser suficiente para completar una pasada completa en una sola plataforma cloud. Alguien podría preguntar: ¿por qué no ejecutarlas de forma concurrente? Eso nos lleva al tercer punto de dolor: el coste.

### Punto de Dolor 3: Coste de las Pruebas

La razón por la que no podemos ejecutarlo todo de forma concurrente son las restricciones de ancho de banda de red. En nuestro entorno de I+D interno, el ancho de banda externo es de solo 40 Mbps. Bajo los escenarios de prueba descritos, transmitir 500 GB de datos a plena utilización del ancho de banda tarda aproximadamente 35 horas, lo que amplía aún más el ciclo de pruebas.

Además de la red, existen otras limitaciones del entorno: licencias de plataformas de virtualización, gasto en proveedores cloud, consumo de recursos del servidor, entre otros.

## Solución de Automatización

Para cada punto de dolor, desarrollamos una solución correspondiente:

### Para Demasiados Casos de Prueba: Usar Terraform para Crear VMs de Prueba Origen en la Nube Pública

Terraform es una herramienta de infraestructura como código que nos permite crear y destruir recursos de prueba de forma rápida y fiable. El ecosistema de providers de Terraform ya cubre las principales nubes públicas domésticas e internacionales, así como la nube privada OpenStack que usamos internamente — sin necesidad de código personalizado; basta con utilizar el provider oficial del proveedor cloud.

Basándonos en el análisis anterior, podemos usar Terraform para preparar rápidamente entornos origen para las pruebas y, al terminar, destruirlos inmediatamente para eliminar el desperdicio de recursos. El mismo enfoque se aplica a la preparación de entornos del lado destino en diversas plataformas cloud.

### Para Ciclos de Prueba Prolongados: Ejecución Concurrente

La concurrencia opera en dos niveles. Primero, al probar contra una única nube pública, podemos usar múltiples cuentas cloud simultáneamente para ejecutar pruebas en paralelo. Segundo, entre diferentes nubes públicas, las pruebas pueden ejecutarse concurrentemente, maximizando el ancho de banda disponible.

### Para el Coste: Recursos Cloud bajo Demanda

Gestionando el ciclo de vida de los recursos de prueba con Terraform, podemos aprovisionar recursos cuando se necesitan y destruirlos inmediatamente tras las pruebas, eliminando el desperdicio y reduciendo significativamente los costes.

## Marco de Pruebas

El marco de pruebas automatizadas global de HyperBDR consta de los siguientes componentes:

### 1. Preparación del Entorno Origen

Usar Terraform para preparar rápidamente el entorno origen requerido para las pruebas, incluyendo la instalación del HyperBDR Agent.

### 2. Driver de Negocio de HyperBDR

Mediante un SDK de Python, llamar a la API de negocio de HyperBDR para impulsar la ejecución automatizada de escenarios. El flujo de trabajo principal es:

- Configurar la plataforma de almacenamiento
- Crear política de sincronización
- Agregar host origen
- Ejecutar operación de sincronización
- Ejecutar operación de arranque
- Ejecutar operación de apagado
- Eliminar host

### 3. Verificación de Resultados

Tras el arranque del host, comprobar la conectividad de red para determinar si el arranque fue exitoso. Verificar que los procesos de negocio funcionan correctamente y confirmar que los discos de datos están montados correctamente.

### 4. Informes de Prueba

Usar la generación de informes integrada de Robot Framework para presentar los resultados de las pruebas en formato HTML para facilitar su revisión.

## Integración con CI/CD

Integramos el marco con Jenkins. Cuando un desarrollador lanza un job de Jenkins, se ejecuta automáticamente una serie de escenarios de prueba. También configuramos jobs programados en Jenkins que se disparan automáticamente cada noche a medianoche, garantizando que se produzcan resultados de prueba diariamente.

## Planes de Futuro

Nuestro marco de pruebas automatizadas aún está en una fase temprana y tiene muchas áreas de mejora:

1. Ampliación de casos de prueba: Los casos de prueba actuales son relativamente limitados. A medida que el producto evolucione, ampliaremos continuamente la cobertura.

2. Mejora de los informes de prueba: El formato de informe actual es bastante básico. Las versiones futuras pueden añadir gráficos y visualizaciones más ricos para hacer los informes más intuitivos.

3. Gestión del entorno de pruebas: La gestión del entorno es actualmente sencilla. Las mejoras futuras podrán introducir herramientas adicionales como Ansible y SaltStack para un mejor control del entorno.
