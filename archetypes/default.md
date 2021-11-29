---
title: {{ replace  .Name "-" " " | replaceRE "^\\d{4} \\d{2} \\d{2} (.*)" "$1" | title }}
date: {{ .Date }}
draft: true
---

