---
title: "Ingeniería de software en la era de la IA: ya no falta desarrollo, falta calidad"
description: "A partir de observaciones en entrevistas con tres tipos de desarrolladores, este artículo explora cómo la IA está reestructurando la ingeniería de software: el cuello de botella ha pasado de la generación a la calidad, las pruebas evolucionan hacia la ingeniería de calidad y el pensamiento de producto se convierte en la competencia central de cada ingeniero."
date: 2026-06-27T08:00:00+08:00
slug: "ai-era-quality-engineering"
author: Ray Sun
categories:
  - Perspectivas del sector IA
tags:
  - Ingeniería de software
  - Ingeniería de calidad
  - Desarrollo con IA
  - Pruebas
  - Pensamiento de producto
draft: false
---

{{< figure src="/images/ai-era-quality-engineering/hero-quality-gate.webp" alt="Ingeniería de software en la era de la IA: de la generación de código a la garantía de calidad" caption="La IA ha disparado la velocidad de generación, pero el control de calidad se ha convertido en el nuevo cuello de botella. Ese es el verdadero reto de la ingeniería de software en la era de la IA." >}}

Estos últimos días he estado entrevistando candidatos para puestos de QA.

Para ser más preciso: en el sentido tradicional, ya no existen roles diferenciados de frontend, backend, QA o diseño.

El año pasado realizamos una reestructuración interna: todos los puestos relacionados con ingeniería pasaron a llamarse **Software Engineer**, con responsabilidades distintas según el foco de cada persona. A principios de este año fuimos un paso más allá y eliminamos por completo el rol de diseño.

La razón es sencilla.

El modelo anterior de desarrollo de software era:

> **La IA asiste a las personas en su trabajo.**

Hoy creemos que el modelo verdaderamente eficiente ha pasado a ser:

> **La IA es el ejecutor principal. Las personas se encargan de planificar, juzgar y garantizar la calidad.**

Este cambio está ocurriendo mucho más rápido de lo que la mayoría imagina.

<!-- more -->

---

## El problema más difícil ya no es escribir código — es saber si el código es correcto

Los grandes modelos de lenguaje actuales escriben código a una velocidad extraordinaria: pueden generar páginas frontend, esquemas de base de datos e implementaciones de API en minutos. Pero el verdadero problema difícil ha pasado a ser otra cosa:

> **No sabes si lo que escribió está bien.**

La IA puede producir cientos de líneas de código en un minuto, pero dado que su mecanismo de generación es fundamentalmente probabilístico, los errores siempre son posibles:

> **Siempre puede equivocarse.**

El cuello de botella en la ingeniería de software del futuro ya no es la *generación*, sino:

**¿Cómo garantizar la calidad de lo que se ha generado?**

La ingeniería de software tradicional dependía de revisiones de código manuales, pruebas manuales y validación humana. Pero la IA ha elevado la velocidad de desarrollo en un orden de magnitud. Si las pruebas siguen dependiendo de la ejecución manual caso a caso, toda la cadena de desarrollo se convertirá inevitablemente en un cuello de botella.

Por eso cada vez estoy más convencido de una idea:

> **Solo la magia puede vencer a la magia.**

La calidad del software del futuro también debe ser garantizada por la IA. Pero aquí surge fácilmente un malentendido: que con simplemente delegar las pruebas a la IA, todo queda resuelto.

En realidad, la IA sobresale en la *ejecución*, no en el *pensamiento*. Puede generar casos de prueba eficientemente, ejecutar regresiones automáticamente y cubrir un gran número de escenarios, pero no entiende verdaderamente los límites del sistema. No puede plantear proactivamente las preguntas que *deberían* hacerse pero que aún no se han formulado.

Es análogo al desarrollo de producto. La IA puede implementar funcionalidades rápidamente a partir de requisitos, pero la parte verdaderamente difícil es definir qué es un "requisito correcto". Con las pruebas ocurre lo mismo.

El verdadero valor no está en *ejecutar* pruebas — está en hacerse las preguntas correctas:

* ¿Dónde tiene más probabilidades de fallar este sistema?
* ¿Qué escenarios son los que los usuarios tienen más posibilidades de encontrar inesperadamente?
* ¿Qué casos límite podrían colapsar el sistema?
* ¿Qué suposiciones implícitas son en realidad falsas?

Estas preguntas no pueden responderse mediante generación.

