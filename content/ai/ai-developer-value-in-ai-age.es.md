---
title: Cuando la IA escribe el 99% del código, ¿qué valor le queda al desarrollador?
author: Ray Sun
date: 2026-06-14T08:00:00+08:00
categories:
  - Gestión de equipos de IA
tags:
  - AI
  - Eficiencia de ingeniería
  - Gestión de equipos
---

Durante el último año he estado reconsiderando mis criterios para evaluar a los equipos técnicos.

Este cambio no proviene de ningún artículo ni de ningún informe del sector, sino de la práctica de nuestro propio equipo: a medida que las herramientas de programación con AI se vuelven cada vez más potentes, los límites del valor de muchos puestos están siendo redefinidos.

Al principio, yo también usaba la AI solo como herramienta de apoyo: para ayudar a escribir código, buscar información, organizar documentación y explicar errores. En esa etapa, era más como un motor de búsqueda más inteligente.

Pero desde que apareció el modo Agent de Cursor, noté claramente que las cosas habían cambiado.

<!-- more -->

## De Ask a Agent: el cambio va más allá de la eficiencia

Aproximadamente en abril de 2025, me suscribí formalmente a Cursor. Antes también había estado usando herramientas de AI, pero más en modo de prueba gratuita y experimentación dispersa, principalmente para resolver problemas concretos. Nunca me había imaginado que escribir código se convertiría en el primer caso de éxito que la AI resuelve de manera casi perfecta.

Lo que realmente me hizo darme cuenta de que el cambio se estaba acelerando fue la aparición del modo Agent.

Del modo Ask al modo Agent, y en el futuro quizás ni siquiera hará falta el Ask: las personas solo necesitan dar objetivos, restricciones y juicios; la AI lee el código, modifica el código, ejecuta pruebas y corrige errores por su cuenta.

Para la industria del software, esto no es una simple mejora de eficiencia, sino un cambio en la posición que ocupa el técnico dentro de la cadena de desarrollo.

## Los primeros afectados: diseño y frontend

En nuestro equipo, los primeros en ser impactados fueron diseño y frontend.

Antes, para hacer una página se necesitaba que el diseñador hiciera los mockups, el frontend los implementara y luego hubiera rondas de ajustes. Pero cuando las herramientas de AI pueden generar rápidamente prototipos de páginas, layouts y estilos, esa cadena empezó a flojear.

El año pasado intentamos que nuestro diseñador hiciera la transición, esperando que pudiera adaptarse a las nuevas formas de trabajo. Al final no lo consiguió. A principios de este año, eliminamos directamente ese puesto.

Lo interesante es que después de eliminar el puesto no apareció la brecha de diseño que temíamos. Al contrario, otros compañeros comenzaron a usar activamente herramientas de AI para hacer páginas, ajustar estilos y modificar interacciones, y el resultado no era malo en absoluto.

Esto me impactó bastante.

Demuestra algo importante: cuando la capacidad de una herramienta es suficientemente fuerte, si un puesto solo depende de "saber usar una herramienta especializada", su valor cae rápidamente. Lo que realmente permanece es el juicio estético, la comprensión del producto y la capacidad de controlar los resultados.

Después del diseño, el siguiente afectado de forma notable fue el frontend.

Ahora las páginas de administración, formularios, tablas, páginas de detalle, páginas de configuración y otras páginas estandarizadas ya pueden generarse rápidamente con AI. Si el frontend solo se dedica a conectar APIs, escribir páginas y ajustar estilos, su reemplazabilidad será cada vez mayor.

Por eso últimamente estamos intentando que los compañeros de frontend avancen hacia una cadena de desarrollo de producto más completa: no solo hacer páginas, sino participar en la comprensión de requisitos, el diseño del producto, el modelado de datos, el mapeo de flujos y la evaluación de riesgos de pruebas.

Pero en este proceso descubrimos dos problemas evidentes.

## Dos debilidades estructurales del frontend

**El primer problema es que muchos compañeros de frontend tienen una base débil en estructuras de datos y modelado.**

No es de extrañar. El frontend lleva mucho tiempo enfrentando APIs ya diseñadas por el backend: ve qué devuelve la interfaz, qué muestra la página, qué interfaz se llama cuando el usuario hace clic.

Pero la parte verdaderamente difícil de un sistema no suele ser cómo dibujar la página, sino:

- Cuáles son los objetos del negocio;
- Cuál es la relación entre los objetos;
- Cómo cambia el estado;
- Qué datos necesitan mantener historial;
- Qué operaciones requieren auditoría;
- Qué excepciones deben manejarse;
- Qué flujos no pueden cubrirse simplemente.

