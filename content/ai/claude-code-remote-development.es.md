---
title: "¿Puede el móvil convertirse en tu herramienta principal de desarrollo? Un registro de verificación real"
date: 2026-06-20T08:00:00+08:00
slug: "claude-code-remote-development"
author: Ray Sun
categories:
  - Práctica con herramientas de IA
tags:
  - Claude Code
  - Desarrollo remoto
  - Desarrollo móvil
  - tmux
  - AI编程
draft: false
---

Tarde de fin de semana, tumbado en el sofá, una taza de café, coges el móvil y... ¿escribes el código, ejecutas las pruebas y despliegas en producción?

Suena un poco descabellado. El móvil no es una máquina de desarrollo, eso es de sentido común. Sirve para consultar documentación, ver el estado del CI o responder urgentemente a un comentario de PR, pero el trabajo real de desarrollo —escribir código, depurar, desplegar, verificar resultados— siempre ha exigido volver al ordenador.

Yo también lo creía así, hasta que conocí la funcionalidad Remote Control de Claude Code.

Este artículo es el registro que escribí después de probar todo esto con mi propio proyecto.

<!-- more -->

## La conclusión primero

Funciona. Una vez que todo está en marcha, la situación es más o menos esta:

Por la noche, tumbado mirando el móvil, se me ocurre que a SourceLens le falta un mecanismo de compartición: cuando un usuario termina una consulta, la respuesta debería poder generar un enlace público para que otros lo vean directamente. Es una funcionalidad completa: el backend necesita diseñar la tabla de compartición, generar URLs cortas y gestionar permisos; el frontend necesita un botón de compartir y una landing page; también hay que pensar en la política de expiración de enlaces. Antes, este tipo de requisito tenía que esperar a que me sentara al ordenador y abriera varios tabs.

Ahora le describo el requisito a Claude, él me va preguntando uno a uno para confirmar los detalles, y luego empieza a escribir código, crear tablas, ejecutar pruebas y abrir un PR. Yo reviso el PR tumbado, digo "cambia esto aquí", él lo cambia y sigue ejecutando. A la mañana siguiente, en el metro camino al trabajo, la funcionalidad ya estaba mergeada.

Lo mismo con el blog: antes, desde que tenía una idea hasta publicarla podían pasar varios días —organizar el pensamiento, escribir el borrador, maquetar, publicar en WeChat, sincronizar otras plataformas—. Ahora le explico mis ideas a Claude por el móvil, él me ayuda a estructurarlas y genera el borrador, yo lo ajusto durante el trayecto, y antes de llegar a la oficina ya está todo publicado.

Todo el proceso sin tocar el ordenador. Eso sí, no basta con instalar una App: hay varios requisitos previos que hay que tener configurados de antemano, y sin alguno de ellos todo se atasca.

## ¿Con qué verificar esto?

Elegí este blog como proyecto de prueba.

No porque sea sencillo —todo lo contrario—. Un artículo desde que se termina hasta que se publica pasa por estas fases: escribir el Markdown en local, construir la vista previa con Hugo, hacer commit y push con Git, que GitHub Actions despliegue automáticamente en el servidor, y finalmente sincronizarlo en la cuenta de WeChat. Cada fase puede fallar, y el resultado de cada una necesita verificación.

Si el móvil es capaz de completar toda esta cadena, más o menos puedo responder esa pregunta.

---

## Primero, aclarar el papel de Claude

Antes de hablar de cómo montarlo todo, hay algo que merece mencionarse por separado: **todo el trabajo de configuración de este entorno, Claude puede ayudarte a completarlo.**

La configuración del CI/CD para el entorno de previsualización, la depuración de la autenticación SSH, la instalación y el uso de tmux — no necesitas saber todo esto de antemano. Solo necesitas saber qué quieres montar y por qué. El resto se lo dejas a Claude, que te guía paso a paso.

El objetivo de este artículo también es ese: **explicar la lógica, no un manual de operaciones**. Con la lógica clara, Claude es tu herramienta de implementación.

---

## Tres cosas que hay que tener claras

### Primera: el resultado tiene que ser visible desde el móvil

Este es el paso que más fácilmente se salta y donde más se tropieza.