La ingeniería de calidad del futuro, por tanto, tiene más que ver con la **capacidad de diseñar las preguntas correctas** que con la ejecución.

La IA se encarga de ejecutar. Las personas definen los problemas, establecen los estándares y construyen el marco de verificación. Quienes son verdaderamente responsables de la calidad ya no ejecutan pruebas ellos mismos — siguen preguntándose:

*¿Qué es lo que aún no hemos probado?*

---

# Tres tipos de desarrolladores que he visto en entrevistas

## Tipo 1: Siguen resistiendo la IA

{{< figure src="/images/ai-era-quality-engineering/engineer-type-1-resistant.webp" alt="Tipo 1: ingenieros que siguen resistiendo la IA" caption="La inercia psicológica los mantiene de espaldas al cambio — aceptar la IA significa desaprender años de hábitos de trabajo acumulados" >}}

Este tipo es el más fácil de identificar.

No están dispuestos a aceptar que la IA ya ha cambiado la ingeniería de software.

Llegan a plantear cosas como:

> ¿Por qué esta entrevista evalúa conocimientos de IA?

¿Por qué no simplemente las habilidades de desarrollo tradicionales?

No están intentando entender el cambio — lo están negando.

Esta resistencia viene de una inercia psicológica.

Aceptar la IA significa que años de métodos de trabajo acumulados deben ser reaprendidos.

Y el cambio siempre es incómodo.

---

## Tipo 2: Conscientes de la IA, pero atascados en la fase de experimentación

{{< figure src="/images/ai-era-quality-engineering/engineer-type-2-dabbling.webp" alt="Tipo 2: ingenieros que experimentan con la IA pero no la integran verdaderamente" caption="Parecen usar la IA, pero nada ha cambiado fundamentalmente. La prueban una vez y vuelven a su forma anterior de trabajar." >}}

Este es el grupo más numeroso.

Son conscientes del cambio y han probado algunas herramientas, pero se quedan en la superficie. Después de experimentar, vuelven a sus flujos de trabajo anteriores. La IA nunca se integra verdaderamente en su proceso. No repiensan cómo trabajan desde una perspectiva de IA. Nunca desarrollan hábitos consistentes a su alrededor.

El resultado: parecen usuarios de IA, pero nada ha cambiado realmente. Hasta que un día descubren que el entorno ha cambiado por completo — y ellos siguen en el mismo lugar. Para entonces, a menudo es demasiado tarde. No los despertó la IA. Los desplazó.

---

## Tipo 3: Ya por delante de la IA

{{< figure src="/images/ai-era-quality-engineering/engineer-type-3-leading.webp" alt="Tipo 3: ingenieros que dirigen la IA con confianza como ejecutor principal" caption="Dirigen la IA como un director de orquesta — entienden los Agentes, los Workflows, el Contexto y los Prompts, y tienen a la IA haciendo trabajo de ingeniería real" >}}

Estas personas han comenzado a entender genuinamente la IA. Conocen conceptos clave como Agentes, Workflows, Contexto y Prompts. Ya han delegado tareas de ingeniería significativas a la IA en su trabajo real.

Pero lo que me sorprendió es que muchos de ellos todavía no se han dado cuenta de que lo que trae la IA no es simplemente una actualización de herramientas — es una reestructuración de los roles a nivel organizacional.

Siempre hago una pregunta en las entrevistas: *Si en el futuro no hay roles de QA, ¿cuál es tu plan?*

La mayoría nunca ha pensado seriamente en esto. Porque lo que está cambiando la IA no es solo cómo trabajamos — es cómo se están redefiniendo los roles organizacionales completos.

---

# Esto ya no es el síndrome de la rana hervida

Mucha gente no empezó a prestar atención seria a la IA hasta este año. Incluso muchos graduados de universidades de élite y poseedores de másteres — personas con experiencia laboral real — solo han comenzado a involucrarse seriamente recientemente. Paradójicamente, es la generación más joven, los que aún están estudiando o recién graduados, quienes han abrazado la IA con mucha más apertura.

Pero la realidad se mueve mucho más rápido de lo que la mayoría espera.

Durante el año pasado, la IA se sentía como agua tibia. La gente pensaba: *está bien, aprenderé gradualmente, todavía hay tiempo.* Pero ahora, entrando en este año, cada vez siento más claramente que el agua ya ha hervido. Muchos cambios de roles no están ocurriendo en el futuro — están ocurriendo ahora mismo. Y cuando la gente finalmente lo comprende, a menudo ya se enfrenta a un panorama competitivo nuevo para el que no estaba preparada.

