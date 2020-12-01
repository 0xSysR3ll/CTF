# ChatTCP

### Description

Trouver le flag caché dans cette communication !

### Solution

En ouvrant le fichier de capture wireshark, on observe quelques échanches TCP.

Contenu de l'échange en clair :
```
Hi !
Hello
Tu as le flag ?
Ouais 2sec
IfspDUG{dibu_xjui_ofudbu}
Merci
```
Il semblerait que `IfspDUG{dibu_xjui_ofudbu}` soit le flag mais encodé.

Je décide d'essayer avec du ROT.

Arrivé au ROT 25 : `HeroCTF{chat_with_netcat}`
