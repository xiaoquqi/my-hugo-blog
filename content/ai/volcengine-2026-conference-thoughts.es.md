---
title: "Del Modelo al Agent: Reflexiones sobre la próxima etapa de la IA tras la Conferencia FORCE 2026 de Volcengine"
description: "Reflexiones tras asistir a la conferencia FORCE 2026 de Volcengine: la industria de la IA está pasando de la competencia en LLM a la implantación empresarial de Agents."
date: 2026-06-25T08:00:00+08:00
slug: "volcengine-2026-conference-thoughts"
author: Ray Sun
categories:
  - AI行业观察
tags:
  - LLM
  - Agent
  - IA Empresarial
  - Volcengine
  - Multimodal
  - Tendencias IA
draft: false
---

{{< figure src="/images/volcengine-2026/venue-entrance.webp" alt="Plaza de entrada a la Conferencia FORCE 2026 de Volcengine" caption="Plaza de entrada a la Conferencia FORCE'26 Summer de Volcengine: el logo en el suelo y las instalaciones tridimensionales transmiten una presencia imponente" >}}

Durante estos dos días asistí a la Conferencia FORCE 2026 de ByteDance Volcengine.

Más que verla como un evento de lanzamiento de productos, prefiero considerarla una ventana para observar los cambios de etapa en la industria de la IA.

Durante los últimos dos años, la mayor parte de la atención del sector se ha concentrado en los propios grandes modelos: parámetros, benchmarks de capacidad, coste de inferencia, longitud de contexto y capacidades multimodales. Sin embargo, la sensación que me dejó esta conferencia es que el debate está cambiando: de "qué tan poderoso es el modelo" a "cómo entra el modelo en la industria y las empresas".

El cambio de temática entre los dos días también fue muy claro. El primer día giró principalmente en torno a las capacidades de base: LLM, multimodal, AI Infra e infraestructura de cómputo. El segundo día viró claramente hacia el lado aplicado, especialmente la forma en que los Agent se despliegan en entornos empresariales.

Esto también representa la nueva etapa que está entrando la industria: **la capacidad del modelo sigue siendo importante, pero la verdadera pregunta comienza a ser — una vez que tenemos IA, ¿cómo la usamos exactamente?**

<!-- more -->

{{< figure src="/images/volcengine-2026/volcengine-trends.webp" alt="Valoración de tendencias clave de la conferencia: unificación LLM, avance multimodal, madurez del Agent empresarial" caption="Diapositiva de tendencias clave del primer día: tres direcciones que representan el consenso actual de la industria" >}}

## I. La competencia en modelos continuará, pero lo multimodal podría convertirse en el punto de ruptura

La competencia entre grandes modelos no va a detenerse; eso es una certeza.

Especialmente en escenarios como Coding Agent, la esencia sigue siendo una competencia de capacidades de modelos lingüísticos: comprensión de requisitos complejos, manejo de contextos largos, razonamiento en múltiples pasos y ejecución estable. Desde la experiencia de uso real, los modelos nacionales chinos aún están en fase de recuperación en esta dirección; los escenarios de desarrollo mainstream siguen dominados por OpenAI y Claude. La razón es directa: cuando el Coding Agent llega al límite, lo que cuenta es la capacidad del modelo base.

Pero otra dirección está cobrando cada vez más importancia: **lo multimodal, especialmente la generación de imágenes y vídeo**.

El Seedance 2.5 que Volcengine presentó esta vez me causó una impresión profunda. La generación de vídeo no es solo un problema de modelo, sino también un problema de datos. El ecosistema de vídeo corto de ByteDance, su sistema de creadores y el ciclo de retroalimentación constituyen en esencia una ventaja de datos muy sólida.

{{< figure src="/images/volcengine-2026/seedance-25.webp" alt="Modelo de generación de vídeo Seedance 2.5 de Doubao" caption="Presentación en vivo de Seedance 2.5: rompe los límites narrativos, amplía la referencia multimodal completa, edición vídeo plano a plano y abraza a los creadores globales" >}}

{{< figure src="/images/volcengine-2026/seedance-demo.webp" alt="Demostración en la sala principal del cortometraje generado con Seedance" caption="Demostración en la sala principal del cortometraje generado con Seedance — impactante sobre el fondo FORCE del escenario: una exhibición concentrada de la capacidad de generación de vídeo en China" >}}

Así, el panorama futuro podría ser: los modelos de lenguaje continúan compitiendo, pero lo multimodal —especialmente la dirección vídeo— tiene la oportunidad de convertirse en el punto de ruptura de la IA china.

## II. El Agent entra en la empresa: el mayor reto no es la IA, sino la organización

