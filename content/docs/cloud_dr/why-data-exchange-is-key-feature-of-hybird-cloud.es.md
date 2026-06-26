---
title: "¿Por Qué el Flujo de Datos Es la Capacidad Central de la Nube Híbrida?"
date: 2022-07-20T08:29:00+08:00
slug: "why-data-exchange-is-key-feature-of-hybird-cloud"
author: Ray Sun
tags:
  - Análisis de Tendencias
  - Computación en la Nube
  - cloud
categories:
  - Análisis de Tendencias
draft: false
---

Desde la entrada en la década de 2010, la computación en la nube ha ido reemplazando gradualmente a la infraestructura tradicional para convertirse en el nuevo cimiento de los sistemas de información. En octubre de 2020 redacté un artículo titulado *Reflexiones sobre Migración y Recuperación ante Desastres en el Contexto Cloud-Nativo* ([https://sunqi.site/posts/cloud-migration-dr-on-cloud-native/](https://sunqi.site/posts/cloud-migration-dr-on-cloud-native/)), en el que analicé en detalle cómo cambiaría la protección de datos — crítica para los usuarios — bajo este nuevo paradigma de infraestructura. El presente artículo parte de esa base y, incorporando dos años de práctica sectorial y recientes acontecimientos de actualidad en China, profundiza en el análisis y la síntesis.

## Plataformas Cloud — ¿Estatales o Privadas?

Esta misma semana (12 de julio de 2022), una noticia de gran calado sacudió el mundo de la computación en la nube. La cuenta oficial de WeChat "Xinhua de Activos Estatales" publicó el comunicado: *La SASAC celebra una reunión de trabajo sobre la profundización de la integración especializada entre empresas centrales*.

![2022-07-20-08-31-13](/images/2022-07-20-08-31-13.png)

El contenido relacionado con la computación en la nube captó especial atención:

> La reunión señaló que en los últimos años las empresas centrales han **implementado una integración especializada con mayor cobertura sectorial, participación más amplia y mayor grado de refinamiento**, obteniendo resultados notables en el servicio a las estrategias nacionales, la optimización del tejido económico estatal y la promoción del desarrollo de alta calidad.

> **China Telecom ha incorporado a varios inversores estratégicos de empresas centrales para construir una empresa de nube nacional, coordinando la innovación tecnológica, la construcción de infraestructura y el despliegue del sistema de seguridad para acelerar la construcción de un ecosistema tecnológico cloud de creación propia.**

Las medidas concretas de China Telecom se describieron así:

> China Telecom, centrada en su estrategia de transformación cloud y transición digital y apoyándose en la integración especializada como palanca, está construyendo un clúster de negocio de "una nube, dos alas". En torno al desarrollo de la sociedad digital, **ha incorporado a inversores estratégicos de empresas centrales como China Electronics, CETC, China Chengtong y China Reform para constituir la empresa de capital diversificado Tianyi Cloud Technology Co., Ltd.**, impulsando activamente la consolidación de los recursos de computación en la nube entre empresas centrales. Mediante la profundización de la I+D conjunta con empresas centrales como China Electronics y universidades de prestigio como la Universidad Tsinghua, está construyendo un ecosistema tecnológico cloud completo y de desarrollo autónomo. Consolidando recursos internos, Tianyi Cloud cuenta con filiales en las 31 provincias y ha establecido un sistema integrado de operaciones cloud-red. Actualmente, Tianyi Cloud es la mayor nube de operador de telecomunicaciones del mundo y la mayor nube híbrida de China, y su marco como nube nacional está esencialmente consolidado.

Según las bases de datos de información corporativa, Tianyi Cloud Technology Co., Ltd. sigue siendo propiedad al 100% de China Telecom — el cambio de titularidad aún no se ha formalizado — pero dado que la dirección estratégica está clara, todo se espera que se acelere.

![2022-07-20-08-31-37](/images/2022-07-20-08-31-37.png)

La designación de la "nube nacional" también parece zanjar los rumores que el año pasado circularon ampliamente sobre la "nube de activos estatales". El 12 de agosto de 2021, el *Plan de implementación para acelerar la migración de empresas estatales a la nube y mejorar el sistema de nube de activos estatales* de la SASAC de Tianjin, en la Parte 3, Tareas Clave, Punto 2, establecía explícitamente:

> Los sistemas de información que las empresas ya hayan desplegado en plataformas de nube pública de terceros (como "Huawei Cloud", "Alibaba Cloud", "Tencent Cloud", "Wo Cloud", "Tianyi Cloud", "China Mobile Cloud", etc.) deberán migrarse íntegramente a la nube de activos estatales en un plazo de 2 meses desde el vencimiento del contrato de arrendamiento, con una fecha límite absoluta del 30 de septiembre de 2022. A partir de hoy, las empresas no podrán suscribir nuevos contratos ni renovar los existentes de alquiler de recursos cloud con plataformas de nube pública de terceros.

Con menos de dos meses para el 30 de septiembre, la situación real de la ejecución de la política sigue siendo incierta. ¿Afectará la designación formal de la nube nacional al cumplimiento de los plazos anteriores? ¿Podría producirse una migración redundante? Desde fuera, los detalles son desconocidos.

Uno de los factores desencadenantes de todos estos cambios fue un incidente de principios de 2021, cuando una importante empresa de internet completó en silencio una cotización exterior no autorizada, proporcionando acceso a grandes volúmenes de datos civiles sensibles. El 10 de junio del mismo año, la 29ª sesión del Comité Permanente de la 13ª Asamblea Popular Nacional aprobó la *Ley de Seguridad de Datos de la República Popular China* ([http://www.npc.gov.cn/npc/c30834/202106/7c9af12f51334a73b56d7938f99a788a.shtml](http://www.npc.gov.cn/npc/c30834/202106/7c9af12f51334a73b56d7938f99a788a.shtml)), en la que se establece:

> Artículo 14: El Estado implementará la estrategia de big data, promoverá la construcción de infraestructura de datos y alentará y apoyará las aplicaciones innovadoras de los datos en diversos sectores e industrias. Los gobiernos a nivel provincial o superior deberán incorporar el desarrollo de la economía digital en sus planes de desarrollo económico y social y, cuando sea necesario, formular planes de desarrollo de la economía digital.

Las empresas estatales son pilares reconocidos de la economía nacional y un campo de batalla decisivo para todos los proveedores cloud. La designación de la nube nacional parece zanjar la incertidumbre sobre si la nube en China será estatal o privada, y el cómputo en la nube chino inevitablemente trazará un camino con características distintivas propias. ¿Pero es este el punto final del cómputo en la nube chino? Claramente no — las políticas siempre van por detrás de la tecnología, y la forma final seguirá evolucionando. Para las empresas usuarias, lo único constante es el cambio. Para afrontarlo, el más importante de los nuevos "activos estatales" — los *datos* — debe fluir libremente, permitiendo a los usuarios abrazar mejor la incertidumbre del futuro.

## Nube Híbrida — Proteger la Inversión Existente, Abrazar el Cambio

Frente al cambio constante, la nube híbrida es claramente una vía adecuada para el desarrollo de China. Desde una perspectiva de crecimiento, la última década de auge del cómputo en la nube ha dado lugar a una proliferación de proveedores de nube pública y privada — por estimaciones conservadoras, hay al menos 20 nubes públicas en operación, y las marcas de nube privada son aún más numerosas. Desde la perspectiva de proteger la inversión empresarial existente, las empresas no pueden abandonar a la ligera sus inversiones previas en cómputo en la nube e infraestructura, lo que convierte a la nube híbrida en la infraestructura integral que sirve tanto a los intereses empresariales como a la estrategia nacional.

Desde el punto de vista técnico, ninguna plataforma base puede ser reemplazada de la noche a la mañana; la construcción de sistemas debe seguir sus propias leyes y avanzar de forma gradual. Como se indicó antes, el flujo de datos permite a los usuarios gestionar los cambios en la infraestructura cloud con mayor agilidad, y el flujo de datos entre distintas nubes en un entorno híbrido es la forma más eficaz de evitar la formación de nuevos "silos de datos" en la era cloud.

![2022-07-20-08-31-54](/images/2022-07-20-08-31-54.png)

## La Evolución de la Gestión de la Nube Híbrida — De Plataforma a Conjunto de Herramientas

En 2018, Gartner mencionó en un artículo ([https://blogs.gartner.com/marco-meinardi/2018/01/22/upcoming-research-cloud-management-platforms/](https://blogs.gartner.com/marco-meinardi/2018/01/22/upcoming-research-cloud-management-platforms/)) los diez módulos de las Plataformas de Gestión Cloud (Cloud Management Platforms). Entre ellos, Cloud Migration and DR existía como módulo independiente — uno de los diez con mayor vinculación al flujo de datos de los usuarios. Sin embargo, en la práctica, dado que los volúmenes de datos en la nube eran pequeños y la necesidad de flujo de datos no era acuciante en los primeros tiempos, muy pocas plataformas de gestión cloud pudieron ofrecer ese módulo de servicio especializado. Solo un puñado de usuarios con visión de futuro identificaron esa necesidad latente y actuaron en consecuencia — por ejemplo, el artículo *Servicios de Migración Cloud-Nativa en el Ecosistema de la Plataforma Cloud Financiera Híbrida de Haitong Securities*, publicado en *Trading Technology Frontiers*, número 40 de la Bolsa de Shanghai (septiembre de 2020), que documentó esas mejores prácticas y sirvió de referencia para otras firmas de corretaje que exploran el flujo de datos en nube híbrida.

![2022-07-20-08-32-06](/images/2022-07-20-08-32-06.png)

¿Por qué un servicio tan importante no puede ofrecerse directamente desde las plataformas de gestión cloud? A mi juicio, hay dos razones: volumen de datos y barrera técnica. En cuanto al volumen de datos, como se señaló, los primeros entornos cloud tenían datos reducidos y el "esfuerzo manual" era suficiente para el flujo de datos. Pero a medida que crecía el número de aplicaciones y el volumen de datos experimentaba un crecimiento explosivo, el tradicional "añadir personas" ya no podía satisfacer las necesidades de flujo de datos como servicio para los usuarios cloud. La barrera técnica, sin embargo, es el mayor obstáculo que impide a las plataformas de gestión cloud ofrecer estos servicios. La tecnología de Cloud Migration y DR se nutre en parte de técnicas de recuperación ante desastres tradicionales y en parte de tecnologías de recursos y orquestación cloud-nativos — es una integración e innovación técnica interdisciplinar que no es menos desafiante que construir una plataforma de gestión cloud en sí misma. La presión de entrega de proyectos deja poco margen a los proveedores de plataformas de gestión cloud para innovar adicionalmente.

Esto quedó confirmado en el informe de Gartner de abril de 2022, *Market Guide for Cloud Management Tooling* ([https://www.gartner.com/doc/reprints?id=1-29PBZLL4&ct=220413&st=sb&elqTrackId=adedc2cde73f4497b990cb119e448714&elqaid=7083&elqat=2](https://www.gartner.com/doc/reprints?id=1-29PBZLL4&ct=220413&st=sb&elqTrackId=adedc2cde73f4497b990cb119e448714&elqaid=7083&elqat=2)). Un cambio muy notable es la terminología: lo que llamábamos habitualmente "Cloud Management Platform" pasa a redefinirse en el informe como "Cloud Management Tooling" — entendible simplemente como conjunto de herramientas de gestión cloud. Gartner considera que, a medida que los servicios de gestión cloud maduran, los proveedores especializados se centran en abstraer los servicios en herramientas automatizadas. En el informe encontramos que las herramientas de gestión cloud especializadas de terceros y las plataformas de gestión cloud tradicionales aparecen como módulos paralelos, proporcionando conjuntamente capacidades de gestión multicloud a los MSP. Gartner también añadió Backup al módulo de Cloud Migration and DR, unificando así las aplicaciones por escenarios que nosotros definimos como "flujo de datos."

![2022-07-20-08-32-18](/images/2022-07-20-08-32-18.png)

## ¿Qué Es el Flujo de Datos? — El Fundamento de la Migración Cloud y el DR Cloud en Sentido Amplio

¿Es la migración cloud un negocio puntual? Muchas personas me lo han preguntado — socios, inversores y otros. Permítanme expresar mi punto de vista directamente: la "migración cloud", según su propósito, puede dividirse en migración cloud en sentido estricto y en sentido amplio. La migración cloud en sentido estricto se refiere a actividades basadas en proyectos: subir a la nube, bajar de la nube o cambiar de nube. La migración cloud en sentido amplio, por el contrario, es un modo de aplicación del flujo de datos, cuyos escenarios derivados incluyen DR cloud, backup, transferencia de datos entre zonas geográficas y más. Desde la perspectiva de las tendencias de desarrollo de la nube híbrida, la migración cloud no es en absoluto una necesidad puntual — es uno de los servicios estándar de la nube.

### Migración Cloud en Sentido Estricto — Escenarios de Aplicación Basados en Proyectos

Comenzando por la migración cloud en sentido estricto: durante el pico de migración (antes de 2010), la migración cloud era la mejor forma de resolver el problema de "la autopista sin coches" — estimulando rápidamente la expansión de capacidad en la infraestructura subyacente para compensar las pérdidas iniciales de los proveedores en sus proyectos.

![2022-07-20-08-32-32](/images/2022-07-20-08-32-32.png)

Con el paso del tiempo, sin embargo, surgieron diversas necesidades de "cambio de nube". A continuación se enumeran algunos escenarios habituales:

**Escenario 1: La plataforma original queda sin mantenimiento.** Las primeras soluciones y proveedores de plataformas cloud eran inmaduros, con muchos productos pioneros en terreno desconocido. Con el tiempo, por diversas razones, las plataformas quedaban sin mantenimiento mientras el negocio continuaba expuesto, lo que obligaba a cambiar de nube para trasladar las cargas de trabajo.

**Escenario 2: Competencia entre proveedores.** Este escenario tiene poco que ver con la tecnología y más con intereses comerciales. Dado que captar nuevos clientes desde entornos locales tradicionales es costoso, los proveedores apuntan a los clientes en nube de sus competidores. También se da el caso de usuarios que querían experimentar con soluciones open source "gratuitas", pero que tras la prueba descubrieron que perdían el control o que el rendimiento no cubría sus necesidades, viéndose obligados a pasarse a soluciones comerciales — una dinámica observable tanto en plataformas cloud como en almacenamiento cloud subyacente.

**Escenario 3: La plataforma no puede actualizarse a sí misma.** El ejemplo más típico es la actualización de versiones cruzadas de OpenStack. Aunque OpenStack incorporó eventualmente capacidades de actualización, las versiones personalizadas de los proveedores contienen grandes cantidades de funcionalidad que no puede contribuirse al upstream, haciendo las actualizaciones prácticamente imposibles. Cuando los usuarios quieren migrar a una versión más reciente, solo pueden hacerlo mediante migración cloud — reemplazando la plataforma antigua y reintegrando el hardware original en el pool de recursos. Este problema no es exclusivo de OpenStack; algunas plataformas cloud comerciales enfrentan el mismo desafío.

Bajar de la nube es, en relación a subir a la nube, una forma de cambio de nube — pero se refiere específicamente al movimiento de nube pública a nube privada, por lo que merece consideración aparte. La nube pública ha ayudado genuinamente a proveedores con fuertes requisitos temporales a acelerar la innovación y aprovechar oportunidades, pero a medida que las empresas maduran, las presiones financieras inevitablemente empujan el crecimiento desordenado hacia la gestión de precisión. En ese momento, las empresas deben valorar la economía de la nube pública frente a la infraestructura propia.

En sentido estricto, la migración cloud se asemeja a una acción pasiva — tan solo un eslabón de una solución, y en ese contexto es efectivamente no repetible.

### Migración Cloud en Sentido Amplio — Escenarios de Aplicación Basados en el Flujo de Datos

La migración cloud en sentido amplio es un servicio cloud-nativo centrado en el flujo de datos que proporciona orquestación de datos a nivel de inquilino. Tal como define Gartner: en un entorno de nube híbrida, las capacidades de flujo de datos permiten que los datos se muevan entre plataformas, proporcionando una gama de escenarios de aplicación en capas superiores que incluyen — entre otros — servicios de migración, DR y backup.

![2022-07-20-08-32-45](/images/2022-07-20-08-32-45.png)

En los entornos físicos tradicionales, el flujo de datos era teóricamente posible pero prácticamente poco significativo — las plataformas eran relativamente homogéneas y las aplicaciones de capa superior basadas en datos eran escasas. Pero en la era cloud-nativa, la riqueza de servicios crea las condiciones para la innovación empresarial impulsada por datos.

Las capacidades de flujo de datos deben hacer un uso racional de los recursos de almacenamiento cloud-nativo y exponer escenarios de capa superior basados en orquestación de cómputo o de almacenamiento. Tomando la capa de orquestación de cómputo como ejemplo: los recursos pueden restaurarse en cualquier plataforma, soportando casos de uso diversos como migración, DR y simulación. La capa de orquestación de almacenamiento, por su parte, proporciona un canal para la innovación basada en datos, conectando a varias interfaces de almacenamiento para suministrar fuentes de datos a contenedores, plataformas de big data y plataformas de IA en capas superiores.

Como señalé en un artículo anterior, debido a las características de la arquitectura cloud-nativa, los datos están distribuidos entre los distintos servicios cloud-nativos. Una plataforma de flujo de datos debe por tanto ser compatible con servicios cloud-nativos diversos — hosts, RDS, contenedores, etc. — al tiempo que aprovecha inteligentemente las propiedades del almacenamiento cloud-nativo para lograr el coste óptimo.

![2022-07-20-08-32-56](/images/2022-07-20-08-32-56.png)

## Conclusión

Los "datos" son un nuevo activo empresarial crítico. Cómo extraer innovación e incluso generar beneficio a partir de los datos en la era cloud es una cuestión que las empresas deben reflexionar y explorar como parte de su transformación digital. Las capacidades de flujo de datos permiten que los datos empresariales circulen dentro de la nube híbrida, proporcionando los cimientos y la garantía para la innovación posterior. Desde la perspectiva del desarrollo de productos, existimos en una era de rápido cambio tecnológico, y el desarrollo del cómputo en la nube está creando nuevas oportunidades para una generación de productos de capa de infraestructura. La clave del éxito del producto reside en aprovechar racionalmente las propiedades comunes de los recursos cloud-nativos, combinándolas con las propias fortalezas técnicas en los dominios tradicionales. Este artículo ha utilizado principalmente la trayectoria del desarrollo del cómputo en la nube en China para pronosticar e interpretar cómo se aplicarán los datos en entornos de nube híbrida. Apoyándose en la evolución de la definición de Gartner sobre las plataformas de gestión cloud, propone el concepto de migración cloud en sentido amplio y llega a la conclusión de que el flujo de datos es la capacidad central de la nube híbrida.
