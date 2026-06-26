---
title: Migración de nube privada con HyperMotion SaaS mediante VPN de Alibaba Cloud
date: 2021-02-10 10:35:16
author: Ray Sun
tags:
  - Alibaba Cloud
  - VPN
  - Migración a la nube
  - HyperMotion
categories:
  - Migración a la nube
draft: false
---

HyperMotion SaaS es un servicio de migración basado en la nube que ayuda a las empresas a trasladar rápidamente sus cargas de trabajo desde nubes privadas o centros de datos locales hacia nubes públicas. Este artículo explica cómo utilizar el servicio VPN de Alibaba Cloud para habilitar la migración de entornos de nube privada con HyperMotion SaaS.

<!-- more -->

## Contexto

La arquitectura de HyperMotion SaaS sitúa el plano de control en la nube, mientras que el plano de datos requiere conectividad directa con el entorno de origen. Para las migraciones de nube pública a nube pública, la conectividad de red generalmente no supone un problema. Sin embargo, para las migraciones desde nubes privadas o centros de datos locales, es necesario establecer una conexión de red segura.

Alibaba Cloud VPN Gateway ofrece una manera sencilla de crear una conexión de red cifrada entre un VPC de Alibaba Cloud y un centro de datos local o una nube privada.

## Diseño de la arquitectura

La arquitectura general es la siguiente:

1. HyperMotion SaaS se despliega en Alibaba Cloud
2. El entorno de nube privada de origen se conecta al VPC de Alibaba Cloud a través de Alibaba Cloud VPN Gateway
3. HyperMotion SaaS accede al entorno de origen a través de la red VPC

## Pasos de configuración

### 1. Crear una VPN Gateway de Alibaba Cloud

En la consola de Alibaba Cloud, cree una VPN Gateway:
- Seleccione una especificación de ancho de banda adecuada (se recomienda al menos 100 Mbps)
- Habilite la función IPsec-VPN

### 2. Crear una puerta de enlace de cliente

Configure la información de la VPN Gateway del centro de datos local o la nube privada:
- Introduzca la dirección IP pública del dispositivo VPN local
- Configure la información de enrutamiento del par remoto

### 3. Crear una conexión VPN

Cree una conexión VPN IPsec:
- Seleccione el método de autenticación por clave precompartida (Pre-shared Key)
- Configure los parámetros IKE e IPsec

### 4. Configurar el dispositivo VPN local

Basándose en la configuración de Alibaba Cloud VPN Gateway, configure el dispositivo VPN local (router o firewall) en consecuencia:
- Configure el túnel IPsec
- Configure las políticas de enrutamiento

### 5. Verificar la conectividad de red

Una vez completada la configuración, verifique la conectividad de red entre el VPC de Alibaba Cloud y el entorno local:

```bash
# Hacer ping al servidor local desde una instancia ECS de Alibaba Cloud
ping <ip-servidor-local>

# Hacer ping al ECS de Alibaba Cloud desde el servidor local
ping <ip-ecs>
```

### 6. Configurar HyperMotion SaaS

Una vez establecida la conectividad de red, configure HyperMotion SaaS:
- Agregue los hosts de origen (usando direcciones IP privadas)
- Seleccione la plataforma en la nube de destino
- Inicie la sincronización de datos

## Notas

1. **Planificación del ancho de banda**: El ancho de banda de la VPN afecta la velocidad de la migración de datos. Planifique adecuadamente en función del volumen de datos y la ventana de migración.

2. **Configuración de grupos de seguridad**: Asegúrese de que los grupos de seguridad de Alibaba Cloud permitan el tráfico proveniente de la subred VPN.

3. **Configuración de enrutamiento**: Asegúrese de que la tabla de enrutamiento del VPC de Alibaba Cloud tenga las rutas correctas apuntando a la red local.

4. **Estabilidad de la VPN**: La estabilidad de la conexión VPN afecta la confiabilidad de la migración de datos. Se recomienda encarecidamente realizar pruebas exhaustivas antes de la migración.

## Resumen

Mediante la VPN de Alibaba Cloud, HyperMotion SaaS puede migrar entornos de nube privada de forma segura y eficiente. Este enfoque es fácil de configurar, seguro y confiable, y satisface los requisitos de la mayoría de los escenarios de migración de nube privada.
