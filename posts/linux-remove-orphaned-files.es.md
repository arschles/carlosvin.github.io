---
title: Eliminar paquetes huérfanos en Linux

lang: es

date: 2012/10/02 13:30:02

update: 2014/03/28 10:00:00

tags: Linux, Archlinux, Debian, Tips and Tricks

description: Cómo eliminar los paquetes que se han instalado automáticamente y
    que ya no se utilizan

type: text
---

Cuando instalamos un paquete en las distribuciones Linux (en las que yo
conozco), se instalan otros paquetes (dependencias). Si en el futuro
desinstalas ese paquete, esas dependencias quedarán instaladas en el
sistema, aunque no serán usadas por nadie, simplemente ocuparán espacio
en disco. Estas dependencias son llamadas paquetes huérfanos.

::: {.contents}
Desinstalar paquetes huérfanos
:::

[Archlinux](https://archlinux.org/)
===================================

Cuando instalamos un paquete en Archlinux `pacman -S nombre_paquete` se
nos descargan automáticamente las dependencias de este paquete. Esto
resulta muy cómo, pero cuando eliminamos el paquete que instalamos con
`pacman -R nombre_paquete`, se nos quedan instaladas las dependencias de
éste. Para evitar ésto, podemos desinstalar los paquetes con
`pacman -Rscn nombre_paquete`, pero si preferimos desinstalar
normalmente solo con la opción -R, después podemos eliminar todos los
paquetes huérfanos de la siguiente forma:

``` {.bash}
pacman -Rsn $(pacman -Qdtq)
```

El funcionamiento es muy sencillo:

-   la sentencia `pacman -Qdt` da un listado de todos los paquetes
    huérfanos
-   `pacman -Rsn` elimina los paquetes listados

[Debian](https://debian.org/)
=============================

En distribuciones basadas en [Debian](https://debian.org/), pasa lo
mismo que en [Archlinux](https://archlinux.org/) (bueno para ser justos
en [Archlinux](https://archlinux.org/) pasa lo mismo que en
[Debian](https://debian.org/), un respeto a la edad). Para eliminar
estos paquetes, que solamente están ocupando espacio en disco,
simplemente hay que ejecutar el siguiente comando.

``` {.bash}
apt-get remove --purge $(deborphan)
```