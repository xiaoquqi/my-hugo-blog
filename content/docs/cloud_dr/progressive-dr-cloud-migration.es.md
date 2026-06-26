---
title: Migración progresiva a la nube con recuperación ante desastres
description: "Estrategia de migración por fases con HyperBDR: comienza con DR, valida el entorno cloud y después conmuta las cargas de trabajo principales, minimizando el riesgo."
date: 2022-09-22 12:08:00
author: Ray Sun
tags:
  - Recuperación ante desastres
  - Migración a la nube
  - HyperBDR
categories:
  - Computación en la nube
draft: false
---

La migración progresiva a la nube es una estrategia para trasladar cargas de trabajo a la nube de manera gradual, en lugar de migrar todo de una sola vez. Este enfoque reduce el riesgo de la migración y al mismo tiempo le da tiempo a las empresas para adaptarse al entorno de computación en la nube.

<!-- more -->

## ¿Qué es la migración progresiva a la nube?

La migración progresiva a la nube se refiere al proceso de trasladar los sistemas de negocio a la nube de forma incremental, según la prioridad y el nivel de riesgo. El enfoque habitual es:

1. Migrar primero los sistemas de negocio no críticos
2. Validar la estabilidad del entorno en la nube
3. Migrar gradualmente los sistemas de negocio críticos

## Combinación de la recuperación ante desastres con la migración progresiva

Combinar la recuperación ante desastres con la migración progresiva es una estrategia de migración muy eficaz. La idea central es:

1. **Fase 1: Establecer la recuperación ante desastres**: Configurar la protección de recuperación ante desastres para los sistemas de negocio en la nube, mientras las cargas de trabajo principales continúan ejecutándose en las instalaciones locales.
2. **Fase 2: Validar la recuperación ante desastres**: Realizar simulacros de recuperación ante desastres para verificar la disponibilidad del entorno en la nube y sus capacidades de recuperación de negocio.
3. **Fase 3: Conmutar principal y secundario**: Cambiar la nube de modo secundario a modo principal, mientras el entorno local pasa a ser el secundario.
4. **Fase 4: Completar la migración**: Una vez confirmada la estabilidad de las operaciones en la nube, desmantelar gradualmente el entorno local y completar la migración.

Las ventajas de esta estrategia son:
- **Riesgo controlado**: Cada fase conlleva un riesgo controlable, y los problemas pueden revertirse rápidamente si surgen.
- **Continuidad del negocio**: Durante todo el proceso de migración, las operaciones de negocio se mantienen continuas.
- **Validación incremental**: La estabilidad del entorno en la nube puede verificarse progresivamente, reduciendo el riesgo de fallo en la migración.

## Solución de migración progresiva de HyperBDR

HyperBDR proporciona una solución completa de migración progresiva:

### Fase 1: Establecer la protección de recuperación ante desastres

Use HyperBDR para establecer la protección de recuperación ante desastres en la nube:

1. Instalar el agente HyperBDR
2. Configurar la plataforma en la nube de destino
3. Iniciar la sincronización de datos
4. Monitorear el estado de la sincronización

### Fase 2: Simulacros de recuperación ante desastres

Realice simulacros de recuperación ante desastres sin afectar el entorno de producción:

1. Activar el flujo de trabajo del simulacro
2. HyperBDR crea automáticamente máquinas virtuales en la nube
3. Validar la disponibilidad de los sistemas de negocio
4. Destruir las máquinas virtuales del simulacro al finalizar

### Fase 3: Conmutación formal

Una vez confirmada la estabilidad del entorno en la nube, realizar la conmutación formal del negocio:

1. Detener las operaciones de negocio en el entorno de producción
2. Esperar a que se complete la sincronización de datos final
3. Activar el flujo de trabajo de conmutación de HyperBDR
4. Validar que los sistemas de negocio en la nube funcionen con normalidad
5. Apuntar el DNS o los balanceadores de carga hacia la nube

### Fase 4: Retroceso (opcional)

Si se detectan problemas tras la migración, HyperBDR admite operaciones de retroceso:

1. Detener las operaciones de negocio en la nube
2. Sincronizar los datos desde la nube de vuelta a las instalaciones locales
3. Restaurar los sistemas de negocio locales

## Caso práctico real

En una ocasión ayudamos a una empresa manufacturera a usar la estrategia de migración progresiva para migrar con éxito sus sistemas de negocio críticos a Alibaba Cloud:

- **Fase 1** (2 meses): Se estableció la protección de recuperación ante desastres y se completó la sincronización de datos
- **Fase 2** (1 mes): Se realizaron 3 simulacros de recuperación ante desastres para validar la estabilidad del entorno en la nube
- **Fase 3** (1 semana): Se completó la conmutación formal durante horas de baja actividad, con un tiempo de inactividad de menos de 30 minutos

Durante todo el proceso de migración, la continuidad del negocio quedó plenamente garantizada y el cliente quedó muy satisfecho con el resultado de la migración.

## Resumen

La migración progresiva a la nube combinada con la tecnología de recuperación ante desastres es una estrategia segura y confiable para que las empresas avancen hacia la nube. La solución completa de HyperBDR ayuda a las empresas a completar su migración a la nube de manera fluida, garantizando al mismo tiempo la continuidad del negocio.
