---
title: "5 dólares por una semana de trabajo: cómo usamos la IA para capturar el conocimiento fragmentado de la empresa"
description: "Una historia real desde el soporte de migración a la nube y recuperación ante desastres: cómo AI-My-Chats usa el correo electrónico como punto de entrada unificado y modelos multimodales para entender el contexto, convirtiendo conversaciones fragmentadas en conocimiento empresarial rastreable y reutilizable — procesando más de 100 registros al mes por unos 5 dólares en costos de modelos."
author: Las Reflexiones de Lao Sun
date: 2026-08-02T08:00:00+08:00
categories:
  - Agentes Empresariales
tags:
  - IA
  - Agentes Empresariales
  - Gestión del Conocimiento
  - Devify
  - Código Abierto
draft: false
---

**5 dólares** recuperan una semana de trabajo. De agosto del año pasado a julio de este año, nuestro equipo de producto de migración a la nube y recuperación ante desastres usó AI-My-Chats para procesar más de 100 piezas de conocimiento fragmentado cada mes, con un costo promedio de modelo de unos **5 dólares**. Después de cambiar a modelos de código abierto, eso bajó recientemente a unos **3.1 dólares**. Este artículo trata sobre la práctica y el razonamiento detrás de esas cifras.

{{< figure src="/images/why-we-built-ai-my-chats/azure-cost-overview.webp" alt="Resumen de costos mensuales de Azure: de agosto de 2025 a julio de 2026, desglosado por mes, con un total de 70.54 dólares, dividido por nombre de servicio, región y suscripción" caption="La factura real: desglosada mes a mes durante el último año, con un promedio de unos 5 dólares al mes en costos de modelos" >}}

{{< callout type="info" >}}
**Última actualización:** AI-My-Chats ahora es compatible con GitHub Issues. Envía fragmentos de chat y capturas de pantalla seleccionados a tu buzón dedicado de AI-My-Chats, y el sistema organiza el contenido automáticamente y crea un Issue estructurado en tu repositorio de GitHub de destino. Incluso puedes definir un idioma de destino para el Issue, así que sin importar en qué idioma haya sido la discusión original, el resultado puede salir en inglés, español o el idioma que elijas — sin necesidad de iniciar sesión en GitHub ni de llenar ningún formulario.
{{< /callout >}}

{{< figure src="/images/why-we-built-ai-my-chats/chat-to-github-issue.webp" alt="El flujo de tres pasos de AI-My-Chats, de chat a GitHub Issue: un usuario plantea una solicitud en el chat, reenvía la conversación al buzón de AI-My-Chats, y la IA extrae el contexto, las tareas pendientes y los adjuntos para generar un Issue estructurado en GitHub" caption="De un registro de chat a un Issue estructurado en GitHub — a solo un reenvío de distancia" >}}

## I. Por qué construimos esto

### Reflexiones sobre la captura de conocimiento empresarial

Hace poco compartí cómo usamos AI-My-Chats en Reddit, y le llegó a mucha gente. Dos preguntas surgieron una y otra vez.

Primero: las empresas generan una enorme cantidad de información valiosa cada día, en correos, chats, notas de reuniones y discusiones de proyectos — texto, capturas de pantalla, registros, adjuntos, juicios improvisados. Muy poco de eso llega a un sistema de gestión de proyectos o a una base de conocimiento. No es que a las empresas les falte conocimiento; es que convertir información en conocimiento implica demasiada fricción. Releer el contexto, extraer los puntos clave, darle formato, archivarlo en el sistema correcto — todo eso exige un flujo constante de trabajo manual. La mayor parte de esta información no carece de valor, simplemente es demasiado costosa de organizar, así que termina dispersa entre distintas herramientas y distintas personas.

Segundo, la sensibilidad de los datos: si el contenido toca proyectos internos, detalles técnicos y datos de negocio, ¿de verdad está bien entregárselo a un servicio de modelos externo como OpenAI o Anthropic? Es una preocupación totalmente razonable, y es justo lo que AI-My-Chats está diseñado para resolver. Nunca lee tus chats de forma automática — tú decides qué vale la pena capturar, y el sistema lo organiza usando ese contexto. Tampoco está atado a un único proveedor de modelos. Las empresas pueden elegir modelos comerciales, modelos de código abierto, o modelos que corren on-premises o en una nube privada, según sus necesidades de calidad, costo y seguridad de datos.