{{< figure src="/images/volcengine-2026/agent-types.webp" alt="Tres tipos de Agent empresarial: productivo, de apoyo a la decisión y de ejecución de procesos" caption="División clara de las tres formas de Agent empresarial: el productivo se ocupa de los entregables, el de apoyo a la decisión respalda el juicio, y el de ejecución de procesos impulsa el cierre del ciclo" >}}

Si los modelos resuelven el problema de la capacidad, los Agent resuelven el problema del modo de uso. Pero desde la perspectiva empresarial, todavía no existe una respuesta estándar.

Usar IA de forma personal y usarla en una empresa son dos cosas completamente diferentes.

Para el individuo, el objetivo es simple: aumentar la eficiencia. Pero para una empresa, la IA debe integrarse en la estructura organizativa, y toda organización implica por naturaleza: permisos, procesos, responsabilidades, colaboración, seguridad y auditoría. Por eso, la complejidad de muchos sistemas de IA empresarial no es complejidad técnica en esencia, sino **complejidad organizativa**.

Volviendo a los primeros principios, muchos procesos no son estrictamente necesarios para completar una tarea —pero mientras la estructura empresarial no cambie, esos procesos seguirán existiendo. Por lo tanto, el problema central al que se enfrentan los Agent empresariales no es "si pueden hacerlo", sino: **cómo entrar en la organización y transformar gradualmente la forma de trabajar**.

{{< figure src="/images/volcengine-2026/digital-employee.webp" alt="Construir un sistema de gestión de empleados digitales" caption="«Construir un sistema de gestión de empleados digitales» — visible, controlable y medible, con diseño en capas para cuatro perfiles: gestores, personal de TI, personal de operaciones y personal de negocio" >}}

Por ahora, el escenario de despliegue más consolidado es el **ciclo de vida completo del desarrollo de software**. Desde el análisis de requisitos, diseño de producto, arquitectura, implementación de código, revisión de código, verificación de pruebas, corrección de errores, hasta la documentación y la entrega, la IA está penetrando en toda la cadena de desarrollo. No sustituye un puesto concreto, sino que está reconfigurando el modelo de eficiencia de todo el sistema de desarrollo.

Sin embargo, en procesos de negocio más complejos como ventas, operaciones o cadena de suministro, la penetración de la IA sigue en una etapa temprana — el problema ya ha pasado de la capacidad tecnológica a cómo la organización usa la IA. Así que durante un tiempo seguiremos viendo que el Agent empresarial permanece en una fase de exploración con múltiples enfoques en competencia.

## III. Observaciones en el área de exposición: IA + hardware amplía fronteras, pero el soporte definitivo aún no está definido

{{< figure src="/images/volcengine-2026/ai-infra-booth.webp" alt="Stand de infraestructura de IA: el LLM Doubao supera los 180 billones de Tokens diarios" caption="Dato del área de exposición: a junio de 2026, el LLM Doubao supera los 180 billones de Tokens de invocación diaria media — la escala de la infraestructura de cómputo ya es considerable" >}}

En el área de exposición, lo que más atención captaba eran habitualmente los productos que combinan IA con hardware.

Por ejemplo, algunos peluches con IA. A primera vista parecen "juguetes que hablan", pero el cambio de fondo es que el LLM transforma la interacción de orientada por reglas a orientada por comprensión, redefiniendo los límites de la capacidad.

{{< figure src="/images/volcengine-2026/ai-plush-toy.webp" alt="Peluche con IA en la exposición: bola inteligente con ojos luminosos" caption="El peluche con IA del área de exposición — detrás de los ojos brillantes hay una capacidad de comprensión impulsada por LLM: la carcasa de hardware no ha cambiado, pero la esencia de la interacción sí" >}}

Otro que me causó bastante impresión fue Tuya Smart y plataformas similares. Se asemejan más a una capa intermedia de capacidad para AIoT: conectan dispositivos, encapsulan capacidades de control e integran capacidades de IA en ellos para que los fabricantes de hardware puedan construir productos inteligentes rápidamente. Esto encaja muy bien con el ecosistema manufacturero chino — antes faltaba la "inteligencia", y ahora la IA está cubriendo esa capa.

{{< figure src="/images/volcengine-2026/ai-hardware-booth.webp" alt="Hardware inteligente con IA: lámpara de escritorio con proyección VR interactiva" caption="Producto de hardware con IA en el área de exposición: lámpara de escritorio protectora de la vista con interacción por proyección VR, un ejemplo típico de cómo la capacidad LLM penetra en el hardware de consumo" >}}

Pero el problema es: **el soporte definitivo de la IA todavía no ha aparecido**.

