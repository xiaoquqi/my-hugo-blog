---
title: Reflexiones sobre migración y recuperación ante desastres en la era Cloud Native
slug: cloud-migration-dr-on-cloud-native
author: Ray Sun
tags:
  - Computación en la Nube
  - Cloud Native
  - Migración a la Nube
  - Recuperación ante Desastres en la Nube
  - Cloud Native
  - Análisis de Tendencias
categories: []
date: 2022-10-18 20:05:00
draft: false
---
## Tendencias

### El auge de Cloud Native

Cloud Native es uno de los temas más candentes en la industria de TI en los últimos años. En julio de 2020, la Academia China de Tecnologías de la Información y las Comunicaciones (CAICT) publicó el *Libro Blanco sobre el Desarrollo Cloud Native (2020)*, señalando explícitamente que la computación en la nube ha llegado a un punto de inflexión y que Cloud Native se ha convertido en un motor crítico para el crecimiento empresarial. Es fácil ver que Cloud Native está barajando nuevamente toda la industria de TI, desde los procesos de desarrollo de aplicaciones hasta las habilidades técnicas requeridas de los profesionales de TI: esta es una revolución disruptiva. Sobre esta base, ha surgido el Open Application Model (OAM) como una abstracción adicional construida sobre plataformas Cloud Native, desplazando el foco de la infraestructura hacia las aplicaciones. Al mismo tiempo, un número creciente de nubes públicas están adoptando servicios Serverless, lo que subraya aún más la dirección futura: las aplicaciones en el centro, con una capa de infraestructura ligera en un rol de soporte. Independientemente de cómo evolucionen las cosas, la dirección general de TI siempre avanzará hacia una iteración empresarial más rápida y una mejor satisfacción de las necesidades del negocio.

En septiembre de 2020, Snowflake salió a bolsa a 120 dólares por acción, marcando la mayor OPI de ese año y la mayor OPI de software en la historia. Snowflake reconstruyó el almacén de datos usando principios Cloud Native, interrumpiendo con éxito el panorama competitivo de esa industria. Esto valida perfectamente el reconocimiento del mercado de la tendencia Cloud Native. ¿Podría el próximo dominio a ser disruptado por Cloud Native ser el espacio tradicional de la recuperación ante desastres (DR)?

<!-- more -->

### Por qué la Nube Necesita Migración y Recuperación ante Desastres Completamente Nuevas

#### 1. Limitaciones de los Enfoques Tradicionales

En este contexto, la migración y el DR tradicionales siguen estancados en el nivel de simplemente mover datos, ignorando la necesidad de repensar y reconstruir en torno a las características de la nube y las necesidades del negocio del usuario. La visión de la computación en la nube es hacer que los recursos de la nube sean tan bajo demanda como los servicios públicos como el agua y la electricidad, por lo que la migración y el DR en la nube naturalmente deben seguir esta tendencia. Snowflake tuvo éxito al innovar en este modelo de negocio, rompiendo el antiguo paradigma competitivo.

¿Por qué los enfoques de DR tradicionales no pueden satisfacer los requisitos Cloud Native? En pocas palabras, los dos se centran en cosas fundamentalmente diferentes. El DR tradicional está centrado en el almacenamiento, confiando en el control supremo sobre el almacenamiento. En la era física, tampoco había mecanismos de programación efectivos para las capas de infraestructura como cómputo, almacenamiento y redes, lo que hacía imposible la orquestación altamente automatizada. En las aplicaciones Cloud Native, el núcleo ha cambiado hacia los propios servicios Cloud Native. Una vez que los sistemas empresariales de un usuario están completamente en la nube, el usuario ya no tiene control absoluto sobre el almacenamiento subyacente, haciendo que los enfoques de DR tradicionales queden obsoletos.

![upload successful](/images/pasted-88.png)

Creo que al construir soluciones de DR Cloud Native, el enfoque debe estar centrado en el negocio, aprovechando las capacidades de orquestación de los servicios Cloud Native para lograr la continuidad del negocio.