Ahora mismo usamos principalmente DeepSeek V4 Pro para la comprensión y el resumen de texto, y Qwen 3.6 Pro para imágenes y contexto — aunque esa es solo nuestra combinación actual, no una limitación fija del producto. Devify, el proyecto de código abierto detrás de AI-My-Chats, ya tiene integración configurable de modelos incorporada, así que cambiar de modelo no significa rediseñar todo el flujo de trabajo.

{{< figure src="/images/why-we-built-ai-my-chats/model-configuration.webp" alt="Pantalla de configuración de modelos de Devify, mostrando dos modelos conectados — Qwen3.6-plus y DeepSeek-V4-Pro — incluyendo endpoint de API, clave, parámetros y estado activo" caption="Los modelos son intercambiables: las empresas pueden combinarlos según sus necesidades de calidad, costo y seguridad de datos" >}}

El informe de Gartner *Token Costs Escalate and AI Sovereignty Concerns* (G00852160) lo resume bien: "dónde corre la IA se está volviendo tan importante como lo que la IA puede hacer". El mismo informe cita una encuesta de CEOs de 2026 en la que el 70% nombró la soberanía tecnológica como una preocupación compartida a nivel de comité ejecutivo, y el 90% dijo estar aumentando la inversión en estrategia geográfica para abordarla. A medida que maduran los modelos de código abierto y el despliegue privado, la libertad de elegir tus propios modelos y controlar tus propios datos se está convirtiendo en una parte central de la infraestructura de IA empresarial.

Ese es el problema que nos propusimos resolver: mientras las empresas mantienen el control total de sus datos, sus modelos y su proceso de tratamiento, bajar el costo de convertir información en conocimiento, y transformar contenido disperso en conocimiento empresarial rastreable, accionable y reutilizable.

### De la respuesta rápida a la captura de conocimiento

OneProCloud construye productos de migración a la nube nativa y recuperación ante desastres — HyperMotion para migración, HyperBDR para recuperación ante desastres — con clientes principalmente en el extranjero, más algunos nacionales. Ambos productos ya son compatibles con las principales plataformas de nube pública y privada dentro y fuera de China, cubriendo prácticamente cualquier entorno de nube heterogéneo que una empresa pueda tener.

Ambos productos están construidos alrededor de la simplicidad, la eficiencia y una automatización intensa. Para la migración de servidores y la recuperación ante desastres, los usuarios no necesitan crear manualmente máquinas virtuales, discos u otros recursos en la nube de destino de antemano — el sistema lee la configuración de origen y aprovisiona el destino automáticamente, habilitando migraciones con un clic, simulacros de recuperación y conmutación por error.

Dicho esto, una migración o recuperación completa suele involucrar el entorno de origen, la red, el almacenamiento, el sistema operativo y la plataforma de nube de destino, y los problemas que enfrentan los clientes no siempre vienen de HyperMotion o HyperBDR — pueden venir igual de fácil de dependencias del lado de origen o de destino. En sentido estricto, algunos de esos problemas quedan fuera del alcance de nuestro producto. Pero a los clientes les importa si se logra el objetivo completo de la migración o la recuperación, no dónde se traza exactamente el límite de nuestro producto. Así que, en los últimos años de soporte a proyectos, mientras ayude a avanzar, generalmente nos hemos involucrado y hemos trabajado junto con los clientes para resolverlo. Muchos clientes se quedan con OneProCloud no solo porque el producto es fácil de usar, sino porque nos importa que realmente logren su objetivo.

A medida que crecía nuestra base de usuarios, empezamos a pensar en cómo mantener respuestas rápidas mientras también capturábamos la experiencia, los requisitos y los criterios técnicos que surgían del trabajo de soporte — porque una vez que tu base de usuarios se multiplica, no puedes simplemente sumar más personas y esperar mantener la misma calidad de servicio y velocidad de respuesta.

