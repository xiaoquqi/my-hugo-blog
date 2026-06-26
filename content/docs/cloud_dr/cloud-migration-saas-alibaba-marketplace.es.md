---
title: Cómo un Producto SaaS de Migración a la Nube se Incorpora al Alibaba Cloud Marketplace
description: "Guía técnica sobre la integración de HyperMotion SaaS en el Alibaba Cloud Marketplace, incluyendo autenticación, permisos RAM y la integración con el sistema de pagos."
slug: how-to-join-cloud-migration-saas-into-aliyun-marketplace
aliases:
  - /2021/12/01/%E4%BA%91%E8%BF%81%E7%A7%BBsaas%E5%A6%82%E4%BD%95%E5%85%A5%E9%A9%BB%E9%98%BF%E9%87%8C%E4%BA%91%E5%B7%A5%E5%85%B7%E5%BA%94%E7%94%A8%E5%B8%82%E5%9C%BA/
date: 2021-12-01T09:08:17+08:00
draft: false
author: Ray Sun
tags:
  - Alibaba Cloud
  - HyperMotion
  - Migración a la Nube
  - Recuperación ante Desastres en la Nube
---

HyperMotion SaaS es una plataforma SaaS de migración a la nube y DR en la nube desarrollada bajo la filosofía Cloud Native. En julio de 2020, la versión de migración de HyperMotion se incorporó oficialmente al Alibaba Cloud Marketplace. Después de iniciar sesión en Alibaba Cloud, los usuarios pueden usar el producto directamente en modo SaaS sin necesidad de lanzar una instancia desde el marketplace de la nube. Dado que el sistema está completamente integrado con la gestión de usuarios, la autorización RAM y los sistemas de pago de Alibaba Cloud, la experiencia del usuario es mucho más fluida. Gracias a la ventaja de tráfico de Alibaba Cloud, HyperMotion SaaS acumuló cerca de 400 clientes a través de tráfico orgánico solamente en su primer año en el marketplace, sin campañas especiales de promoción o marketing. El Alibaba Cloud Marketplace es sin duda la mejor encarnación de la filosofía "ser integrado" de Alibaba Cloud, proporcionando un terreno fértil para el software SaaS de IaaS. Este artículo comparte el proceso completo de incorporación al Alibaba Cloud Marketplace desde una perspectiva técnica.

<!-- more -->

## Experiencia del Usuario

### Cómo Se Siente Usarlo

Veamos primero cómo los usuarios interactúan con el producto después de que se incorpora al Alibaba Cloud Marketplace.

![2021-12-01-10-53-53](/images/2021-12-01-10-53-53.png)

Los usuarios entran al producto sin ninguna instalación y van directamente al flujo de uso.

![2021-12-01-11-03-51](/images/2021-12-01-11-03-51.png)

### Flujo de Compra

Dado que el sistema está completamente integrado con el sistema de pago de Alibaba Cloud, los usuarios pueden pagar y adquirir el producto directamente.

![2021-12-01-11-18-07](/images/2021-12-01-11-18-07.png)

### Provisión de Permisos

Cuando los usuarios compran el producto, Alibaba Cloud pre-configura todos los permisos RAM requeridos para el uso del producto de acuerdo con los requisitos de la aplicación. Esto reduce la carga de configuración del cliente y ofrece una verdadera experiencia lista para usar.

## Valor de Incorporarse al Marketplace

¿Por qué entonces incorporarse al Alibaba Cloud Marketplace, y cómo beneficia al negocio?

### Ventaja 1: Valor de Mercado

Ya sea para productos de migración a la nube o de DR en la nube, nuestro desarrollo siempre ha estado guiado por la filosofía Cloud Native, y lograr que estos dos productos se integren profundamente con una plataforma de nube ha sido el mayor objetivo de todo el equipo. Anteriormente habíamos intentado comunicarnos en profundidad con Alibaba Cloud a través de múltiples canales, pero por diversas razones esos esfuerzos nunca llegaron a nada. El modelo del Alibaba Cloud Marketplace resultó ser exactamente lo que necesitábamos. Al mismo tiempo, que nuestro producto sea reconocido por Alibaba Cloud y se incorpore exitosamente al marketplace es el mayor reconocimiento y respaldo tanto para la empresa como para el equipo de I+D.

### Ventaja 2: Tráfico de Clientes

La consola de Alibaba Cloud es una enorme entrada de tráfico, y ese tráfico incluye una gran proporción de valiosos usuarios empresariales. Asegurar una presencia visible en la consola de esta manera es sin duda un enorme canal para la promoción del producto. Pronto lanzaremos formalmente nuestra plataforma de DR Cloud Native, que también se incorporará al Alibaba Cloud Marketplace. Esperamos colaborar con más equipos de negocio de Alibaba Cloud para promover conjuntamente nuestros productos y ganar la confianza de más clientes.

