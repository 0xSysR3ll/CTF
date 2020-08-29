Pour ce deuxième épisode, les trames contenus dans la capture ne sont que de type `HTTP` et semblent vouloir brouiller nos pistes. En effet il s'agit de requête vers des répertoires inexistants.

Extrait :

<pre>
6	0.409621	127.0.0.1	127.0.0.1	HTTP	170	GET /randomfile1 HTTP/1.1 
10	0.412286	127.0.0.1	127.0.0.1	HTTP	513	HTTP/1.0 404 File not found  (text/html)
19	0.413073	127.0.0.1	127.0.0.1	HTTP	165	GET /frand2 HTTP/1.1 
23	0.438550	127.0.0.1	127.0.0.1	HTTP	513	HTTP/1.0 404 File not found  (text/html)
32	0.451770	127.0.0.1	127.0.0.1	HTTP	160	GET /0 HTTP/1.1 
36	0.469019	127.0.0.1	127.0.0.1	HTTP	513	HTTP/1.0 404 File not found  (text/html)
45	0.470248	127.0.0.1	127.0.0.1	HTTP	161	GET /00 HTTP/1.1 
49	0.471868	127.0.0.1	127.0.0.1	HTTP	513	HTTP/1.0 404 File not found  (text/html)
57	0.472592	127.0.0.1	127.0.0.1	HTTP	161	GET /01 HTTP/1.1 
61	0.497444	127.0.0.1	127.0.0.1	HTTP	513	HTTP/1.0 404 File not found  (text/html)
70	0.498419	127.0.0.1	127.0.0.1	HTTP	161	GET /02 HTTP/1.1 
</pre>

Cependant, à la tout fin, on retrouve encore un objet, mais cette foi-ci c'est un fichier `confidentiel.zip`

Même procédure que dans l'épisode 1 pour extraire le fichier.
Pour dézipper le fichier, il faut un mot de passe.

Il se trouve qu'en explorant les objets http, on tombe sur un fichier `secret.txt` qui contient le mot de passe de cette archive.

<pre>\__    _/(  ___  )\__   __/( (    /|       (  ____ \(  ____ \( (    /||\     /|(  ___  )(  ____ \| \    /\
   )  (  | (   ) |   ) (   |  \  ( |       | (    \/| (    \/|  \  ( || )   ( || (   ) || (    \/|  \  / /
   |  |  | |   | |   | |   |   \ | | _____ | (__    | (_____ |   \ | || (___) || (___) || |      |  (_/ / 
   |  |  | |   | |   | |   | (\ \) |(_____)|  __)   (_____  )| (\ \) ||  ___  ||  ___  || |      |   _ (  
   |  |  | |   | |   | |   | | \   |       | (            ) || | \   || (   ) || (   ) || |      |  ( \ \ 
|\_)  )  | (___) |___) (___| )  \  |       | (____/\/\____) || )  \  || )   ( || )   ( || (____/\|  /  \ \
(____/   (_______)\_______/|/    )_)       (_______/\_______)|/    )_)|/     \||/     \|(_______/|_/    \/

ou JOIN-ESNHACK

</pre>

Dans l'archive, le flag est en clair dans une image, encore une fois.