{{< figure src="/images/why-we-built-ai-my-chats/knowledge-workflow-en.webp" alt="El flujo de conocimiento de AI-My-Chats: entradas de múltiples fuentes (chat, correo, reuniones, capturas de pantalla) pasan por una curación humana, entran a AI-My-Chats para su comprensión, estructuración y enrutamiento (con soporte para modelos comerciales, modelos de código abierto y despliegue privado), y salen hacia Jira, GitHub Issues, Feishu y bases de conocimiento" caption="La arquitectura general de AI-My-Chats: entrada multifuente, curación humana, procesamiento unificado por IA, salida a múltiples destinos" >}}

Queríamos que la IA convirtiera esta información fragmentada en conocimiento empresarial rastreable y reutilizable sin añadir carga extra al proceso — y, con el tiempo, dejar que el sistema se apoyara en ese conocimiento acumulado para ayudar directamente a los usuarios a analizar y resolver problemas.

---

## II. Cómo lo diseñamos

### Por qué no nos integramos directamente con las plataformas de chat

Al principio, exploramos formas de conectarnos directamente a las plataformas de mensajería, incluyendo proyectos como WeChaty. Ese tipo de enfoques capturan mensajes mediante emulación de protocolos, hooks u otros métodos no oficiales, pero suelen venir con riesgos de estabilidad, cumplimiento normativo y seguridad de cuentas — difíciles de justificar como infraestructura de largo plazo para una empresa.

Más importante aún, terminamos dándonos cuenta de que leer automáticamente cada conversación no es una buena idea, para empezar. La charla diaria de una empresa está llena de información desechable; no todos los mensajes merecen conservarse. Alimentar todo eso a un sistema solo genera ruido y empeora el problema de sensibilidad de datos. Así que nos inclinamos por dejar que las personas dentro de la empresa tomaran esa decisión por sí mismas — qué vale la pena conservar, qué necesita seguimiento, qué experiencia debería entrar a la base de conocimiento.

Luego notamos que las aplicaciones de mensajería ya permiten reenviar contenido seleccionado por correo. Eso nos dio un camino más simple y controlable: no integrarnos con la plataforma de chat en absoluto, no recolectar todo automáticamente, simplemente dejar que los usuarios elijan lo que vale la pena y lo envíen ellos mismos al proceso. Esa pequeña acción resuelve dos problemas a la vez — el acto de enviar algo ya es en sí mismo un filtro, y el sistema solo toca contenido que la empresa decidió enviar explícitamente, lo cual da un límite de datos mucho más claro.

Pero reenviar contenido por correo no basta por sí solo. Si nadie aclara el contexto, los puntos clave y los siguientes pasos, esa información todavía no puede fluir hacia un proceso posterior, ni puede buscarse, rastrearse o reutilizarse más adelante. Nuestro objetivo nunca fue mover información de una herramienta a otra — es convertir notas dispersas e improvisadas en entradas de conocimiento que un equipo pueda tomar y seguir usando.

### De información fragmentada a conocimiento capturado

Una vez que definimos el envío guiado por el usuario, la siguiente pregunta fue cómo convertir esa información dispersa en conocimiento empresarial que realmente pudiera gestionarse y reutilizarse. En ese momento, OneProCloud usaba principalmente Jira para ingeniería y seguimiento de incidencias, así que la versión uno de AI-My-Chats tenía un objetivo simple: tomar el contenido que la gente enviaba, hacer que la IA lo organizara, y escribir el resultado estructurado directamente en Jira.

Esa primera versión usaba GPT-4.1 mini para texto y el OCR de Microsoft para las capturas de pantalla. Cuando llegaba un correo, el sistema extraía el cuerpo del texto, las imágenes y los adjuntos, y luego usaba el contexto para generar un título, el trasfondo, una descripción del requisito, los hallazgos existentes y una lista de tareas pendientes. En cuanto salió GPT-5 nano, migramos gradualmente el procesamiento de texto — misma calidad, menor costo por elemento.

En los últimos meses empezamos a incorporar modelos de código abierto como DeepSeek y Qwen. En pruebas reales funcionaron bien tanto en nuestros casos de comprensión de texto como multimodales, y en cuanto la diferencia de calidad dejó de importar, el costo, el control y la flexibilidad de despliegue empezaron a importar mucho más. Hoy usamos principalmente DeepSeek V4 Pro para la comprensión y el resumen de texto, y Qwen 3.6 Pro para imágenes y contexto. Después de cambiar a esta combinación de código abierto, nuestro costo mensual promedio bajó aún más, de unos 5 dólares a unos 3.1 dólares — mismo volumen de trabajo, un cambio más de modelo, y el costo bajó un escalón más.

