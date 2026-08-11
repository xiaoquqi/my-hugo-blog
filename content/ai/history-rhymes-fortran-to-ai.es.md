---
title: "La historia rima: hace 70 años, tampoco confiábamos en que las máquinas escribieran buen código"
description: "Hace setenta años, los programadores tampoco confiaban en que los compiladores generaran código utilizable. La crisis de confianza actual en torno al código escrito por IA es casi la misma historia repitiéndose. Desde el origen de FORTRAN hasta el cambio organizacional impulsado por los costos y el surgimiento de la ingeniería de software como disciplina propia, la historia ya nos ha dado la respuesta."
author: Las Reflexiones de Lao Sun
date: 2026-08-10T08:00:00+08:00
categories:
  - Perspectivas del sector IA
tags:
  - IA
  - Ingeniería de Software
  - FORTRAN
  - Compiladores
draft: false
---

{{< figure src="/images/history-rhymes-fortran-to-ai/cover-machine-reliable.webp" alt="Programador de los años 50 revisando con lupa la cinta perforada que sacó el compilador, entre un check y un signo de interrogación; programador de los 2020 mirando código generado por IA con su propio signo de interrogación — la misma pregunta, setenta años después" caption="Años 50 vs. años 2020: ¿de verdad podemos confiar en lo que escribió la máquina?" >}}

## 01 · La IA puede escribir código, pero ¿de verdad confiamos en él?

Hay una contradicción curiosa en la comunidad de programadores en este momento: todo el mundo no puede dejar de usar IA para escribir código, y al mismo tiempo se queja de la avalancha de código generado por IA que nadie ha entendido ni verificado de verdad.

Comunidades de código abierto como Rust, LLVM y Godot han empezado a plantear la misma preocupación, y "AI slop" (basura generada por IA) se ha convertido en un término habitual para describirlo.

Así que el verdadero debate hoy no es si la IA puede escribir código. Es este:

> **¿Confiamos de verdad lo suficiente en lo que escribe la IA como para lanzarlo a producción?**

Cada vez más gente llega a la misma respuesta: la IA puede escribir el código, pero alguien tiene que poder leerlo, revisarlo, verificarlo y, al final, responder por el resultado.

Y aquí está lo interesante: hace casi 70 años, los programadores vivieron una crisis de confianza casi idéntica, con el compilador.

---

## 02 · Hace 70 años, lo caro de verdad era la traducción manual

En la década de 1950, escribir un programa no se parecía en nada a como es hoy.

Supongamos que querías hacer algo simple: sumar A y B, y si el resultado era mayor que 100, pasar al siguiente paso.

Hoy, eso es sencillo de escribir:

```
C = A + B

if C > 100:
    do_something()
```

En una computadora de esa época, lo que un programador realmente tenía que escribir se parecía más a esto:

```
CLA A
ADD B
STO C
SUB HUNDRED
TPL NEXT
```

Los programadores no solo expresaban lógica: tenían que saber exactamente dónde vivían los datos en memoria, qué instrucciones soportaba la máquina y cómo funcionaba cada una. Cambiar de máquina significaba volver a aprender y reescribir buena parte de todo eso desde cero.

Así que en esa época, los programadores pasaban la mayor parte de su tiempo no en "qué problema estoy resolviendo", sino en:

> Traducir una idea humana a las acciones exactas que una máquina concreta podía ejecutar.

Ese es el contexto económico del que surgió FORTRAN. John Backus recordaría después que, en aquel momento, el costo de los programadores de un centro de cómputo solía ser ya comparable al costo de la propia computadora, y la máquina todavía pasaba entre un cuarto y la mitad de su tiempo depurando programas.

Las computadoras eran cada vez más rápidas. Las personas se convirtieron en el cuello de botella.

{{< figure src="/images/history-rhymes-fortran-to-ai/manual-translation-to-compiler.webp" alt="Programador de los años 50 traduciendo a mano ADD A+B a tarjetas de instrucciones LOAD/ADD/STORE/JUMP; programador de los 60 en adelante solo escribe C=A+B y deja que el compilador saque el binario automáticamente" caption="De la traducción manual a dejar que el compilador la haga automáticamente" >}}

---

## 03 · ¿Por qué no dejar que la máquina hiciera su propia traducción?

El verdadero punto de inflexión vino de una pregunta que hoy suena obvia, pero que en su momento era realmente audaz:

> Si los programadores dedicaban todo su tiempo a traducir, ¿por qué no dejar que la computadora hiciera esa traducción por sí misma?

Hacia 1954, John Backus y su equipo en IBM se propusieron construir FORTRAN.

Toda esa cadena de operaciones de bajo nivel ahora podía escribirse de una forma mucho más cercana a como piensa una persona:

```fortran
C = A + B

IF (C .GT. 100) GO TO 20
```

El programador solo tenía que expresar lo que quería calcular.

Generar las instrucciones de máquina, leer los datos, manejar los saltos: todo eso ahora era trabajo del compilador.

La división del trabajo entre humano y máquina cambió:

> **El trabajo de la persona es expresar la intención. El trabajo de la máquina es traducirla en código que pueda ejecutar.**

---

## 04 · En aquel entonces, los programadores tampoco confiaban en la máquina

Los programadores profesionales no se lo creyeron al principio.