Estas cosas no se pueden completar automáticamente desde la capa UI.

**El segundo problema es que muchos compañeros de frontend tienen una comprensión muy débil del negocio, e incluso no tienen el hábito de comprenderlo activamente.**

Esto me preocupa aún más.

El frontend trabaja con "cosas visibles", y en teoría debería estar más cerca de los usuarios y del producto. Pero la realidad es que mucha gente solo saca la página adelante sin haber comprendido realmente la lógica de negocio que hay detrás.

Por ejemplo, nosotros hacemos software de migración a la nube y recuperación ante desastres. Cuando quisimos que los compañeros de frontend participaran en una nueva dirección de recuperación ante desastres, descubrí que su comprensión del producto existente no era suficiente. Saben qué botones hay en la página, saben qué campos devuelve la interfaz, pero no necesariamente entienden:

- Por qué los clientes necesitan migrar, por qué necesitan recuperación ante desastres;
- Cuál es la diferencia esencial entre recuperación ante desastres y copia de seguridad;
- Qué problemas resuelven respectivamente el simulacro, la toma de control y el retorno;
- Qué significan RPO y RTO para el cliente;
- Qué acciones son de alto riesgo para el cliente.

Es decir, trabajan todos los días con páginas visibles, pero no han entendido realmente por qué existen esas páginas.

También intentamos que analizaran productos de la competencia, para entender cómo hacen sus productos, cómo organizan sus páginas, cómo expresan el negocio. Pero esto también resultó difícil para ellos: por un lado, les falta base técnica de fondo; por otro, les falta motivación propia.

Mucha gente está acostumbrada a esperar los requisitos, esperar el diseño, esperar la interfaz, y luego implementar la página. Pedirles que investiguen activamente la competencia, comprendan el negocio, descompongan la lógica del producto y deduzcan la estructura de datos les resulta muy incómodo.

Esa es la mayor debilidad estructural de la transición del frontend en la era AI.

Antes la ventaja del frontend era "estar más cerca del usuario". Pero si un frontend solo está cerca de la página y no cerca del negocio, esa ventaja desaparecerá rápidamente con la llegada de la AI.

## El proceso de entrevistas también tiene que cambiar

Estos cambios han afectado directamente nuestra forma de contratar últimamente.

Antes hacíamos que los candidatos resolvieran ejercicios de desarrollo: escribir código en el momento y ver si funcionaba. Pero ahora siento cada vez más que ese método pierde poder discriminatorio: escribir código es cada vez más fácil con asistencia de AI, un candidato puede llegar con AI hasta hacerlo funcionar, pero eso no significa que haya entendido realmente el sistema.

Por eso cambiamos las preguntas de entrevista a **preguntas de diseño de sistemas**.

El enunciado en sí no es complicado, normalmente es un escenario con complejidad de negocio real, como un sistema de liquidación con fuentes de precios no unificadas, reglas configurables e historial de datos trazable. El candidato no necesita implementarlo en el momento, solo tiene que entregar tres cosas:

1. **Estructura de datos**
2. **Flujo principal o diagrama de secuencia**
3. **Puntos de prueba clave**

Lo que realmente queremos evaluar son las siguientes capacidades:

**Capacidad de descomposición del negocio**: ¿Puede identificar rápidamente los objetos clave del negocio y sus relaciones? ¿Tiene la capacidad de convertir una descripción de negocio vaga en límites de datos claros? Muchos candidatos, al recibir el enunciado, saltan directamente al diseño de tablas sin haber aclarado primero las diferencias conceptuales.

**Capacidad de juicio en el modelado**: Las decisiones de diseño de la estructura de datos suelen reflejar la profundidad de ingeniería de una persona. ¿Qué campos necesitan versiones históricas? ¿Qué estados requieren auditoría? ¿Qué relaciones cambian con el tiempo? Estos juicios no requieren escribir código, pero sí requieren entender de verdad en qué circunstancias fallará el sistema.

**Conciencia de excepciones y límites**: Un ingeniero con experiencia, ya en la fase de diseño, piensa activamente: ¿cómo se degrada cuando falla una dependencia externa? ¿Cómo se rastrean los datos históricos cuando cambian las reglas? ¿Deben los datos anómalos entrar directamente al flujo oficial? Estas preguntas son donde la AI puede generar código pero no puede asumir el juicio en tu lugar.