Nada de esto se trató de perseguir un modelo en particular. Un modelo es solo un componente reemplazable; lo que realmente importa es mantener todo el proceso de conocimiento estable, controlable y capaz de funcionar a largo plazo. La información que antes estaba dispersa entre correos, capturas de pantalla y chats cotidianos ahora se convierte en un único registro estructurado que conserva el trasfondo, el criterio actual y los siguientes pasos. Incluso después de resolver un problema, el proceso y la experiencia detrás de él no desaparecen con la conversación — siguen siendo buscables, rastreables y reutilizables.

Gartner plantea algo similar en *AI Inference's Financial Reckoning* (G00847756): el valor de la IA empresarial está pasando de la inversión puntual y de capital que implica entrenar modelos, al consumo continuo y operativo que implica la inferencia, un cambio que transforma de raíz cómo los líderes de TI tienen que hacer sus cuentas. El mismo informe proyecta que, para 2030, más del 80% del gasto en IaaS optimizado para IA se destinará a sostener cargas de trabajo de inferencia. Una vez que la IA realmente corre dentro de tu flujo de trabajo, la capacidad del modelo por sí sola no basta para evaluarlo — también hay que sopesar la calidad, el costo por elemento y el valor real. Para nosotros, que un flujo de trabajo de IA pueda sostenerse a largo plazo se reduce a dos cosas: si realmente hace bien el trabajo, y si puede seguir haciéndolo a un costo estable y controlable.

Cuando todavía usábamos modelos de OpenAI, nuestro equipo de producto de migración a la nube y recuperación ante desastres, de unas 20 personas, procesaba con AI-My-Chats más de 100 incidencias, requisitos y registros de conocimiento al mes. El costo del modelo: unos 5 dólares, entre 30 y 40 yuanes.

{{< figure src="/images/why-we-built-ai-my-chats/azure-cost-overview.webp" alt="Resumen de costos mensuales de Azure: de agosto de 2025 a julio de 2026, desglosado por mes, con un total de 70.54 dólares" caption="La misma factura, vista de otra forma: desglosada por mes, la curva de costos es mucho más intuitiva que un total acumulado" >}}

Este tipo de información antes requería que alguien la releyera, descifrara el contexto y extrajera los puntos clave antes de poder avanzar al siguiente paso. AI-My-Chats básicamente elimina esa etapa manual intermedia — y, con 15 a 30 minutos ahorrados por elemento, eso suma aproximadamente una semana completa de trabajo liberada cada mes. Dicho de otra forma: por unos 5 dólares al mes, podemos analizar y organizar más de 100 piezas de información fragmentada, para que tanto fluyan hacia nuestro flujo de trabajo actual como permanezcan como conocimiento empresarial buscable y reutilizable.

Lo más importante que demuestra esta cifra no es que ahorramos algo de dinero — es que este tipo de proceso de conocimiento puede funcionar de forma confiable a un costo unitario muy bajo, con mucho margen para escalar aún más.

### De reconocer imágenes a entender el contexto

La versión uno dependía principalmente del OCR para leer el texto de las capturas de pantalla, pero pronto descubrimos que reconocer las palabras de una imagen no resuelve la mayoría de los problemas. Cuando alguien pone una imagen en una conversación, lo que importa es por qué envió esa imagen en particular en ese momento — y el OCR simple no puede captar cómo se relaciona una imagen con la discusión que la rodea.

Así que pasamos a modelos multimodales que entienden tanto el contenido de la imagen como el contexto completo a la vez. El beneficio no fue solo un mejor reconocimiento de imágenes; el sistema mejoró mucho a la hora de juzgar el trasfondo de un problema, lo que el usuario realmente quiso decir, y qué debía pasar después. A partir de ahí, AI-My-Chats dejó de procesar solo texto e imágenes por separado — empezó a procesar lo que esa información realmente significaba dentro del contexto completo del negocio.

---

## III. De un producto único a una plataforma de conocimiento extensible

### De un único destino a un enrutamiento de conocimiento extensible