---

# Un consejo y dos cambios: modelos, calidad y pensamiento de producto

### Un consejo: experimenta primero con los mejores modelos

Doy el mismo consejo a todos los candidatos al final de la entrevista: independientemente de si acabamos trabajando juntos, por favor ve a probar los mejores modelos de IA del mundo.

La razón es simple. El modelo mental de la mayoría de las personas sobre la IA se ha construido a partir de modelos gratuitos, modelos de código abierto o plataformas locales. No es una crítica a esas herramientas — pero si tu primera impresión de la IA vino de un modelo que aún no está totalmente maduro, es muy fácil llegar a una conclusión equivocada:

> *La IA tampoco es para tanto.*

En realidad, la brecha entre los modelos verdaderamente de frontera y los modelos promedio es mucho mayor de lo que la mayoría imagina. Sin haber usado los mejores modelos, es muy difícil entender hacia dónde está llevando realmente la IA a la ingeniería de software.

---

### Cambio 1: Las pruebas se están convirtiendo en ingeniería de calidad

{{< figure src="/images/ai-era-quality-engineering/quality-engineer-white-hat.webp" alt="Ingeniero de calidad: diseñando sistemas de verificación como un hacker de sombrero blanco" caption="Los futuros ingenieros de calidad no ejecutarán pruebas — diseñarán preguntas. Encontrando constantemente dónde el sistema tiene más probabilidades de fallar. Esta habilidad solo se vuelve más valiosa en la era de la IA." >}}

El primer cambio que veo claramente es en las pruebas en sí.

A mucha gente le gusta debatir si los roles de QA desaparecerán. Mi respuesta: las pruebas tradicionales disminuirán, pero la calidad no desaparecerá.

Lo que verdaderamente importará en el futuro no son las Pruebas — es la **Ingeniería de Calidad**. Los ingenieros de QA no solo ejecutarán pruebas; construirán un sistema completo de garantía de calidad mediante habilidades de desarrollo, capacidades de automatización e IA.

La IA escribe el código, la IA genera las pruebas, la IA ejecuta la regresión, la IA valida los resultados. Los ingenieros de calidad definen los estándares de verificación, diseñan la arquitectura de pruebas, construyen la infraestructura de automatización y encuentran lo que la IA pasó por alto.

Son más como hackers de sombrero blanco situados en el lado opuesto del producto — buscando constantemente dónde el sistema tiene más probabilidades de romperse. Esta habilidad se vuelve *más* valiosa en la era de la IA, no menos.

---

### Cambio 2: El pensamiento de producto se convierte en competencia central

El segundo cambio es la creciente importancia del pensamiento de producto.

En el futuro, tanto los desarrolladores como los ingenieros de QA necesitan pensar como personas de producto. No solo escribir código. No solo completar tareas. Sino genuinamente entender el producto desde la perspectiva del usuario — el negocio, la experiencia, por qué las cosas están diseñadas de cierta manera y qué problema realmente necesita resolverse.

La IA será cada vez más capaz en la ejecución. Lo que permanece genuinamente difícil de reemplazar es el juicio, la planificación, la comprensión del producto y el pensamiento sistémico. Estas serán las ventajas competitivas más importantes de cada ingeniero de software en el futuro.

---

## Reflexión final

Estas entrevistas han reforzado algo en lo que cada vez creo más: la IA está reformando la ingeniería de software, pero lo que en última instancia determina el éxito no es la rapidez con la que puede escribir código — es si puede soportar la entrega de productos de alta calidad genuina.

La IA puede aumentar drásticamente el volumen de generación. Pero si la calidad del output es inestable o poco fiable, la velocidad no significa nada.

Especialmente en entornos empresariales, un producto orientado al cliente que carece de rigor hace que la confianza sea imposible de construir — y mucho menos los ingresos.

Por eso el rigor, la estabilidad y la verificabilidad son la primera prioridad.

El problema fundamental de la ingeniería de software del futuro es este: dado que la IA es ahora un participante masivo en la producción, ¿cómo construimos un sistema que realmente garantice la calidad del producto?

Los futuros ingenieros de software no serán solo quienes escriban código. Serán quienes dirijan la IA, diseñen los sistemas de calidad y actúen como guardianes de productos de alta calidad.

Ese es el verdadero núcleo de la ingeniería de software en la era de la IA.