**Percepción de la prioridad de pruebas**: La calidad de los puntos de prueba clave suele decir más que la cantidad de casos de prueba. ¿Tiene el candidato la capacidad de identificar, entre un montón de escenarios posibles, cuáles son las rutas de riesgo críticas que deben cubrirse obligatoriamente?

Las preguntas de diseño no tienen una respuesta estándar. Lo que realmente miramos es la forma de pensar del candidato: ¿define el problema antes de desarrollar el diseño? ¿Refleja la estructura de datos la comprensión del negocio? ¿Los puntos de prueba propuestos capturan el riesgo real?

Estas capacidades, la AI no puede reemplazarlas ni disimularlas.

## Un candidato que me dejó una impresión duradera

La semana pasada vino un candidato con dos o tres años de experiencia que, durante la entrevista, estaba un poco confundido. Sentía que lo que le preguntábamos no parecía una entrevista de desarrollo, sino más una entrevista de product manager.

Ese feedback es muy típico.

Muchos desarrolladores están acostumbrados a una división del trabajo: el product manager se ocupa de los requisitos, el backend de las interfaces, el frontend de las páginas, el test de la verificación. Cada uno completa su tarea en su casilla. Con la llegada de la AI, esas casillas se están rompiendo.

El propio candidato también dijo que ahora el 99% de su trabajo de coding lo hace la AI.

Entonces le pregunté a él:

**Si la AI ya hace el 99% del coding, ¿qué puedes hacer tú?**

La pregunta es directa, pero creo que es una pregunta que todo técnico debe responder de frente.

Si tu valor solo es el coding, y el coding ya lo hace mayoritariamente la AI, ¿cuál es tu valor restante?

¿Entender los requisitos? ¿Diseñar la estructura de datos? ¿Juzgar los riesgos del flujo? ¿Identificar los puntos clave de prueba? ¿Diagnosticar problemas en producción? ¿Convertir lo que genera la AI en un resultado de ingeniería fiable?

Si nada de esto es tu capacidad, entonces estás en una situación realmente peligrosa.

## La AI no mejora a todos por igual

Tras un año de práctica, cada vez estoy más convencido de un juicio:

**La AI no mejora a todos por igual. La AI amplifica a los fuertes y disfraza a los débiles.**

Clasifico a los técnicos aproximadamente en tres tipos.

![Tres tipos de desarrolladores en la era AI](/images/ai-dev-three-types.svg)

**Tipo 1: El disfrazado por AI**

Este tipo de persona originalmente no sabe analizar, no sabe diseñar, no sabe probar, solo deja que la AI genere contenido sin poder juzgar si es bueno o malo.

Tras usar la AI, su producción superficial aumenta, pero el riesgo también se incrementa. Antes, si no podía hacerlo, el problema se exponía temprano. Ahora puede usar la AI para hacer algo que parece completo y funciona, pero el problema se pospone hasta el Review, las pruebas, el despliegue, o incluso hasta el cliente.

Así que este tipo de persona no ha sido amplificada por la AI, sino **disfrazada** por ella.

Lo peor es que algunas personas terminan desplazando la responsabilidad: en las decisiones usan la AI como autoridad, y cuando algo sale mal usan la AI como chivo expiatorio:

> "Así lo generó la AI."
> "Le pregunté a la AI y dijo que estaba bien."
> "Ese caso de prueba lo generó la AI, por eso no quedó cubierto."

Pero en una organización de ingeniería, ese argumento no es válido. La AI puede participar en el proceso de producción, pero no puede ser el sujeto de responsabilidad. La persona que adopta la solución, hace el commit del código, fusiona la rama y pone el sistema en producción debe responder por el resultado. Es igual que antes con el código copiado de Stack Overflow: el código puede no ser tuyo, pero quien lo adopta es responsable.

**Tipo 2: El que usa la AI como herramienta**

Este tipo sabe usar la AI y efectivamente mejora su eficiencia: escribir código, buscar información, generar scripts, escribir pruebas, organizar documentación, todo bien.

Este tipo no carece de valor, pero creo que gradualmente se convertirá en una **capa de ejecución mediocre**. La mejora que la AI les aporta es principalmente hacerles completar más rápido el trabajo que ya debían completar, sin mejorar de forma notable la calidad del juicio.

Se pueden usar, pero no reutilizar. Se les pueden asignar tareas, pero no juicios.

**Tipo 3: El amplificado por AI**

Este tipo ya tiene pensamiento estructurado, juicio de ingeniería y consciencia del riesgo; la AI solo les ayuda a desarrollar, complementar, verificar y expresar más rápidamente.