#### 2. Seguridad de los Datos

El CTO de AWS, Werner Vogels, dijo una vez: "Everything fails, all the time." A través del modelo de responsabilidad compartida de AWS, queda claro que los proveedores de nube son responsables de la infraestructura subyacente, mientras que los usuarios siguen siendo responsables de su propia seguridad de datos y continuidad del negocio.

![upload successful](/images/pasted-74.png)

Creo que en la era Cloud Native, la necesidad más inmediata del usuario es la seguridad de los datos, es decir, la copia de seguridad. La migración, la recuperación y la alta disponibilidad son todas manifestaciones empresariales construidas sobre la copia de seguridad. La capacidad de copia de seguridad puede ser proporcionada por servicios Cloud Native o por soluciones de terceros, pero los resultados empresariales finales se producen a través de la orquestación.

Ir a la nube no significa tranquilidad. Por el contrario, los usuarios necesitan aprender a usar la nube correctamente para maximizar la continuidad del negocio. Aunque la nube está diseñada para una alta fiabilidad a nivel de infraestructura, las fuerzas externas aún pueden causar interrupciones, como cables de fibra cortados, cortes de energía o errores humanos que hacen que una zona de disponibilidad de la nube quede inutilizable. Por eso hay chistes como "la estabilidad de la computación en la nube de China depende de los operadores de retroexcavadoras." Creo que desde el momento en que un usuario decide migrar su negocio a la nube, la copia de seguridad, la migración, la recuperación y la alta disponibilidad forman un proceso continuo. El desafío es cómo aprovechar las características del servicio Cloud Native para lograr la continuidad del negocio mientras se optimizan los costos y se reduce el costo total de propiedad (TCO).

#### 3. Evitar el Bloqueo del Proveedor

En cierto sentido, la dirección Cloud Native representa una nueva ola de bloqueo de proveedores, similar a la arquitectura IOE que alguna vez dominó, excepto que ahora los proveedores de nube sirven como base para las aplicaciones. En la era IOE, los usuarios tenían dificultades para encontrar reemplazos adecuados. En la era de la nube, las diferencias son menos pronunciadas. Como resultado, la mayoría de los clientes eligen la nube híbrida como su estrategia de nube. Para permitir que las aplicaciones se muevan fluidamente entre nubes, la migración usando tecnología de DR inevitablemente se convertirá en un requisito normalizado. Gartner también lista la migración y el DR como una capacidad distinta en su definición de plataforma de gestión multinube, destacando aún más la tendencia normalizada de migración y DR en entornos multinube.

![upload successful](/images/pasted-82.png)


## La Relación Entre la Migración a la Nube y la Recuperación ante Desastres en la Nube

### El Surgimiento de la Demanda de Migración a la Nube

En los entornos tradicionales, la migración no era una necesidad frecuente: solo surgía durante reubicaciones de centros de datos o actualizaciones de hardware, e incluso entonces era más como mover hardware físicamente. La necesidad de herramientas de migración automatizadas no era particularmente evidente. Cuando apareció VMware, creció la demanda de migración de físico a virtual, pero dado que era una sola plataforma de virtualización, las herramientas proporcionadas por el proveedor eran en gran medida suficientes. En las plataformas de virtualización, lo que antes requería esfuerzo físico manual de repente se volvió ligero: los servidores tradicionales pasaron de ser un montón de hardware a ser un archivo que podía moverse y copiarse. Luego llegó la era de la nube, con plataformas de nube en auge y el mercado de computación en la nube chino volviéndose muy competitivo. Moverse a la nube se convirtió en un requisito obligatorio. Con el tiempo, factores como el costo y el bloqueo de proveedores han hecho que la migración entre nubes sea una demanda cada vez más normalizada.

### Tecnología Subyacente Compartida

