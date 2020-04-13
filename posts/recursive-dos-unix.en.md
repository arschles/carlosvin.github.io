---
title: "Convert files formats: Windows to Unix"
lang: en
date: 2016/02/12 10:34:00
tags: Useful Commands, Unix, Windows
description: Convert Windows formatted files to Unix format per directory recursively
type: micro
---

If you are developing from a Windows environment to a Unix target
environment, most likely you have had this issue: You install source
files in Windows format in your Unix environment.

There is a way quite simple to convert all your files from Windows to
Unix format:

``` {.bash}
find . -type f -print0 | xargs -0 dos2unix
```

I got it, of course, form <https://stackoverflow.com/questions/11929461/how-can-i-run-dos2unix-on-an-entire-directory>