---
title: Contenedores Docker multi-dominio

date: 2016/11/23 21:00

tags: Docker, Microservices

description: Cómo crear varios contenedores Docker con diferentes dominios en la
    misma máquina.
previewimage: /docker-multidomain/proxy.png
type: text
lang: es
---


::: {.contents}
:::

Caso de Uso
===========

Tenemos varias aplicaciones servidoras a la vez en un mismo entorno de
desarrollo, cada una encapsulada en un contenedor, llamémosles de ahora
en adelante \"Contenedor A\" y \"Contenedor B\".

Utilizando docker estas aplicaciones tienen la misma dirección IP en
nuestra máquina, una forma de distinguirlas es cambiando el puerto que
exponen.

![Aplicaciones exponiendo la misma dirección IP utilizando diferentes
puertos para diferenciar las aplicaciones](/docker-multidomain/ip.png)

-   Si queremos llamar a la \"aplicación A\" haremos algo así: GET
    <http://10.20.30.40:8080/colors/red>
-   Si queremos llamar a la \"aplicación B\" haremos algo así: GET
    <http://10.20.30.40:8081/fruits/tomato>

Pero esto es un poco confuso, ¿8080 sigfica que accedemos a las
\"aplicación A\" y 8081 significa \"aplicación B\"?

Sería mucho más sencillo de recordar algo así:

-   Si queremos llamar a la \"aplicación A\" haremos algo así: GET
    <http://a.domain.com/colors/red>
-   Si queremos llamar a la \"aplicación B\" haremos algo así: GET
    <http://b.domain.com/fruits/tomato>

![Diferenciando aplicaciones por nombre de
dominio](/docker-multidomain/domain.png)

Obtener este valor semántico extra es más sencillo de lo que parece.

Cómo configurar un Proxy Inverso Multi-Dominio
==============================================

Dije que era fácil porque no vamos a tener que hacer casi nada, ya que
otro contenedor hará casi todo el trabajo por nosotros. Vamos a utilizar
[nginx-proxy](https://github.com/jwilder/nginx-proxy), que generará
automáticamente las configuraciones necesarias para
[NGINX](https://www.nginx.com).

::: {.note}
::: {.title}
Note
:::

Puedes descargar el ejemplo completo desde:
<https://github.com/carlosvin/docker-reverse-proxy-multi-domain>
:::

Así que al final no tendremos 2 contenedores, sino también tendremos un
tercero que hará las veces de proxy.

![Los 2 contenedores y el proxy](/docker-multidomain/proxy.png)

Estructura del proyecto de ejemplo
----------------------------------

-   docker-compose.yaml (Archivo con la configuración descrita en la
    imágen previa)
-   a (Directorio para la aplicación A)
    -   Dockerfile (Archivo con la configuración del contenedor A)
-   b (Directorio para la aplicación B)
    -   Dockerfile (Archivo con la configuración del contenedor B)

[Ver proyecto](/listings/docker-reverse-proxy-multi-domain).

Configuración de la arquitectura (docker-compose)
-------------------------------------------------

La parte más importante es la configuración de las relaciones entre los
contenedores.

``` {.yaml}
```

-   En la línea 4 y 10 es donde configuramos el nombre de dominio que
    queremos utilizar para cada aplicación.
-   A partir de la línea 13 configuramos el proxy (esta es la parte de
    copiar y pegar).
-   En la línea 2 y 8 estamos indicando a docker-compose que tiene que
    construir las imágenes dentro del directorio indicado. Por ejemplo,
    en la línea 2, estamos indicando que docker-compose tiene que
    construir la imágen docker utilizando ./a/Dockerfile.

Configuración de la imágen de la aplicación
-------------------------------------------

A continuación vamos a comentar la configuración de la imágen del
contenedor para la aplicación A.

Línea 1: Importamos una imágen con un servidor apache.

Línea 2: Servimos un archivo que muestra \"Host A\" como página por
defecto.

La configuración para la aplicación B, es prácticamente la misma:

Añadiendo los nombres de dominio a tu configuración
---------------------------------------------------

En Linux simplemente tenemos mapear la dirección local a los nombres de
dominio que hayas elegido, en nuestro ejemplo es a.domain.com y
b.domain.com.

``` {.bash .numberLines}
#/etc/hosts
127.0.0.1     localhost.localdomain localhost
::1             localhost6.localdomain6 localhost6
127.0.0.1   a.domain.com
127.0.0.1   b.domain.com
```

Simplemente he añadido las líneas 4 y 5.

¡Todo listo!
------------

Ya solo nos queda probar el ejemplo.

``` {.bash .numberLines}
docker-compose build
docker-compose up
```

Ya están las tres contenedores arrancados.

Ahora podemos abrir nuestro navegador y escribir a.domain.com y nos
mostrará el texto *App A works!*. Si escribimos b.domain.com entonces
veremos *App B works!*.

![a.domain.com en el navegador](/docker-multidomain/a.screenshot.png)

![b.domain.com en el navegador](/docker-multidomain/b.screenshot.png)

::: {.note}
::: {.title}
Note
:::

En la mayoría de distribuciones Linux necesitarás privilegios para
ejecutar los comandos docker (sudo).
:::

lang: es