La migración a la nube y el DR discutidos aquí no se refieren a servicios de migración entregados por grandes equipos de personas: enfatizan enfoques altamente automatizados. El objetivo es garantizar la continuidad del negocio durante la migración, minimizando o incluso eliminando el tiempo de inactividad. Esto aprovecha la tecnología de sincronización a nivel de almacenamiento del DR para lograr una "migración en vivo" en entornos heterogéneos. Las soluciones existentes van desde herramientas de migración tradicionales diseñadas para la era de las máquinas físicas hasta herramientas construidas sobre principios Cloud Native. Independientemente de la forma, todas abordan los requisitos básicos de los usuarios para moverse a la nube en distintos grados. El mayor diferenciador es la eficiencia humana, lo cual impacta directamente en los resultados económicos.

Desde otro ángulo, la migración es esencialmente un proceso intermedio de DR hasta el corte final. Además, una vez que un sistema empresarial se migra a una plataforma de nube, la recuperación ante desastres se convierte en una actividad continua que abarca no solo la copia de seguridad tradicional y el DR, sino también los conceptos de alta disponibilidad nativos de la nube. Solo entonces los sistemas empresariales de los usuarios pueden liberarse de la carga de la infraestructura tradicional después de ir a la nube, lograr "cero operaciones" y beneficiarse verdaderamente de lo que la nube tiene para ofrecer. Por lo tanto, creo que en el estado Cloud Native, la migración a la nube, el DR en la nube y la copia de seguridad en la nube son fundamentalmente la misma forma de negocio, y los medios técnicos subyacentes pueden ser completamente idénticos.

### Dirección del Desarrollo

Contra el telón de fondo de los puntos de dolor y las tendencias descritos anteriormente, inevitablemente surgirá una plataforma completamente nueva para ayudar a los clientes a abordar los desafíos de seguridad de datos y continuidad del negocio. Analicemos desde esta perspectiva cómo construir soluciones de migración y DR para sistemas de aplicaciones en la era Cloud Native.

## Tendencias de Migración a la Nube

### Enfoques de Migración a la Nube

La migración es un negocio de consultoría intensivo. Los proveedores de nube y los MSP tienen sus propias metodologías en línea, pero no difieren mucho. Muchas personas han compartido temas relacionados antes, por lo que este artículo no los repetirá. En cambio, nos centramos en qué herramientas y enfoques son más efectivos en la implementación real. Las herramientas de migración a la nube mueven cargas de trabajo desde el origen al destino, asegurando que las cargas de trabajo se ejecuten correctamente en el destino. Los escenarios comunes incluyen: físico a virtual, virtual a virtual, físico a nube y virtual a nube.

![upload successful](/images/pasted-62.png)

Esta es la teoría de migración clásica de las 6R (ahora actualizada a 7R, con VMware añadido). En este diagrama, solo Rehosting, Replatforming, Repurchasing y Refactoring están verdaderamente relacionados con la migración. Entre estos cuatro, Refactoring es claramente un proceso iterativo a largo plazo que requiere colaboración entre usuarios y proveedores de software. Repurchasing es esencialmente equivalente a la reimplementación manual. Entonces lo que es realísticamente alcanzable por usuarios o MSPs a corto plazo es solo Rehosting y Replatforming.

En comparación con el diagrama clásico de teoría de migración anterior, prefiero el siguiente diagrama, que refleja mejor el viaje completo de una aplicación tradicional evolucionando hacia una aplicación Cloud Native. Similar a la conclusión anterior, al abrazar verdaderamente la nube, los caminos son esencialmente los siguientes tres:

* Lift & Shift es otro nombre para el enfoque Rehost. Este camino es el más amplio, simbolizando el camino más corto hacia la nube: las aplicaciones van a la nube sin ninguna modificación.
* Evolve y Go Native son caminos más estrechos, simbolizando que en comparación con Rehost, estos caminos toman más tiempo y son más desafiantes.
* En el lado derecho del diagrama, los tres estados pueden convertirse entre sí, evolucionando finalmente hacia Cloud Native completo, simbolizando que la migración no es un evento único sino un proceso gradual.

![upload successful](/images/pasted-61.png)

### Enfoque de Rehosting

