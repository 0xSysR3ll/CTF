Episode 1 du challenge Vol de données.
Ces challenges consistent en l'analyse de fichiers de capture <a href="https://fr.wikipedia.org/wiki/Wireshark">Wireshark</a>

En explorant les trames wireshark, on observe des trames de type `TCP` et `HTTP`.
Les trames TCP ne vont pas nous intéresser car elles sont trop nombreuses.
Appliquant un filtre http, on remarque que les trames `n°48` et `n°63` mettent en avant une images.

<pre>11	2.871716	127.0.0.1	127.0.0.1	HTTP	120	GET / HTTP/1.1 
15	2.873372	127.0.0.1	127.0.0.1	HTTP	388	HTTP/1.0 200 OK  (text/html)
48	13.724797	127.0.0.1	127.0.0.1	HTTP	194	GET /poutine.jpg HTTP/1.1
63	13.744728	127.0.0.1	127.0.0.1	HTTP	49	HTTP/1.0 200 OK  (JPEG JFIF image)</pre>

Avec wirehark il est possible d'extraire les ojects interceptés par la capture.
Pour ça on va dans <pre>File > Export Objects > HTTP</pre>

On y retrouve notre `poutine.jpg` qui contient évidemment le flag en clair sur l'image.