Primero definen el problema y luego usan la AI: le dan a la AI un contexto claro, hacen que genere múltiples soluciones para comparar, cuestionan activamente las conclusiones de la AI, convierten el output de la AI en sus propios juicios, saben qué partes requieren confirmación manual y llevan los resultados hasta la estructura de datos, el flujo, las pruebas, los logs, el manejo de excepciones y los riesgos de despliegue.

Cuando estas personas usan la AI, mejora la eficiencia y también mejora la calidad. Porque la AI no amplifica su velocidad de tecleo, sino su **sistema de juicio**.

## El valor del técnico está migrando de la implementación al juicio

![Migración del valor técnico](/images/ai-dev-value-shift.svg)

Antes, el valor central del técnico era la capacidad de implementación: saber escribir código, escribir interfaces, escribir páginas, depurar bugs, completar tareas. Estas capacidades siguen siendo importantes, pero ya no son suficientes.

En la era AI, lo más importante es la capacidad de juicio: poder definir el problema, diseñar la estructura de datos, mapear los flujos clave, juzgar los límites de excepción, identificar los riesgos de prueba, evaluar si el output de la AI es fiable y hacerse responsable del resultado final.

Por eso cada vez valoro más algo muy difícil de cuantificar: **el buen gusto de ingeniería**.

Pero lo que llamo buen gusto de ingeniería es, en esencia, **criterio**.

El criterio no es preferencia estética ni un estilo personal, sino una capacidad de juicio: entender a través de los primeros principios qué necesita realmente el cliente y luego expresarlo de una manera elegante, y que además esa elegancia sea aceptada por la mayoría.

**La primera capa del criterio es ver a través de la necesidad real.**

El cliente dice "necesito este botón", pero la pregunta real es: ¿por qué lo necesita? ¿En qué situación lo usará? ¿Qué espera que ocurra después de usarlo? ¿Qué debería hacer si falla?

Un ingeniero con criterio no se limita a satisfacer la necesidad superficial. Parte de la situación del usuario y razona hacia atrás: en qué situaciones este sistema debería tomar decisiones por el usuario, en cuáles debería darle suficiente información para que él mismo decida, y en cuáles debe evitar que el usuario cometa un error.

**La segunda capa del criterio es la expresión elegante.**

Pero esta elegancia no es decoración visual, sino el sentido de profesionalidad que transmite el sistema: los mensajes de error ayudan al usuario a entender qué ocurrió, en lugar de decir "error del sistema, contacte al administrador"; los estados vacío, de carga y de fallo están todos manejados completamente, en lugar de una pantalla en blanco; cuando una operación del usuario falla, sabe qué hacer a continuación en lugar de quedarse confundido; los logs del backend ayudan a diagnosticar problemas, y cuando algo falla hay un trace_id para rastrear.

Esto no es una acumulación de detalles, es la materialización del criterio.

**La tercera capa del criterio, y la más difícil, es ser aceptado por la mayoría.**

Un diseño que solo los ingenieros pueden apreciar no es criterio, es autocomplacencia. El verdadero criterio es convertir la capacidad de juicio experta en una sensación de confianza que los no expertos puedan percibir: que un usuario ordinario lo vea y piense "esto parece fiable".

La AI puede generar fácilmente el flujo principal, pero casi no puede replicar el criterio. Porque el criterio no es una regla, es un juicio. Exige que el ingeniero se sitúe realmente en la situación del usuario, entienda qué necesitan de verdad y tome la elección más adecuada.

Y eso es precisamente la verdadera diferencia entre un ingeniero maduro y un ejecutor ordinario.

## Para terminar

Ahora, cuando entrevisto a técnicos, ya no pregunto mucho "¿sabes usar la AI?": esa pregunta tiene poco valor.

Lo que realmente debería preguntarse es:

**Con la intervención de la AI, ¿tu capacidad de juicio ha sido amplificada?**

Si la AI solo te ayuda a completar más rápido el trabajo que ya debías completar, solo estás quedándote en el mismo sitio, pero más rápido.

Si la AI ha amplificado tu comprensión del negocio, tu pensamiento estructurado, tu juicio de ingeniería, tu consciencia de las pruebas y tu capacidad de control del riesgo, entonces sí tienes un valor sostenido en una organización nativa de AI.

Por eso la pregunta que ahora más quiero hacer es:

**Cuando la AI termina de escribir el código, ¿de qué puedes hacerte responsable en ese sistema?**