Los métodos comunes de rehosting incluyen la migración en frío y la migración en vivo. La migración en frío a menudo involucra pasos complejos, requiere un esfuerzo manual significativo, es propensa a errores, tiene baja eficiencia e impacta significativamente la continuidad del negocio, lo que la hace inadecuada para la migración de sistemas de producción. Las soluciones de migración en vivo son generalmente comerciales y pueden dividirse adicionalmente en nivel de bloque y nivel de archivo, y luego en enfoques tradicionales versus Cloud Native.

#### Migración en Frío

Veamos primero el enfoque de migración en frío manual, usando VMware a OpenStack como ejemplo. El método más simple es convertir los archivos de máquina virtual de VMware (VMDK) usando la herramienta qemu-img al formato QCOW2 o RAW, cargarlos en el servicio OpenStack Glance y luego reiniciar las instancias en la plataforma de nube. Este proceso requiere inyectar controladores virtio, de lo contrario el host no puede iniciarse normalmente en la plataforma de nube. El paso más lento es cargar los archivos de máquina virtual a OpenStack Glance. En nuestra práctica más temprana, tomó nada menos que 24 horas desde el inicio de la migración hasta el inicio exitoso de un solo host. Además, se generan datos incrementales durante el período de migración. A menos que apague el origen mientras espera que se complete la migración, deberá repetir todos los pasos anteriores. Este enfoque es verdaderamente inadecuado para sistemas de producción con requisitos de continuidad del negocio.

¿Qué hay de la migración en frío para máquinas físicas? Según nuestras mejores prácticas, recomendamos la veterana herramienta de copia de seguridad CloneZilla. Es un software de copia de seguridad clásico comúnmente utilizado para copia de seguridad y recuperación de sistemas completos, muy similar en principio a Norton Ghost. CloneZilla realiza copias de nivel de bloque desde abajo hacia arriba, puede hacer copias de seguridad de discos completos y admite múltiples formatos de destino. Sin embargo, CloneZilla requiere arrancar a través de un Live CD, lo que inevitablemente conduce a largos períodos de inactividad del sistema empresarial, razón por la cual la migración en frío no es adecuada para migraciones en entornos de producción.

![upload successful](/images/pasted-63.png)

![upload successful](/images/pasted-64.png)

#### Enfoques Tradicionales de Migración en Vivo

Las soluciones de migración en vivo tradicionales se dividen generalmente en nivel de bloque y nivel de archivo, ambas aprovechando la tecnología de sincronización delta, es decir, sincronización alternada de datos completos e incrementales.

Las soluciones de migración en vivo a nivel de archivo tienden a tener limitaciones significativas y no pueden considerarse realmente un enfoque Rehost verdadero. Requieren preparar un sistema operativo idéntico al origen de antemano y no pueden lograr la migración de sistema completo. Tanto la complejidad operativa como la estabilidad de la migración son menores. El Rsync comúnmente utilizado en Linux puede servir como solución de migración en vivo a nivel de archivo.

Para un verdadero enfoque de migración en vivo, debe usarse la sincronización a nivel de bloque para reducir la dependencia del sistema operativo subyacente y lograr la migración de sistema completo. Las soluciones tradicionales de migración en vivo a nivel de bloque son esencialmente variantes de las soluciones de DR tradicionales, implementadas usando sistemas operativos en memoria como Win PE u otros Live CDs. Aunque este enfoque aborda los objetivos de migración hasta cierto punto, aún tiene las siguientes deficiencias para la migración normalizada futura en nubes híbridas:

* Dado que las soluciones tradicionales de migración en vivo están construidas sobre entornos físicos, hay mucha intervención manual a lo largo del proceso, lo que requiere altas habilidades técnicas de los usuarios.
* No puede satisfacer los requisitos de multitenencia y autoservicio de la era Cloud Native.
* Instalar un agente siempre es una preocupación que tienen los usuarios.
* La sincronización uno a uno no es rentable.
* El mejor método de verificación de migración es restaurar completamente el clúster del sistema empresarial en la nube, pero la verificación manual aumenta nuevamente los costos de mano de obra de migración.