### Ventaja 3: Agilizar el Proceso de Adquisición

En el mercado empresarial, la adquisición es a menudo un proceso extremadamente engorroso. Al integrarse completamente con el flujo de pago de Alibaba Cloud, ahorramos a las empresas su overhead de adquisición y permitimos que los equipos de negocio tomen y ejecuten decisiones más rápidamente. A continuación se muestra una comparación entre el flujo de adquisición tradicional y el flujo de adquisición del Alibaba Cloud Marketplace:

![2021-12-01-14-37-06](/images/2021-12-01-14-37-06.png)

## Cronograma Clave y Costos

Comenzamos conversaciones iniciales con el equipo del Alibaba Cloud Marketplace en febrero de 2020. En marzo, mantuvimos conversaciones separadas con los equipos de arquitectura y seguridad relevantes para planificar la arquitectura de etapa temprana, revisamos las especificaciones de desarrollo front-end y de API, y proporcionamos un entorno de prueba para el trabajo de desarrollo posterior.

Como el equipo de I+D ya tenía un calendario de desarrollo comprometido, el desarrollo formal no comenzó hasta mediados y finales de abril. A principios de abril, solo finalizamos el estilo de página y la experiencia de usuario con el equipo front-end de Alibaba Cloud. El ciclo de I+D fue de aproximadamente un mes y cubrió:

* Desarrollo de la UI según las especificaciones de diseño de Alibaba Cloud
* Ajuste de todas las interfaces API para cumplir con las especificaciones de desarrollo de Alibaba Cloud, y actualización del front-end para conectarse a las nuevas interfaces
* Integración con el marketplace
* Ajuste de políticas de seguridad, incluyendo el agente del lado del origen y las políticas de grupos de seguridad
* Modificación del SDK para cumplir con los requisitos de autorización del Alibaba Cloud Marketplace
* Mover la parte de programación de API del agente de sincronización de datos original para la plataforma de nube de vuelta al lado del servidor para cumplir con los requisitos de seguridad

Desde principios de junio hasta el lanzamiento final el 10 de julio, ajustamos nuestro pipeline CI/CD (HyperMotion se clasifica como un producto de herramientas pero cubre un amplio alcance y tiene una compilación compleja: un artículo dedicado lo cubrirá más adelante) y realizamos pruebas finales de extremo a extremo, saliendo a producción el 10 de julio.

### Lo Que Ganamos del Producto

Durante esta integración, las conversaciones en profundidad con varios equipos de Alibaba Cloud fueron muy valiosas. Desde una perspectiva de seguridad del producto, los equipos hicieron sugerencias constructivas que nos ayudaron enormemente a mejorar la seguridad de nuestro propio producto. Adicionalmente, este proceso nos llevó a reexaminar nuestro pipeline CI/CD, proporcionando una excelente referencia para soportar mejor lanzamientos de múltiples versiones en el futuro.

## Detalles de la Integración Técnica

### Arquitectura General

El plano de control de HyperMotion está construido sobre el framework de microservicios asíncronos de OpenStack y adopta un modelo de implementación en contenedores. Puede implementarse en una sola máquina o en un clúster de Kubernetes. El diagrama de arquitectura general es el siguiente:

![2021-12-01-13-37-04](/images/2021-12-01-13-37-04.png)

Este es el diagrama de arquitectura completo para la integración ISV de Alibaba Cloud:

![2021-12-01-13-38-15](/images/2021-12-01-13-38-15.png)

Los módulos backend están implementados en un clúster de Kubernetes. Como nuestro escenario también incluye funciones como descargas de agentes, solicitamos adicionalmente recursos de almacenamiento de objetos.

### Interfaz de Usuario

Para mantener consistencia visual con Alibaba Cloud, el equipo front-end de Alibaba Cloud nos proporcionó un conjunto completo de especificaciones de diseño front-end.

![2021-12-01-13-41-20](/images/2021-12-01-13-41-20.png)

Aunque HyperMotion admite migración entre múltiples nubes, se personalizó una versión dedicada de Alibaba Cloud específicamente para el marketplace (como se muestra al principio de este artículo).

Integrarse en el ecosistema front-end de Alibaba Cloud también requiere cierta configuración adicional. Para Vue 3.0, se deben agregar las siguientes opciones en `vue.config.js`:

![2021-12-01-13-46-23](/images/2021-12-01-13-46-23.png)

### Capa de API

Por razones de seguridad, no podíamos usar nuestro framework de API existente; en cambio, necesitábamos re-encapsular nuestras interfaces según las especificaciones de API de Alibaba Cloud.

Según los requisitos de la especificación, todas las llamadas a nuestros propios servicios utilizan la interfaz GET, definida de la siguiente manera:

```
GET http://${isv_ip}/api/${action}?userinfo=${userinfo}&accessToken=${accessToken}&params=${params}&traceId=${traceId}
```

