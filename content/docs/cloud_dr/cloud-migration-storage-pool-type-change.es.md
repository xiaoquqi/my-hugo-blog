---
title: Cómo cambiar el tipo de grupo de almacenamiento durante la migración
date: 2021-12-03T07:08:26+08:00
author: Ray Sun
tags:
  - Migración a la nube
  - Almacenamiento
  - HyperMotion
categories:
  - Migración a la nube
draft: false
---

Durante la migración a la nube, la selección y gestión de los grupos de almacenamiento es un tema importante. A veces elegimos un tipo de grupo de almacenamiento al inicio de la migración, pero necesitamos cambiarlo a otro tipo durante el proceso. Este artículo explica cómo cambiar el tipo de grupo de almacenamiento en HyperMotion.

<!-- more -->

## Tipos de grupos de almacenamiento

En la migración a la nube, existen principalmente dos tipos de grupos de almacenamiento:

### 1. Almacenamiento de objetos

El almacenamiento de objetos (Object Storage) es un método de almacenamiento de alta disponibilidad y alta confiabilidad, adecuado para almacenar grandes cantidades de datos no estructurados. Las principales plataformas en la nube ofrecen los siguientes servicios de almacenamiento de objetos:
- Alibaba Cloud OSS
- Tencent Cloud COS
- AWS S3
- Huawei Cloud OBS

Características del almacenamiento de objetos:
- Bajo costo: Es más económico que el almacenamiento en bloque
- Capacidad ilimitada: Puede almacenar datos de cualquier tamaño
- Mayor latencia de acceso: En comparación con el almacenamiento en bloque, presenta una latencia de acceso más alta

### 2. Almacenamiento en bloque

El almacenamiento en bloque (Block Storage) es un método de almacenamiento de baja latencia y alto rendimiento, adecuado para escenarios que requieren lecturas y escrituras frecuentes. Las principales plataformas en la nube ofrecen los siguientes servicios de almacenamiento en bloque:
- Alibaba Cloud EBS (Elastic Block Storage)
- Tencent Cloud CBS (Cloud Block Storage)
- AWS EBS
- Huawei Cloud EVS

Características del almacenamiento en bloque:
- Alto rendimiento: Baja latencia, alto IOPS
- Mayor costo: Más caro que el almacenamiento de objetos
- Capacidad limitada: Sujeto a las restricciones de la plataforma en la nube, los discos individuales tienen un límite de capacidad máxima

## ¿Por qué cambiar el tipo de grupo de almacenamiento?

Razones por las que podría necesitar cambiar el tipo de grupo de almacenamiento durante la migración:

1. **Optimización de costos**: Inicialmente eligió un almacenamiento en bloque de alto rendimiento pero costoso, y descubrió durante la migración que el almacenamiento de objetos puede satisfacer sus necesidades, por lo que cambia para reducir costos.

2. **Cambio en los requisitos de rendimiento**: Inicialmente evaluó que el rendimiento del almacenamiento de objetos sería suficiente, pero encontró durante la migración real que los tiempos de recuperación eran demasiado largos y necesitaba cambiar al almacenamiento en bloque para mejorar el rendimiento.

3. **Limitaciones de cuota**: Debido a las restricciones de cuota de la plataforma en la nube, ya no puede continuar usando el tipo de almacenamiento original y necesita cambiar a otro tipo.

## Cambiar el grupo de almacenamiento en HyperMotion

HyperMotion proporciona capacidades flexibles de gestión de grupos de almacenamiento, lo que permite a los usuarios cambiar el tipo de grupo de almacenamiento durante la migración.

### Pasos

1. **Detener la sincronización de datos**: Antes de cambiar el grupo de almacenamiento, primero debe detener cualquier tarea de sincronización de datos en curso.

2. **Crear un nuevo grupo de almacenamiento**: En la consola de HyperMotion, cree un nuevo grupo de almacenamiento del tipo deseado y configure los parámetros relevantes.

3. **Migrar los datos**: Migre los datos existentes del grupo de almacenamiento antiguo al nuevo. Este proceso puede llevar algún tiempo dependiendo del volumen de datos.

4. **Actualizar la configuración**: Una vez completada la migración de datos, actualice la configuración del grupo de almacenamiento del host para que apunte al nuevo grupo de almacenamiento.

5. **Reiniciar la sincronización**: Una vez actualizada la configuración, reinicie las tareas de sincronización de datos.

### Notas

- Durante el cambio de grupo de almacenamiento, asegúrese de mantener la integridad y coherencia de los datos.
- Cambiar el grupo de almacenamiento causará un período de interrupción en la sincronización de datos; planifique la ventana de tiempo con anticipación.
- Una vez completado el cambio, realice pruebas exhaustivas para asegurarse de que las tareas de migración puedan ejecutarse normalmente.

## Mejores prácticas

En la práctica, recomendamos:

1. Antes de iniciar el proyecto de migración, evalúe exhaustivamente sus requisitos de almacenamiento y elija el tipo de almacenamiento adecuado.
2. Si no está seguro, puede usar primero el almacenamiento de objetos para realizar pruebas y luego decidir si necesita cambiar al almacenamiento en bloque según las condiciones reales.
3. Antes de cambiar el grupo de almacenamiento, asegúrese de haber realizado copias de seguridad y pruebas adecuadas.