![upload successful](/images/pasted-67.png)


#### Enfoques de Migración en Vivo Cloud Native

Es precisamente debido a los inconvenientes de las soluciones de migración tradicionales que han surgido los enfoques de migración en vivo Cloud Native. El proveedor líder en este espacio es CloudEndure, una empresa israelí de DR y migración Cloud Native que AWS adquirió en 2019 por 250 millones de dólares, superando a Google Cloud.

La migración en vivo Cloud Native se refiere a aprovechar la tecnología de sincronización delta a nivel de bloque combinada con APIs y recursos Cloud Native para lograr una migración altamente automatizada, mientras también proporciona multitenencia e interfaces API para satisfacer los requisitos de autoservicio de los inquilinos de nubes híbridas. Analicemos desde una perspectiva de principios por qué el enfoque Cloud Native puede cumplir los requisitos de alta automatización y experiencia de usuario de autoservicio en comparación con las soluciones tradicionales. Comparando los dos enfoques, se destacan varias ventajas del enfoque Cloud Native:

* El uso de APIs y recursos Cloud Native simplifica las operaciones, reemplazando completamente los numerosos pasos manuales tediosos en las soluciones tradicionales. Los requisitos técnicos para los usuarios son menores y la curva de aprendizaje se reduce significativamente.
* Debido a las operaciones más simples, la eficiencia de migración mejora, aumentando efectivamente la relación de eficiencia humana de las implementaciones de migración.
* Un enfoque de sincronización de uno a muchos reduce significativamente el uso de recursos de cómputo: los recursos de cómputo solo se usan durante la verificación y el corte final.
* Puede satisfacer los requisitos de multitenencia y autoservicio.
* El modo sin agente en el lado del origen también es compatible, aliviando las preocupaciones de los usuarios y adecuado para la migración masiva en lotes.
* Medios de verificación altamente automatizados que permiten repetir la verificación múltiples veces antes de que se complete el corte de migración.

![upload successful](/images/pasted-69.png)

Este es el diagrama de arquitectura de CloudEndure. Por supuesto, también puede usar CloudEndure para implementar DR entre regiones.

![upload successful](/images/pasted-70.png)