Mucha gente empieza configurando Remote Control, Claude dice "ya está hecho" y abres el móvil... sin ver ningún cambio. Porque `localhost:1313` simplemente no abre en el móvil, lo que equivale a desarrollar a ciegas.

Solo hay una solución: **antes de ponerte a trabajar, monta un entorno de previsualización accesible desde el móvil**.

Mi enfoque fue dividir el proceso de publicación en dos líneas:

```
push a rama main  →  despliegue automático a preview.sunqi.site (previsualización, incluye borradores)
git tag v*        →  despliegue automático a sunqi.site (producción)
```

Con cada commit, el CI se ejecuta automáticamente, abres la dirección de previsualización en el móvil y ves el resultado renderizado real. Cuando confirmas que está bien, creas el tag y producción se despliega automáticamente.

La configuración de GitHub Actions correspondiente, con dos workflows independientes:

```yaml
# .github/workflows/preview.yml
name: Deploy to Preview
on:
  push:
    branches: [main]
jobs:
  preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Build
        run: hugo --gc --minify --buildDrafts
      - name: Setup SSH
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/id_rsa
          chmod 600 ~/.ssh/id_rsa
          echo "StrictHostKeyChecking no" >> ~/.ssh/config
      - name: Deploy
        run: |
          rsync -avz --delete \
            -e "ssh -p ${{ vars.REMOTE_PORT }} -o StrictHostKeyChecking=no" \
            public/ \
            ${{ vars.REMOTE_USER }}@${{ secrets.REMOTE_HOST }}:${{ vars.REMOTE_PATH_PREVIEW }}/
```

> **Aviso de trampa común**: en el CI, el valor de `REMOTE_HOST` debe ser la IP real del servidor, no el dominio. Si el dominio pasa por un CDN como Cloudflare, las peticiones SSH llegarán al nodo del CDN y agotarán el tiempo de espera — a mí me llevó bastante tiempo depurar esto.

### Segunda: la autenticación tiene que estar configurada

Con el entorno de previsualización listo, Claude puede "ver los resultados". Pero cuánto puede hacer por ti depende de los permisos que le hayas dado.

La autenticación no es opcional; es el requisito previo para que Claude pueda ejecutar cosas realmente en tu nombre.

**SSH Key** — permite que Claude haga SSH directamente al servidor para consultar logs, reiniciar servicios o depurar problemas de despliegue, sin que tengas que retransmitirle nada:

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub user@your-server
ssh user@your-server "echo ok"   # verificar login sin contraseña
```

**GitHub CLI** — permite que Claude opere directamente sobre el repositorio: ver logs de Actions, relanzar ejecuciones, configurar variables, gestionar PRs:

```bash
gh auth login
gh auth status   # verificar
```

Una vez configurados estos dos puntos, la capacidad de Claude es completamente diferente. Volviendo al ejemplo de la depuración de este artículo: el despliegue del CI fallaba, Claude ejecutó `gh run view` directamente para obtener los logs, localizó la causa, modificó el workflow y lo volvió a lanzar — yo lo observé todo desde el móvil y solo intervine en los puntos de decisión clave diciendo "sí" o "cambia de enfoque". Sin la autenticación configurada, cada uno de esos pasos habría tenido que hacerlo yo manualmente.

### Tercera: la sesión tiene que ser continua

Este punto suele ignorarse, pero determina si el móvil puede integrarse de verdad en tu flujo de trabajo.

Si ejecutas `claude` directamente en el terminal, al cerrar la ventana el proceso muere. Usando tmux para que Claude Code corra en segundo plano, la sesión sobrevive a desconexiones de red, cambios de aplicación o bloqueo de pantalla:

```bash
tmux new-session -s dev      # crear sesión persistente
cd ~/my-project
claude                       # entrar en Claude Code
/rc                          # activar Remote Control (también funciona /remote-control)

