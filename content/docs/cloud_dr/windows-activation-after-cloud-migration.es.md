---
title: ¿Cómo activar Windows después de migrar a la nube?
slug: how-to-activiate-windows-after-cloud-migration
aliases:
  - /2021/11/19/windows%E7%B3%BB%E7%BB%9F%E8%BF%81%E7%A7%BB%E4%B8%8A%E4%BA%91%E5%90%8E%E5%A6%82%E4%BD%95%E6%BF%80%E6%B4%BB/
author: Ray Sun
date: 2021-11-19 08:06:32
tags:
  - Migración a la nube
  - Recuperación ante desastres en la nube
draft: false
---
Cuando se utiliza el enfoque de migración de máquina completa (Re-Host) para migrar Windows a una plataforma en la nube, el hardware subyacente cambia, lo que invalida la clave de licencia de Windows y requiere una nueva activación. Para los usuarios empresariales, ¿cómo proteger la inversión existente y activar el sistema de forma legítima sin incurrir en costes adicionales? Este artículo ofrece un análisis detallado basado en las mejores prácticas de proyectos reales.

<!-- more -->

## ¿Por qué la licencia queda inválida después de la migración?

Según Microsoft: cuando se instala Windows, la licencia digital queda asociada al hardware del dispositivo. Si se realizan cambios significativos en el hardware del dispositivo (como reemplazar la placa base), Windows no podrá encontrar una licencia que coincida con el dispositivo, y será necesario reactivar Windows para que funcione correctamente.

Basado en el enfoque de migración utilizado por la herramienta de migración nativa en la nube HyperMotion, que realiza copias a nivel de bloque en la capa subyacente, una vez que el sistema se inicia, el hardware subyacente cambia a los dispositivos virtuales de la plataforma en la nube. Este cambio de hardware provoca la invalidación de la licencia. Debido a cómo funcionan las plataformas en la nube, este cambio es inevitable, por lo que no hay forma de prevenir este problema en la capa de virtualización. Por tanto, al migrar o configurar la recuperación ante desastres en nubes públicas o privadas, se necesitan diferentes enfoques para abordar esta situación.

## Nube pública

Según la documentación pública disponible, la gran mayoría de las nubes públicas utilizan KMS para activar Windows automáticamente.

![upload successful](/images/pasted-280.png)

También es posible configurar la activación automática mediante un script de inicio:

```
cscript /nologo %windir%/system32/slmgr.vbs -skms kms.tencentyun.com:1688
cscript /nologo %windir%/system32/slmgr.vbs -ato
```

Huawei Cloud utiliza un enfoque similar: activación por lotes a través de un servidor KMS interno.

![upload successful](/images/pasted-281.png)

### Conservar la licencia original

Este enfoque solo aparece documentado en materiales de AWS. Se denomina License Mobility, pero requiere contactar con el revendedor de la licencia original para presentar la solicitud correspondiente.

![upload successful](/images/pasted-282.png)

## Nube privada

Los clientes de nube privada son en su mayoría empresas que generalmente han adquirido licencias de volumen legítimas. Las licencias de volumen ofrecen cierta flexibilidad en el número de activaciones permitidas. Debe quedar claro un requisito previo: los usuarios empresariales deben haber adquirido licencias de volumen legítimas; las licencias minoristas quedan fuera del alcance de esta discusión.

En primer lugar, es importante aclarar un concepto: una licencia y el número de activaciones son dos cosas completamente distintas. El número de licencias es fijo, mientras que el número de activaciones es flexible. Esta flexibilidad es precisamente lo que permite resolver el problema de activación de licencias tras la migración de sistemas de negocio. El enfoque es el siguiente:

* Supongamos que un usuario ha adquirido 10 licencias de Windows Server. En el Centro de servicios de licencias por volumen de Microsoft, el usuario debería tener 50 activaciones disponibles.
* El usuario ya tiene instalados y activados 10 servidores Windows y ahora necesita migrarlos.
* Usando la capacidad de migración en caliente de HyperMotion, Windows se migra desde un entorno VMware a la plataforma en la nube sin agente, sin impacto en la continuidad del negocio.
* El usuario quiere utilizar la función de validación de migración de HyperMotion para construir rápidamente un entorno de simulación. Las 10 instancias de Windows se inician en la plataforma en la nube (mientras los sistemas de negocio originales siguen funcionando con normalidad).
* Debido a que la capa de virtualización ha cambiado, las instancias de Windows iniciadas se encuentran en estado no activado (Windows 2012, si está conectado a Internet, intentará activarse automáticamente), pero esto no afecta a la validación del sistema de negocio.
* Tras validar el entorno y confirmar que el negocio opera correctamente, el cliente se prepara para la transferencia del sistema.
* Después de la sincronización incremental final, los sistemas de negocio originales se apagan, los sistemas de negocio se inician en la VPC de producción con las direcciones IP sin cambios.
* Tras la transferencia, las instancias de Windows siguen en estado no activado. Con conexión a Internet, se usan los números de serie originales para reactivarlas.
* La migración del sistema de negocio se completa y Windows queda activado.

Si el recuento de activaciones alcanza su límite, ¿qué se debe hacer? Tras consultar con el servicio de atención al cliente 400 de Microsoft, se confirmó que para las licencias de volumen empresariales, el recuento de activaciones puede ampliarse de forma gratuita. Basta con presentar una solicitud en este enlace (https://support.microsoft.com/en-us/supportrequestform/2afa6f15-b710-db46-909a-8346017c802f?sl=en&sc=US). Una vez que Microsoft complete la verificación en aproximadamente 5 días hábiles, los usuarios pueden acceder al Centro de servicios de licencias por volumen de Microsoft para consultar el recuento de activaciones disponibles, o contactar directamente con Microsoft a través del teléfono 400 para comentar las opciones de ampliación. Tenga en cuenta que esta opción solo está disponible una vez que se haya alcanzado el límite de activaciones.

![upload successful](/images/pasted-283.png)

El flujo de trabajo general se muestra en el siguiente diagrama:

![upload successful](/images/pasted-284.png)

## ¿Windows se reiniciará automáticamente si no está activado?

Según la información proporcionada por el servicio de atención al cliente 400 de Microsoft, debido a las políticas de protección de software genuino, Windows puede desencadenar varios eventos aleatorios; el reinicio es uno de ellos, pero no ocurre el 100% de las veces. El problema que sí aparece de forma periódica garantizada es el recordatorio de activación.

## Resumen

* Para entornos de nube pública, se recomienda utilizar el servicio KMS proporcionado por la propia plataforma de nube pública.
* Para entornos de nube privada, si ha adquirido licencias de volumen empresariales, no necesita preocuparse por los problemas de activación de licencias: Microsoft le ayudará a resolver el problema de activación.