En la versión uno, el contenido organizado iba directo a Jira para que el equipo de ingeniería le diera seguimiento. Pero cuanto más profundizábamos en su uso, más notábamos que la misma pieza de información suele tener más de un uso. Una incidencia de producto podría necesitar que ingeniería la siga rastreando, o podría valer la pena convertirla en una FAQ pública que ayude a los clientes a resolver el mismo problema por sí mismos. Un requisito podría necesitar entrar a una Bitable de Feishu para un seguimiento unificado, o sincronizarse con GitHub Issues para sumarse al flujo del proyecto.

Así que separamos el paso de organización de la IA de dónde termina finalmente el conocimiento resultante. La IA se encarga primero de entender el contexto, limpiar la información y producir contenido estructurado; luego, según cómo se vaya a usar, el resultado se escribe en el sistema empresarial que corresponda. Además, agregamos soporte para Bitable de Feishu y GitHub Issues, y podemos seguir sumando más destinos desde aquí. Las fuentes también pueden seguir ampliándose — más allá de los fragmentos de chat, correos, capturas de pantalla y adjuntos que la gente envía por su cuenta, las notas de reuniones, las discusiones de proyectos y otra información fragmentada pueden fluir por el mismo proceso.

Así es como pensamos la extensibilidad de AI-My-Chats: no se trata de vincular fijamente una pieza de información a un sistema de destino. Se trata de convertir primero el contenido fragmentado en conocimiento real, y luego enrutar ese conocimiento hacia donde la empresa realmente lo necesite.

### Dejar que las Skills propias de la empresa participen en el criterio

Lo siguiente que queremos hacer es traer a AI-My-Chats las Skills que una empresa ya ha acumulado — y por Skills no nos referimos solo a scripts técnicos. También nos referimos a los criterios, los principios de trabajo y la experiencia de negocio que un equipo construye a lo largo de proyectos de largo plazo.

En el pasado, ese tipo de criterio solía vivir en la cabeza de unas pocas personas con experiencia. De ahora en adelante, queremos que el sistema se apoye en el conocimiento y las reglas propias de la empresa mientras organiza información, para que su análisis y clasificación encajen realmente con la forma en que esa empresa trabaja. A medida que crece el uso, lo que el sistema acumula deja de ser un montón de registros dispersos y se convierte en conocimiento que refleja cada vez más cómo opera realmente la empresa.

### Convertir un flujo de trabajo probado en una app

A medida que se acumulaban los casos de uso, empezamos a hacernos una pregunta más grande: ¿qué necesitan realmente las empresas — una herramienta genérica de orquestación de agentes, o una aplicación que ya resuelve un problema específico? Las personas dentro de una empresa suelen conocer mejor que nadie su propio negocio, pero conocer el negocio no es lo mismo que poder convertir esa experiencia, esas reglas y esa forma de trabajar en un flujo de trabajo de IA estable y efectivo. Con frecuencia, lo difícil no es si el modelo puede entender una frase — es cómo dividir el proceso en pasos, cómo definir los criterios de decisión, y a dónde debe llegar el resultado final.

Así que llegamos a una conclusión bastante directa:

**Cuanto más genérico, menos útil.**

{{< figure src="/images/why-we-built-ai-my-chats/fde-productized-delivery-en.webp" alt="Comparación entre el desarrollo a medida y la entrega de IA productizada: la entrega tradicional parte de los requisitos del cliente y construye todo desde cero antes de personalizarlo; la entrega de IA productizada parte de una app y un flujo de trabajo ya validados, que un FDE adapta al escenario del cliente para una entrega llave en mano" caption="De 'construir todo desde cero cada vez' a 'un producto validado más adaptación en sitio'" >}}

Eso no es una crítica a la capacidad genérica a nivel de plataforma — es que lo que las empresas realmente necesitan no es una configurabilidad infinita. Necesitan un producto que ya esté validado contra un problema específico y listo para usarse. Así que nuestra elección fue empaquetar en apps concretas los flujos de trabajo que hemos validado una y otra vez: los modelos, las bases de conocimiento, los permisos y los componentes base pueden seguir siendo flexibles, pero la lógica de negocio que realmente determina el resultado ya está diseñada y validada de antemano por el producto. Los usuarios no tienen que diseñar prompts y flujos de trabajo desde cero — solo configuran lo que necesitan para su propio entorno y empiezan a usarlo.

