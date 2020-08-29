Dans ce challenge, il s'agit de trouver un `secret` caché par un dénommé Elliot.
On attéri sur un site web fait uniquement en html. On écarte alors tout de suite les attaques CRSS, XSS, CRSF, etc.
Je pense qu'on chercher plutôt un fichier ou répertoire caché car il y a beacoup trop de contenu/liens. Autant chercher une aiguille dans une bôte de foin...

Comme tout bon pirate, j'utilise `dirbuster` pour balayer tous les répertoire du site.
Après quelques minutes, je tombe sur un fichier `secret/secret.zip`. 
Evidemment, cela aurait été trop facile de dézipper cette archive sans qu'elle soit protégée par un mot de passe.

Encore une fois, il me semblait peut probable que le mot de passe soit caché sur le site, je décide donc d'utiliser `fcrackzip` avec le dictionnaire `rockyou.txt` pour faire un bruteforce du mot de passe.
Après quelques secondes seulement, le mot de passe tombe.

L'achive dézippée, le mot de passe n'apparaît évidemment pas en clair, trop facile !
On se retrouve avec 65 photos JPG...

Premier réflexe, un petit `exiftool` des images pour véfifier si le flag ne serait pas à l'intérieur.
Comme il y a 65 photos, je décide de toutes les vérifier en même temps au niveau du champs `Comment:`

<pre>$exiftool ./*.JPG | grep 'Comment'</pre>

En fait, la première lettre de chaque commentaire constituait une lettre du flag.
<pre>ESNHACK{d0_n07_und3r3571m473_7h3_r0b075_7x7_f1l3}</pre>

Fier car ce challenge a été réalisé 6 minutes avec la fin du CTF et nous sommes les seuls à l'avoir validé.