Desafortunadamente, dado que CloudEndure fue adquirido por AWS, actualmente solo admite migración a AWS y no puede satisfacer las necesidades de varias migraciones en la nube en China. Aquí recomendamos una plataforma de migración completamente desarrollada en el país: HyperMotion de OneProCloud (https://hypermotion.oneprocloud.com/). En principio es muy similar a CloudEndure, mientras que también admite migración sin agente para VMware y OpenStack. Más importante aún, cubre la migración a todas las principales nubes públicas, nubes propietarias y nubes privadas en China.


![upload successful](/images/pasted-71.png)

### Enfoque de Replatforming

A medida que Cloud Native proporciona más y más servicios, reduce la complejidad de la arquitectura de aplicaciones, permitiendo a las empresas centrarse más en el desarrollo de su negocio principal. Sin embargo, la reducción de la carga de trabajo de I+D significa que esta parte del costo se transfiere al lado de implementación y operaciones, haciendo de DevOps un componente indispensable en la adopción de Cloud Native, y permitiendo a las empresas responder a los cambios empresariales complejos de manera más ágil.

Como se mencionó anteriormente, los usuarios pueden priorizar el uso de algunos servicios Cloud Native a través de modificaciones menores. Este enfoque de migración se llama Replatforming. Actualmente, las migraciones de Replatforming tienden a centrarse en servicios relacionados con los datos del usuario. Los ejemplos comunes incluyen: servicio de base de datos RDS, servicio de almacenamiento de objetos, servicio de cola de mensajes y servicio de contenedores. La introducción de estos servicios Cloud Native reduce los costos de operación y mantenimiento de los usuarios. Sin embargo, dado que los servicios Cloud Native están altamente encapsulados y la capa de infraestructura subyacente es completamente invisible para los usuarios, el enfoque Rehost anterior no puede usarse para la migración: deben emplearse medios suplementarios alternativos.

Tomando las bases de datos relacionales como ejemplo, casi todas las nubes proporcionan herramientas de migración, como AWS DMS, Alibaba Cloud DTS y Tencent Cloud Data Transfer Service DTS. Estas herramientas Cloud Native admiten la migración de múltiples bases de datos relacionales y NoSQL, incluyendo MySQL, MariaDB, PostgreSQL, Redis y MongoDB. Tomando MySQL como ejemplo, estos servicios aprovechan inteligentemente la replicación binlog para lograr la migración de bases de datos en línea.

Tomando el almacenamiento de objetos como otro ejemplo, casi todas las nubes proporcionan su propia herramienta de migración, como ossimport de Alibaba Cloud y la herramienta COS Migration de Tencent Cloud, ambas capaces de migración incremental desde almacenamiento local a almacenamiento de objetos en la nube. Sin embargo, el costo también debe considerarse en la migración real: el almacenamiento de objetos en nubes públicas es relativamente económico para almacenar datos, pero se aplican cargos por la salida de datos basados en el tráfico de red y el número de solicitudes. Esto requiere una consideración cuidadosa del costo al diseñar soluciones de migración. Para conjuntos de datos muy grandes, también pueden considerarse opciones de dispositivos sin conexión como AWS Snowball o el Lightning Cube de Alibaba Cloud.

![upload successful](/images/pasted-72.png)

Si elige el enfoque Replatforming para moverse a la nube, además de las modificaciones de aplicación necesarias, también necesita seleccionar una herramienta de migración apropiada para garantizar una migración fluida de datos a la nube. Combinado con el enfoque de migración Rehost descrito anteriormente, puede lograr la migración completa de sus sistemas empresariales a la nube. Dada la gran cantidad de servicios involucrados, se proporciona a continuación una tabla de referencia de herramientas de migración.

![upload successful](/images/pasted-89.png)

## Tendencias de Recuperación ante Desastres en la Era Cloud Native

Hasta la fecha, ninguna plataforma única puede satisfacer completamente las necesidades unificadas de DR en el estado Cloud Native. Analicemos cómo construir una plataforma de DR unificada que satisfaga los requisitos Cloud Native a través de los siguientes escenarios.

### Arquitectura Tradicional

Tomando un entorno simple de WordPress + MySQL como ejemplo, una implementación típica en un entorno tradicional se ve así:

![upload successful](/images/pasted-58.png)

Si tuviera que diseñar una solución de DR para esta arquitectura de aplicación, podría usar los siguientes enfoques:

* DR del balanceador de carga: Los balanceadores de carga pueden ser hardware o software. La alta disponibilidad y el DR del balanceador de carga de hardware se logran típicamente a través de sus propias soluciones. Para los balanceadores de carga de software, se requiere instalación en el sistema operativo base. El DR local (misma ciudad) se puede lograr mediante métodos de alta disponibilidad de software, mientras que el DR remoto se implementa típicamente pre-estableciendo nodos pares o usando DR a nivel de bloque o archivo con software de DR. Este es un componente crítico del failover.
* DR del servidor web: El entorno de ejecución de WordPress es esencialmente Apache + PHP. Dado que el sistema de archivos para los archivos cargados por usuarios está separado, este nodo es casi sin estado y puede lograr alta disponibilidad mediante escalado horizontal. El DR remoto es relativamente simple: los enfoques tradicionales de nivel de bloque o de archivo pueden satisfacer los requisitos de DR.
* DR del sistema de archivos compartido: El diagrama utiliza un sistema de archivos GlusterFS. Dado que la consistencia en los sistemas distribuidos generalmente se mantiene internamente, usar solo nivel de bloque es difícil para garantizar la consistencia de los nodos, por lo que el DR a nivel de archivo es más apropiado aquí.
* DR de bases de datos: Depender únicamente de la capa de almacenamiento no puede lograr fundamentalmente cero pérdida de datos para las bases de datos. La solución generalmente necesita implementarse a nivel de base de datos. Por supuesto, para reducir costos, el DR de bases de datos puede lograrse simplemente a través de volcados periódicos de bases de datos. Para requisitos de mayor fiabilidad, también puede usarse CDP (Protección Continua de Datos).

Del análisis de caso anterior, queda claro que el DR en la infraestructura tradicional está centrado en el almacenamiento, ya sea a través de duplicación de almacenamiento en matrices de discos o tecnología de captura a nivel de bloque de datos de E/S y nivel de byte, combinado con técnicas a nivel de aplicación para redes, bases de datos y clustering para construir arquitecturas de alta disponibilidad y DR. Los principales participantes en todo el proceso de DR son: hosts, almacenamiento, redes y software de aplicaciones, relativamente sencillo. Por lo tanto, en las soluciones de DR tradicionales, resolver correctamente el DR de almacenamiento es la clave para resolver el problema.

### Recuperación ante Desastres en Nube Híbrida

Este es actualmente el enfoque de nube híbrida más común y el promovido principalmente por los principales proveedores de DR. Aquí, la plataforma de nube se trata esencialmente como una plataforma de virtualización, con casi ninguna de las características únicas de la plataforma de nube utilizadas. Durante la recuperación, se requiere una intervención manual significativa para restaurar el sistema empresarial a un estado utilizable. Esta arquitectura no representa las mejores prácticas de la nube, pero es ciertamente una descripción precisa de cómo lucen muchos sistemas empresariales después de ser respaldados o migrados a la nube.

![upload successful](/images/pasted-83.png)

Esta arquitectura sí resuelve el problema de DR, pero el costo es alto. Consideremos una alternativa. Usamos almacenamiento de objetos y un servicio de base de datos para optimización. Los datos del servicio de almacenamiento original se colocan en almacenamiento de objetos, y se usa un servicio de transferencia de datos para replicación de bases de datos en tiempo real. Las VM en la nube todavía usan el enfoque de sincronización a nivel de bloque tradicional. Una vez que ocurre un fallo, se necesita orquestación automatizada para restaurar la copia de seguridad en el menor tiempo posible de acuerdo con nuestro plan preestablecido, completando el DR.

![upload successful](/images/pasted-84.png)

### Arquitectura de DR en la Misma Ciudad en la Nube

El enfoque de copia de seguridad descrito anteriormente es esencialmente una migración usando el enfoque Replatforming. Dado que la migración ya se ha usado para la copia de seguridad, la arquitectura puede modificarse adicionalmente como sigue para formar una arquitectura de DR en la misma ciudad. Siguiendo las mejores prácticas de la plataforma de nube, la arquitectura se ha ajustado de la siguiente manera:

![upload successful](/images/pasted-85.png)

Esta arquitectura no solo logra alta disponibilidad a nivel de aplicación sino que también admite ciertos niveles de alta concurrencia. Los usuarios pueden lograr una configuración activo-activo dentro de la misma ciudad con costos mínimos de modificación. Analicemos cuántos servicios Cloud Native se utilizan en la nube:

* Servicio DNS
* Servicio VPC
* Servicio de balanceo de carga
* Servicio de autoescalado
* Servicio de VM en la nube
* Servicio de almacenamiento de objetos
* Servicio de base de datos relacional RDS

Excepto las VM en la nube, todos los demás servicios admiten nativamente la alta disponibilidad entre zonas de disponibilidad. Para las VM en la nube, se pueden crear imágenes y gestionar por el servicio de autoescalado. Dado que las zonas de disponibilidad en la nube representan el concepto de DR en la misma ciudad, hemos logrado el DR del sistema empresarial en la misma ciudad.

La arquitectura ajustada cumple los requisitos de continuidad del negocio hasta cierto punto, pero la seguridad de los datos aún carece de protección suficiente. En los últimos años, los ataques de ransomware han proliferado, causando enormes pérdidas a muchas empresas. Por lo tanto, la copia de seguridad de datos debe implementarse después de ir a la nube. Los propios servicios Cloud Native proporcionan soluciones de copia de seguridad, como instantáneas periódicas para VM en la nube, pero estos servicios tienden a estar dispersos y son difíciles de gestionar de manera uniforme. Además, la recuperación a menudo requiere restaurar servicio por servicio. Para sistemas empresariales de gran escala, esto aumenta significativamente los costos de recuperación. Aunque los servicios Cloud Native resuelven sus propios desafíos de copia de seguridad, reorganizar las copias de seguridad en aplicaciones requiere capacidades de orquestación automatizada.

### Arquitectura de DR Interregional en la Misma Nube

La mayoría de los servicios Cloud Native dentro de una zona de disponibilidad proporcionan capacidades de alta disponibilidad, pero entre regiones generalmente solo se proporcionan capacidades de copia de seguridad. Por ejemplo: las VM en la nube pueden convertirse en imágenes y replicarse a otras regiones; las bases de datos relacionales y el almacenamiento de objetos también tienen capacidades de copia de seguridad entre regiones. Usando las propias capacidades de copia de seguridad de estos componentes junto con las capacidades de orquestación de recursos de la nube, podemos restaurar sistemas a un estado utilizable en la zona de DR. ¿Cómo activamos un corte?

Aquí, según las características del sistema empresarial, configuramos alertas en el monitoreo Cloud Native y usamos las capacidades de activación de la plataforma de alertas para activar la computación de funciones, completando el corte del sistema empresarial entre regiones para lograr el efecto de DR remoto.

![upload successful](/images/pasted-86.png)

### Recuperación ante Desastres entre Nubes

El DR entre nubes difiere del DR en la misma nube en que los servicios son al menos consistentes en diferentes zonas de disponibilidad dentro de la misma nube. En escenarios entre nubes, los métodos utilizados en la misma nube son esencialmente ineficaces, y se necesitan las capacidades de la plataforma de nube objetivo o soluciones neutrales de terceros. Más allá de la copia de seguridad de datos, también debe abordarse la correspondencia de configuración de servicios entre nubes para satisfacer completamente los requisitos de recuperación de DR entre nubes. El costo es otra consideración importante: toma el almacenamiento de objetos como ejemplo, es típicamente "fácil entrar, difícil salir." Por lo tanto, cómo diseñar racionalmente soluciones de DR aprovechando las características de los recursos Cloud Native es una prueba significativa para la gestión de costos.

![upload successful](/images/pasted-87.png)


## Resumen

El DR Cloud Native todavía está en sus primeras etapas. Actualmente, ninguna plataforma completa puede soportar los requisitos de DR para todos los escenarios descritos anteriormente: es un tema que vale la pena explorar continuamente. El DR Cloud Native se centra en la copia de seguridad y abarca escenarios empresariales de migración, recuperación y alta disponibilidad para lograr el flujo libre de cargas de trabajo entre nubes, satisfaciendo finalmente las necesidades empresariales del usuario.

Por lo tanto, una plataforma de DR orientada a Cloud Native debe abordar tres capacidades:

**Primera**, centrada en los datos, permitiendo que los datos fluyan libremente entre múltiples nubes. Los datos son el valor central para los usuarios, por lo que independientemente de cómo cambie la infraestructura subyacente, la copia de seguridad de datos siempre será un requisito obligatorio para los usuarios. Cómo resolver la copia de seguridad de datos para diferentes servicios Cloud Native es la base esencial para el flujo de datos.

**Segunda**, aprovechar las capacidades de orquestación Cloud Native para lograr alta automatización y construir escenarios empresariales sobre los datos. Usar capacidades de orquestación automatizada para implementar más aplicaciones basadas en la capa de datos ayuda a los usuarios a lograr más innovación empresarial.

**Tercera**, aprovechar flexiblemente las características de los recursos Cloud Native para reducir el costo total de propiedad. Abordar el problema de la gran inversión en DR tradicional permite a los usuarios pagar verdaderamente los costos bajo demanda, como el agua y la electricidad.