Esto también nos hizo repensar el valor del FDE — el Forward-Deployed Engineer. La entrega de software solía venir en dos sabores: partir de cero, entender los requisitos y construir algo a medida, o tomar un producto ya hecho y forzarlo a encajar en el proceso del cliente. El primero es demasiado caro; el segundo rara vez resuelve realmente el problema del cliente.

La IA ha hecho más rápido construir y ajustar software, y eso abrió una tercera opción: construir un producto y un flujo de trabajo ya validados que cubran la mayoría de los escenarios, y luego enviar a un FDE al sitio del cliente para adaptarlo a sus propios datos, reglas y procesos. Es un poco como la entrega de software estilo "kit de comida": la capacidad principal y el flujo de trabajo ya funcionan, y una vez que llega al entorno del cliente, lo que queda es la configuración final, el ajuste fino y la integración, terminando en un sistema que realmente resuelve el problema.

Este es exactamente el modelo que AI-My-Chats está explorando. Sus capacidades principales vienen del proyecto de código abierto Devify, así que un FDE puede hacer la adaptación en sitio sobre un producto maduro, abierto y ajustable, en lugar de construir todo desde cero cada vez. Visto así, el valor de un FDE no es solo ayudar a una empresa a construir una nueva app de IA — es conectar un producto maduro con las necesidades reales de una empresa, la última milla que hace que todo funcione de verdad.

---

## Cómo probar AI-My-Chats

Las capacidades principales detrás de AI-My-Chats son de código abierto en GitHub como el proyecto Devify (<https://github.com/cloud2ai/devify>). Si quieres probarlo rápido, ofrecemos dos opciones.

### Opción 1: Probar el SaaS directamente

Abre <https://aimychats.com>, regístrate y empieza a usarlo de inmediato — sin necesidad de despliegue. Ideal para desarrolladores individuales o equipos pequeños que quieren validar todo el flujo rápidamente. El camino de principio a fin: **herramientas de chat (WeChat / WhatsApp / Slack) → reenviar por correo → AI-My-Chats procesa automáticamente → resultados estructurados (Bug / ToDo / Tarea / Resumen) → sincronizado con Jira, GitHub Issues, Bitable de Feishu y sistemas similares.**

### Opción 2: Despliegue local / autoalojado (recomendado)

Ideal para equipos con requisitos de seguridad de datos o integración de sistemas. Devify admite despliegue completamente local, y la forma más simple de empezar es con Docker:

```bash
git clone https://github.com/cloud2ai/devify.git
cd devify
cp env.sample .env   # copia la plantilla y ajústala según sea necesario
docker compose up -d
```

> ⚠️ El repositorio incluye una plantilla, `env.sample`, mientras que Docker Compose lee `.env` por defecto. Antes de iniciar, ejecuta `cp env.sample .env` y completa tu configuración — de lo contrario el servicio no arrancará.

Una vez que esté funcionando, abre la interfaz de Devify en tu navegador y registra la cuenta de administrador. Desde ahí, todo se configura en la interfaz web, sin volver a tocar la línea de comandos — solo dos pasos para dejarlo funcionando.

**Paso 1 · Conectar un modelo de IA:** Ve a "Consola de administración → Configuración de modelos", agrega un modelo (API key del proveedor, endpoint, nombre del modelo), y márcalo como predeterminado en la configuración de la app. Es compatible con proveedores comunes como OpenAI, Tongyi Qianwen y OpenRouter, además de modelos locales.

**Paso 2 · Configurar la recepción de correo (IMAP):** Ve a "Configuración → Correo", elige la modalidad de extracción por IMAP, y completa la dirección del servidor, la cuenta, la contraseña, el puerto SSL y la carpeta de entrada de tu buzón empresarial. A partir de ahí, el sistema extraerá el correo según un horario y lo procesará automáticamente.

Una vez completados ambos pasos, todo el flujo queda activo: **herramientas de chat → reenviar al buzón de la empresa → extracción por IMAP → procesamiento con IA → resultados estructurados, sincronizados con Jira / GitHub Issues / Bitable de Feishu.**

Si tienes algún problema al probarlo, o quieres contribuir o intercambiar ideas sobre código abierto, abre un issue o una discusión en el [repositorio de GitHub](https://github.com/cloud2ai/devify).