# Ctrl+B → D  separar la sesión (el proceso sigue ejecutándose)
# tmux attach -t dev  volver a conectarse
```

<img src="/images/claude-rc-terminal-v2.png" alt="Activando Remote Control con /rc en el terminal" style="max-width:100%;margin:16px 0"/>

Una vez activado, toca el icono en la parte superior de Claude App o del cliente de escritorio, entra en la página **Code** y verás la lista de sesiones remotas; busca la sesión correspondiente y entra para tomar el control directamente.

<img src="/images/claude-mobile-session-v2.png" alt="Lista de sesiones en Claude App para móvil" style="max-width:360px;display:block;margin:16px 0"/>

Una vez dentro de la sesión, la interfaz de interacción en el móvil es idéntica a la del escritorio:

<img src="/images/claude-code-mobile-interaction-v2.png" alt="Interfaz de interacción de Claude Code en móvil" style="max-width:360px;display:block;margin:16px 0"/>

Pero la persistencia no es solo que "el proceso no muera"; lo más importante es el **traspaso sin interrupciones entre dispositivos**. Una tarea que empiezas en el metro, puedes continuarla directamente en el ordenador al llegar a la oficina; si te acuerdas de algo por la noche, la retomas desde el móvil — misma sesión, mismo contexto, sin tener que volver a explicar nada, sin inicios de sesión ni cambios de dispositivo. Eso es lo que significa trabajar verdaderamente desde cualquier lugar.

**Plataformas compatibles**: iOS y Android ya son compatibles; la extensión de VS Code también puede activarlo escribiendo `/rc`. Requiere suscripción Claude Pro ($20/mes) o superior, y Claude Code v2.1.51+.

---

## Algunos consejos para un uso más fluido

### Entrada de voz: usa un teclado de terceros, no el nativo de Claude

Claude App en móvil tiene entrada de voz nativa, pero su soporte para el chino siempre ha sido problemático — la precisión es inestable, los problemas se acentúan con la terminología técnica, y la mezcla de chino e inglés es prácticamente inviable. No es un problema puntual, es la situación habitual.

Se recomienda cambiar al teclado de WeChat o al de Doubao:

<div style="display:flex;gap:12px;align-items:center;margin:12px 0">
  <img src="/images/wechat-input-icon.png" width="48" height="48" style="border-radius:12px" alt="Teclado de WeChat"/>
  <img src="/images/doubao-input-icon.png" width="48" height="48" style="border-radius:12px" alt="Teclado de Doubao"/>
</div>

Estos dos teclados están muy bien optimizados para la mezcla de chino e inglés: puedes intercalar palabras en inglés o términos técnicos mientras hablas en chino y la precisión de reconocimiento sigue siendo alta, más que suficiente para el desarrollo cotidiano. Mantén pulsada la tecla de voz, di lo que necesitas, echa un vistazo al texto para confirmarlo y luego envíaselo a Claude. Ese paso de confirmación extra ahorra mucho más tiempo que corregir texto mal reconocido. Prueba los dos y quédate con el que te resulte más cómodo.

### No intentes abarcar demasiado de golpe: primero la estructura, luego el detalle

Esta es la forma de trabajar más importante en el móvil, ya sea escribiendo contenido o desarrollando — la lógica es siempre la misma: **primero define la estructura, luego rellena el contenido**.

Al escribir un artículo, pídele primero a Claude que estructure el esquema general, confirma que la lógica es correcta y luego escribe sección por sección. Confirmas una sección y pasas a la siguiente. Este artículo se hizo exactamente así, y fue mucho más fluido que dar todos los requisitos de golpe y terminar haciendo grandes revisiones.

Lo mismo aplica al desarrollo de funcionalidades: desglosa primero los módulos claramente, define qué hace cada parte, y luego avanza bloque a bloque, en lugar de darle a Claude todo el requisito de una vez.

Escribir en el móvil es lento, y cuando una tarea es compleja y difícil de describir, puedes invertir el proceso y pedirle a Claude que te pregunte él:

```
Quiero implementar [objetivo], la situación es algo compleja. Por favor hazme
las preguntas una a una para entender bien los requisitos antes de empezar.
```

### Skills: instala según el contexto, añade lo que te falta

No hace falta instalarlas todas de golpe; hazlo según tu caso de uso:

**Producción de contenido** (escribir artículos, publicar en WeChat): `wechat-draft-publisher` es imprescindible, permite enviar artículos directamente al borrador de WeChat, pero antes hay que configurar el AppID y AppSecret de la cuenta oficial. Las skills de generación de imágenes las eliges según las herramientas que uses.

**Desarrollo**: skills del tipo `superpower` valen la pena instalarlas, ya que amplían considerablemente las capacidades básicas de Claude Code. Las demás, según necesidad — si no sabes qué instalar, díselo directamente a Claude y pídele que las encuentre e instale él.

### Notificaciones push: aviso automático al terminar una tarea

Activa los permisos de notificación de Claude App en la configuración del sistema del móvil; es una pieza clave de toda la experiencia móvil. Cuando Claude termina una tarea larga o necesita que tomes una decisión para continuar, te enviará una notificación push al móvil — no tienes que estar mirando la pantalla constantemente; haz lo que tengas que hacer y vuelve cuando llegue la notificación.

---

## Algo que hay que dejar claro: el responsable eres tú

Completar un desarrollo completo desde el móvil es perfectamente viable, pero hay un punto que no tiene nada que ver con el móvil: **el ser humano debe ser responsable del resultado final**.

La IA puede escribir código, ejecutar pruebas y abrir PRs, pero no asume las consecuencias. Si una migración de base de datos sale mal, si hay un error en la configuración de permisos, si hay un fallo en la lógica de pagos — la responsabilidad es tuya, no de Claude. Eso no cambia si estás en el móvil o delante del ordenador; cambia si revisaste las cosas con atención o no.

Ante operaciones de alto riesgo, la actitud correcta no es "vuelvo al ordenador para revisarlo", sino: **si no estás seguro, no hagas commit**.

Primero recorre la lógica en la conversación: pídele a Claude que explique qué hace cada paso, que te pregunte cuál es tu expectativa en cada punto de decisión clave, hasta que tú mismo puedas explicar toda la lógica con claridad. Entonces da la instrucción de ejecución. Si estás en el ordenador, puedes añadir una revisión manual viendo el código directamente; si estás en el móvil, la confirmación por conversación puede lograr el mismo efecto, aunque requiere un poco más de paciencia.

Este es el principio central de la colaboración humano-IA: la IA ejecuta, la persona juzga. Delegar también el juicio es el punto donde este modo de trabajo tiene más probabilidades de fallar.

---

## Lista del entorno

| Categoría | Herramienta | Descripción |
|-----------|-------------|-------------|
| Sesión persistente | tmux | El proceso corre en segundo plano, con acceso desde múltiples dispositivos |
| Control remoto | Claude Code v2.1.51+ | Suscripción Pro, iniciar con `claude --rc` |
| Móvil | Claude App (iOS / Android) | Acceso desde la página Code, misma sesión que el escritorio |
| Entorno de previsualización | URL accesible desde internet | Requisito previo para verificar resultados en el móvil |
| Permisos del repositorio | GitHub CLI (`gh auth login`) | Requisito previo para que Claude opere el CI/CD |
| Permisos del servidor | SSH sin contraseña | Requisito previo para que Claude opere el servidor remotamente |
| Teclado | Teclado de WeChat / Teclado de Doubao | Alta precisión en mezcla de idiomas, alternativa a la voz nativa de Claude |

---

Volviendo a la pregunta del principio: tarde de fin de semana, tumbado en el sofá, una taza de café, ¿puedes escribir el código y desplegarlo en producción así?

La respuesta es sí. Pero dicho con más precisión: lo que este método cambia no es dónde trabajas, sino cuándo puedes empezar a trabajar. En el trayecto al trabajo, en los ratos de espera, en un hotel durante un viaje de negocios — cada momento libre puede usarse para avanzar de verdad en una tarea, no solo para ver mensajes o revisar el estado de algo.

El móvil no va a sustituir al ordenador, igual que el ordenador no sustituyó al papel y el lápiz. Lo que amplía son los límites, no reemplaza la forma de trabajar existente. Lo que realmente cambia es el supuesto de que "solo puedo trabajar sentado delante del ordenador" — ese supuesto ya no se sostiene.

---

**Referencias**
- [Documentación oficial de Claude Code: Remote Control](https://code.claude.com/docs/en/remote-control)
- [Stop losing Claude Code sessions: a tmux primer for mobile devs](https://dev.to/jagafarm/stop-losing-claude-code-sessions-a-tmux-primer-for-mobile-devs-2p48)
- [Claude Code on Your Phone | Builder.io](https://www.builder.io/blog/claude-code-mobile-phone)
