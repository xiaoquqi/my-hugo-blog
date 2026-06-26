---
title: Mejores prácticas para la migración de un centro de negociación de valores a Alibaba Cloud
date: 2021-02-05 17:35:56 +08:00
author: Ray Sun
tags:
  - Migración a la nube
  - Finanzas
  - Mejores prácticas
  - Alibaba Cloud
categories:
  - Migración a la nube
draft: false
---

Este artículo presenta las mejores prácticas de un centro de negociación de valores que utilizó HyperMotion para migrar sus sistemas de negocio a Alibaba Cloud. Los centros de negociación de valores tienen requisitos extremadamente elevados en materia de seguridad de datos y continuidad del negocio, lo que convierte este caso en un estudio de migración a la nube típico del sector financiero.

<!-- more -->

## Contexto del cliente

El centro de negociación de valores es una institución financiera regional cuyas actividades principales incluyen el registro de valores, la custodia de valores y la negociación de valores. Con el rápido crecimiento del negocio, el centro de datos IDC existente ya no podía satisfacer las necesidades de desarrollo empresarial. Sumado a la presión del vencimiento del arrendamiento del centro de datos, se tomó la decisión de migrar las operaciones de negocio a Alibaba Cloud.

## Desafíos de la migración

### 1. Altos requisitos de continuidad del negocio

Las operaciones del centro de negociación de valores deben funcionar de manera ininterrumpida las 24 horas del día, los 7 días de la semana, y no se permiten tiempos de inactividad prolongados.

### 2. Altos requisitos de seguridad de datos

Los datos de valores son datos financieros extremadamente sensibles. La seguridad e integridad de los datos deben garantizarse durante todo el proceso de migración.

### 3. Alta complejidad del sistema

Los sistemas de TI del centro de negociación de valores incluyen decenas de sistemas de aplicaciones con complejas interdependencias.

### 4. Requisitos de cumplimiento normativo

Como institución financiera, debe cumplir con los requisitos de seguridad de datos y cumplimiento establecidos por las autoridades reguladoras pertinentes.

## Plan de migración

### Arquitectura general

Para hacer frente a los desafíos anteriores, se desarrolló el siguiente plan de migración:

1. **Migración por lotes**: Los sistemas de aplicaciones se agruparon en múltiples lotes según la relevancia empresarial y la prioridad, y luego se migraron lote por lote.
2. **Minimizar el tiempo de inactividad**: Se aprovecharon las capacidades de migración en línea de HyperMotion para mantener el tiempo de inactividad en un mínimo absoluto.
3. **Pruebas exhaustivas**: Se realizaron pruebas exhaustivas antes de la migración para garantizar el funcionamiento normal del sistema después de la conmutación.

### Arquitectura de red

Para garantizar la seguridad de la transmisión de datos, se utilizó Alibaba Cloud Direct Connect para conectar el IDC y el VPC de Alibaba Cloud, en lugar de una VPN de red pública.

### Flujo de trabajo de la migración

1. **Preparación del entorno**: Preparar el entorno de destino en Alibaba Cloud, incluyendo VPC, grupos de seguridad e instancias ECS.

2. **Sincronización de datos**: Usar HyperMotion para establecer un canal de sincronización de datos desde el origen hasta Alibaba Cloud e iniciar la sincronización continua de datos.

3. **Pruebas y validación**: Una vez completada la sincronización de datos, realizar pruebas de negocio exhaustivas en Alibaba Cloud, incluyendo pruebas funcionales, pruebas de rendimiento y pruebas de seguridad.

4. **Conmutación formal**: Durante las horas de menor actividad (generalmente los fines de semana de madrugada), detener las operaciones en el lado de origen, esperar a que se complete la sincronización de datos final y luego iniciar los sistemas de negocio en Alibaba Cloud.

5. **Validación y confirmación**: Tras el inicio de los sistemas de negocio, realizar una validación de negocio exhaustiva para confirmar el funcionamiento normal.

6. **Conmutación DNS**: Una vez superada la validación de negocio, realizar la conmutación DNS para dirigir el tráfico de negocio hacia Alibaba Cloud.

## Resultados de la migración

Todo el proceso de migración duró 3 meses:

- **Escala de la migración**: Se migraron más de 50 servidores y más de 30 sistemas de aplicaciones
- **Tiempo de inactividad**: El tiempo de inactividad máximo en una sola migración se mantuvo en menos de 2 horas
- **Integridad de los datos**: Se garantizó el 100 % de la integridad de los datos con cero pérdida de datos
- **Continuidad del negocio**: Excepto por los tiempos de inactividad planificados, el negocio nunca se interrumpió

## Lecciones aprendidas

1. **Investigación previa exhaustiva**: Antes de la migración, realizar una investigación exhaustiva de los sistemas de TI existentes para comprender su arquitectura, dependencias y características de negocio.

2. **Plan de migración detallado**: Elaborar un plan de migración detallado que incluya el orden de migración, las ventanas de tiempo y las estrategias de reversión.

3. **Pruebas exhaustivas**: Realizar pruebas exhaustivas antes de la migración formal, incluyendo pruebas funcionales, pruebas de rendimiento y pruebas de recuperación ante desastres.

4. **Colaboración en equipo**: La migración es una tarea compleja que requiere una estrecha colaboración entre múltiples equipos, incluyendo equipos de negocio, equipos de TI y proveedores de servicios en la nube.

5. **Monitoreo continuo**: Una vez completada la migración, monitorear continuamente las operaciones del sistema para identificar y resolver cualquier problema de manera oportuna.
