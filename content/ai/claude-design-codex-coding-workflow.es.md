---
title: "Claude Design para pensar el producto, Codex para llevarlo al código"
description: "Tras perder el acceso a Claude Code, pasé dos días programando más con Codex. La experiencia me ayudó a entender qué aporta cada agente y cuánto cuesta cambiar de herramienta a mitad del trabajo."
date: 2026-09-29T08:00:00+08:00
slug: "claude-design-codex-coding-workflow"
author: Ray Sun
categories:
  - Práctica con herramientas de IA
tags:
  - Claude Code
  - Claude Design
  - Codex
  - Programación con IA
  - Diseño de producto
draft: false
---

Hace un par de días suspendieron mi cuenta de Claude Code de forma inesperada. Todavía no tengo claro el motivo. Como no podía usarlo, recurrí a Codex con mucha más frecuencia para desarrollar, y ese cambio me hizo ver con más claridad las diferencias entre ambos agentes de programación.

Antes de entrar en materia, una aclaración: uso ChatGPT a diario. Aquí hablo **de mi experiencia con Claude Code y Codex al desarrollar software**, no de una comparación general entre ChatGPT y Claude.

<!-- more -->

## Claude Design piensa en el producto

La diferencia que más noto está en el diseño. Claude Design tiene más criterio de producto que Codex.

Trabajar con él se parece menos a pedirle a una herramienta que genere una interfaz y más a colaborar con alguien con experiencia en gestión de producto. Piensa en cómo encaja cada pantalla en el conjunto y después baja al detalle. Si un campo de entrada tiene nueve estados relevantes, los desarrolla todos y explica por qué ha diseñado cada uno de esa manera.

{{< figure src="/images/claude-design-codex-coding-workflow/interaction-states.png" alt="Especificación de una pantalla de inicio de sesión con distintos estados de botones, campos de entrada y mensajes" caption="El diseño contempla los estados de interacción, no solo el aspecto inicial de la pantalla." >}}

La distinción importa. Una página vistosa no es necesariamente un producto bien resuelto. En mi experiencia, Claude Design a veces propone soluciones más completas que algunas que he visto de diseñadores experimentados, con detalles que a mí ni siquiera se me habían ocurrido.

## Distinto ritmo, resultados parecidos

Codex se comporta más como un ingeniero: le das una tarea, se pone manos a la obra, entrega una primera versión funcional y la mejora sobre la marcha. Claude Code tiende a conversar antes sobre el objetivo, las restricciones y la forma de abordar el trabajo.

Puede que el código final no sea muy distinto. Lo que cambia de verdad es el ritmo: **Codex avanza rápido; Claude Code dedica más tiempo a comprobar que va en la dirección correcta.**

En el desarrollo asistido por IA, escribir código suele ser la parte barata. Lo caro es descubrir que tomaste el camino equivocado y tener que rehacerlo. Por eso valoro cada vez más la reflexión previa de Claude Code cuando se trata de un módulo nuevo, un rediseño o una refactorización importante. Una vez definida la dirección, Codex es muy eficaz llevando la implementación hasta el final.

## La combinación que hoy me funciona

Por ahora, una división del trabajo bastante práctica es **usar Claude Code como diseñador y Codex como desarrollador**.

Puedo recurrir a Claude Design para definir la estructura de la página, los estados, las interacciones y las razones detrás de cada decisión, y después encargarle la implementación a Codex. En un proyecto existente funciona especialmente bien: Claude Design estudia el código actual y plantea el rediseño de la interfaz; Codex lo integra en la arquitectura que ya existe.

Aun así, si mi cuenta funcionara y tuviera suficiente capacidad en la suscripción, preferiría no cambiar de herramienta tan a menudo. En un desarrollo real, el contexto importa. Los requisitos, las decisiones de diseño, la implementación, la depuración y la refactorización forman una conversación continua. Cada traspaso obliga a reconstruir parte de ese contexto, y pueden perderse ideas que nunca llegaron a quedar por escrito.

Por eso, esta combinación de Claude Design y Codex me resulta útil dadas mis circunstancias actuales, pero no es mi flujo de trabajo ideal.

## El criterio sigue siendo nuestro

Use el agente que use, la calidad máxima del resultado sigue dependiendo de cuánto haya pensado yo el problema. La IA puede acelerar la ejecución y sugerir ideas que quizá se me habrían escapado. No puede decidir por mí si persigo el objetivo adecuado ni si estoy haciendo las concesiones correctas.

**La IA debe ayudar a las personas, no al revés.**