Estos productos son muy llamativos, pero si se convertirán en el próximo punto de entrada estable todavía no se puede determinar. Las aplicaciones puramente de software suelen tener fosos defensivos débiles; en cuanto cambien las capacidades del modelo, la forma de las aplicaciones puede redefinirse por completo. A largo plazo, las verdaderas barreras pueden provenir de: datos, escenarios, puntos de entrada de interacción y nuevas formas de combinación software-hardware.

## IV. ArkClaw y la forma del producto de IA: la dirección es válida, pero aún en exploración

{{< figure src="/images/volcengine-2026/agentkit-arch.webp" alt="Arquitectura completa de AgentKit: identidad, Policy, registro, runtime, sandbox, evaluación, observabilidad, Memory, Knowledge" caption="AgentKit como infraestructura de Agent empresarial, abarca la capa de ejecución completa desde la autenticación de identidad hasta la base de conocimiento" >}}

En esta conferencia también probé ArkClaw. La impresión general fue: **la dirección es correcta, pero la forma del producto aún no ha convergido**.

ArkClaw en esencia está construyendo un Agent Workspace en la nube para transformar al Agent de "herramienta de conversación" en un sistema con entorno de ejecución, invocación de herramientas y capacidades de ejecución de tareas. Esta dirección la valido, y la razón es muy práctica:

Al promover la IA dentro de una empresa, la primera resistencia suele no ser el modelo, sino el entorno — no saber instalar herramientas, no saber configurar el entorno, no saber gestionar las Keys. ArkClaw reduce esta barrera hasta cierto punto.

Pero al mismo tiempo introduce otro problema: el entorno se simplifica, pero los datos empiezan a moverse al exterior. Esto entra inmediatamente en el terreno de la seguridad, los permisos y el cumplimiento normativo empresarial. Así que la contradicción central del Agent empresarial sigue siendo: no solo tiene que "poder usarse", sino **"poder usarse con confianza"**.

Desde el punto de vista del producto, dentro del ecosistema de ByteDance coexisten Coze, ArkClaw y otras líneas. Desde fuera puede parecer que hay cierta superposición, pero en realidad esto es la forma típica en que las grandes empresas exploran: en una etapa sin respuesta estándar, permiten que distintos equipos prueben y fallen simultáneamente. La esencia es responder a la misma pregunta — **¿cuál será el punto de entrada de trabajo de la IA en el futuro?** ¿Una plataforma de desarrollo, un Coding Agent, un empleado digital o un nuevo punto de entrada del sistema? Por ahora no hay respuesta.

Al mismo tiempo, las plataformas cloud actuales todavía no han completado la transición de Cloud Native a AI Native. Incluso dentro de una plataforma unificada, los desarrolladores siguen teniendo que gestionar Keys, Endpoints y configuración de recursos — sigue siendo en esencia "personas ensamblando sistemas". La dirección AI Native debería ser: **el usuario solo expresa el objetivo, y el sistema completa automáticamente la combinación de recursos y la ejecución**.

## V. Valoración de tendencias: de la capacidad del modelo a la estructura del sistema

Si comprimimos las observaciones de esta conferencia en varios juicios:

**La competencia entre LLM seguirá siendo prolongada**, especialmente en la dirección Coding Agent, donde la capacidad del modelo de lenguaje base sigue siendo el cuello de botella central. Pero lo multimodal está convirtiéndose en otro camino clave, y la generación de vídeo e imagen puede convertirse en la dirección de ruptura más ventajosa para la IA china.

**El despliegue de la IA en las empresas ya ha comenzado, pero el verdadero reto no está en la tecnología, sino en la organización**. El valor más consolidado actualmente proviene de la mejora de eficiencia en el ciclo de vida completo del desarrollo, pero una vez que penetra en los procesos de negocio, el problema se transforma en cómo la organización usa la IA.

**En qué forma existirá finalmente la IA está aún por determinar**. Aplicaciones, plataformas y hardware siguen en fase de exploración, sin convergencia. Las aplicaciones puramente de software son fácilmente absorbidas por la capacidad del modelo, mientras que los nuevos puntos de entrada de interacción siguen evolucionando.

Por tanto, el estado más realista es:

**La IA está penetrando desde escenarios parciales, no formando un estado final de una sola vez.** Primero cambia proceso a proceso concreto, luego reconfigura gradualmente la estructura del sistema. Cuando estos cambios se acumulen a escala suficiente, la nueva forma surgirá de manera natural.

---

*Este artículo es un registro inmediato tras la conferencia; las ideas pueden no estar completamente desarrolladas. Bienvenida la discusión.*