El trabajo de modificación de la API fue relativamente pesado en el lado de I+D, requiriendo cambios tanto en el front-end como en el back-end simultáneamente. Como HyperMotion siguió estrictamente la filosofía de desarrollo de microservicios durante su desarrollo, los cambios no fueron difíciles: simplemente fue cuestión de agregar una capa delgada de encapsulación alrededor de las interfaces.

### Ajustes de Seguridad

Después de una estrecha colaboración con el equipo de seguridad de Alibaba Cloud, finalmente realizamos ajustes en las siguientes dos áreas:

#### Dirección de Comunicación

Antes de incorporarnos a Alibaba Cloud, para garantizar la eficiencia de comunicación, nuestro producto utilizaba un modelo de comunicación bidireccional entre el host del lado del origen (por ejemplo, una máquina física) y el plano de control. El plano de control también usaba un modelo de envío unidireccional cuando operaba la pasarela de sincronización de nube (una VM en la nube dentro del inquilino de Alibaba Cloud). De acuerdo con los requisitos de política de seguridad de Alibaba Cloud, la red donde reside nuestro servicio debe estar estrictamente aislada del mundo exterior: incluso si la VM en la nube del usuario es una VM de Alibaba Cloud, no está permitido iniciar conexiones entrantes. Por lo tanto, cambiamos toda la comunicación entre el plano de control y los hosts del lado del origen y las pasarelas de sincronización de nube para que sea unidireccional (iniciando hacia arriba a nuestro plano de control), satisfaciendo los requisitos de seguridad.

#### Seguridad de la Interfaz

Cuando los usuarios usan el producto, necesitan implementar un programa agente en el host del lado del origen o dentro de la plataforma de virtualización, lo que requiere una descarga. El enfoque original no tenía un mecanismo de seguridad suficientemente robusto y podría potencialmente permitir un registro no autorizado. Siguiendo el consejo del equipo de seguridad de Alibaba Cloud, adoptamos un enfoque basado en claves para cifrar información crítica, evitando que la información sea descifrada y también previniendo operaciones no autorizadas y peligrosas.

### Lanzamiento y Puesta en Producción

El proceso de compilación de HyperMotion se divide en dos partes principales: compilaciones de Agent y compilaciones de contenedores. Debido a que están involucrados muchos sistemas operativos (Linux/Windows) y versiones de kernel, la compilación del Agent es relativamente compleja. La compilación de contenedores es comparativamente sencilla. Según los requisitos de puesta en producción, consolidamos todas las compilaciones en la plataforma DevOps de Alibaba Cloud (Yunxiao), colocamos todos los artefactos en el repositorio de artefactos designado, y luego el equipo de Alibaba Cloud completó el proceso de puesta en producción actualizando el entorno de Kubernetes.

## Sugerencias de Mejora

El Alibaba Cloud Marketplace también es un equipo relativamente nuevo dentro de Alibaba Cloud. Hubo bastantes puntos problemáticos durante el proceso de integración real. Fuimos de los primeros clientes semilla: que yo sepa, muchas empresas que intentaron la integración finalmente optaron por abandonar. Las principales razones son las siguientes:

1. **No se proporcionó un entorno separado de desarrollo y prueba.** Aunque Alibaba Cloud proporcionó un entorno de prueba al principio, en realidad era el entorno de producción final. Una vez que el sistema entró en producción, no tuvimos ninguna otra plataforma disponible para depuración. Si bien se pueden usar iteraciones rápidas para corregir errores en producción, para un software comercial riguroso, especialmente uno que involucra datos de usuarios, preferiríamos mucho tener tiempo suficiente para pruebas exhaustivas antes del lanzamiento.

2. **No se proporcionó un punto de entrada de operaciones.** Actualmente, si surgen problemas en el entorno en vivo, debemos depender del enlace de Alibaba Cloud para extraer registros en nuestro nombre. No podemos localizar problemas rápidamente por nuestra cuenta, lo que alarga el tiempo para resolver incidentes.

3. **El costo de modificar el sistema existente es demasiado alto.** Del proceso de integración descrito anteriormente, los cambios requeridos en la capa de API son un desafío no trivial para muchas empresas.

4. **La referencia de tráfico no es suficientemente prominente.** A pesar de múltiples rediseños para atraer tráfico al Alibaba Cloud Marketplace, muchos clientes aún lo desconocen por completo. Al mismo tiempo, el equipo del Alibaba Cloud Marketplace colabora demasiado poco con otros equipos internos. Recomendamos más iniciativas conjuntas de promoción con los equipos de negocio para llegar a más clientes.

A pesar de las muchas áreas que aún vale la pena mejorar en el Alibaba Cloud Marketplace, como pionero en el ecosistema de computación en la nube de China que defiende la filosofía "ser integrado" y proporciona un entorno de competencia justa para los socios del ecosistema, esperamos continuar avanzando juntos con Alibaba Cloud.