Y, honestamente, ese escepticismo tenía sentido.

Los primeros sistemas de programación automática solían producir código que simplemente no era lo bastante rápido. Las computadoras eran tan caras en aquel entonces que, si el código generado corría notablemente más lento que lo que escribía a mano un programador experto, toda la idea perdía sentido.

Así que la pregunta que el equipo de FORTRAN realmente tenía que responder no era "¿podemos generar código automáticamente?", sino:

> ¿Podía el código generado por la máquina ser lo bastante bueno como para que un programador profesional confiara de verdad en él?

{{< figure src="/images/history-rhymes-fortran-to-ai/we-shipped.webp" alt="Programador de 1957 sosteniendo la cinta que sacó el compilador de FORTRAN, preguntando con dudas '¿esto funciona de verdad? ¿lo lanzamos así?'; programador de 2026 viendo a Codex terminar de correr las pruebas, gritando '¿pasaron las pruebas? ¡a producción!'" caption="Entonces: no lo sabíamos. Pero lo lanzamos igual." >}}

Al final, lo lograron. La generación de código de FORTRAN I estaba lo bastante optimizada como para competir con lo que escribiría a mano un buen programador.

Hoy nos hacemos una versión de la misma pregunta sobre la IA: puede escribir el código, pero ¿se puede entender lo que escribe, verificarlo, mantenerlo con el tiempo, y hay alguien dispuesto a responder por ello?

Hace setenta años, estábamos construyendo confianza en el compilador.

Hoy, estamos construyendo confianza en la IA.

---

## 05 · Cuando una tecnología demuestra su valor, las organizaciones cambian

Lo que realmente cambió las cosas no fue solo que el compilador madurara como tecnología, sino que demostrara su valor económico.

El primer compilador de FORTRAN salió en 1957. Los números mostraron que había reducido los costos de programación y depuración a aproximadamente una cuarta parte de lo que eran antes.

Para una empresa, eso ya no era solo una nueva pieza de tecnología: era una forma genuinamente más eficiente de producir software.

Una encuesta realizada en abril de 1958 a 26 sitios con IBM 704 encontró que más de la mitad ya usaba FORTRAN para más de la mitad de su carga de trabajo, y en muchos de ellos el uso de FORTRAN ya superaba el 80%.

Del primer intento en 1954, a algo realmente utilizable en 1957, a una adopción rápida en 1958: todo el proceso tomó apenas unos años.

Lo que de verdad vale la pena notar aquí es que lo que impulsaba el cambio ya no eran las preferencias individuales de los programadores. El costo y la eficiencia habían entrado en las decisiones de la dirección.

> **Cuando una tecnología deja de tratarse de si es agradable de usar y empieza a tratarse de si prescindir de ella perjudica tus costos y tu competitividad, el cambio organizacional ocurre rápido.**

{{< figure src="/images/history-rhymes-fortran-to-ai/value-to-business-adoption-en.webp" alt="La tecnología surge, los ingenieros la evalúan, el valor se valida, el negocio decide, la adopción escala, la industria acelera: programadores de los años 50 dudando si el compilador de verdad supera al código manual, adoptándolo después de comprobar el ahorro en costos y la mejora en eficiencia; equipo de los 2020 mirando los datos de AI coding —tiempo de desarrollo -60%, esfuerzo de ingeniería -50%, velocidad de entrega +80%— y adoptándolo en toda la organización" caption="La tecnología crea la posibilidad. El valor impulsa la adopción. El negocio escala el futuro." >}}

El ensamblador no desapareció. Pero cada vez menos gente necesitaba escribirlo a mano: la máquina había asumido un trabajo que antes requería que una persona hiciera la traducción.

---

## 06 · Cuando escribir código se vuelve fácil, el criterio de ingeniería es lo escaso

La historia que vino después de FORTRAN ya nos dio una respuesta a esto.

A medida que escribir programas se volvió más fácil, el software no se volvió más simple: se volvió más grande y más complejo. El problema difícil pasó de "cómo escribo este código" a cómo diseñas sistemas, organizas la colaboración, aseguras la calidad y mantienes las cosas a largo plazo.

Para 1968, la ingeniería de software ya se había consolidado como una disciplina propia, tomada en serio como un problema de ingeniería.

Y muchos de los nuevos problemas que creó la automatización terminaron resolviéndose con más automatización: los compiladores necesitaban optimizarse, así que llegó la optimización automática; los programas se volvieron más complejos, así que llegaron el análisis estático, las pruebas automatizadas y toda una familia de herramientas de verificación.

Lo que vence a la magia, casi siempre, es más magia.

Probablemente hoy pase lo mismo. La IA está haciendo que producir código sea cada vez más rápido, pero los nuevos cuellos de botella que crea —calidad, pruebas, verificación— no van a depender para siempre de que alguien lea cada línea a mano. Esos también terminarán automatizándose más.

Así que lo que de verdad va a escasear en el futuro probablemente no sea escribir código, ni siquiera solo revisarlo. Es esto:

> **Definir el problema, entender el negocio, diseñar el sistema, fijar el estándar, evaluar el resultado, y al final responder por él.**

Cada vez que una tecnología democratiza rápidamente alguna capacidad, la verdadera oportunidad suele aparecer en el nuevo problema que deja al descubierto.
