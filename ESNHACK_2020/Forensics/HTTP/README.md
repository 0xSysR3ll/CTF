Même principe que les challenges Exfiltration de données.

Dans les trames de la capture Wireshark, on observe une requête http vers un fichier `flag.txt`.

Extrait :

<pre>
No.	Time	Source	Destination	Protocol	Length	Info
50	368.555598178	192.168.13.254	192.168.13.126	HTTP	144	GET / HTTP/1.1 
64	368.557619612	192.168.13.126	192.168.13.254	HTTP	280	HTTP/1.0 200 OK  (text/html)
72	384.452869896	192.168.13.254	192.168.13.126	HTTP	215	GET /flag.txt HTTP/1.1 
76	384.453477666	192.168.13.126	192.168.13.254	HTTP	268	HTTP/1.0 200 OK  (text/plain)
</pre>

On essaye alors d'extraire ce fichier en passant par :
<pre>File > Export Objects > HTTP </pre>

Dans ce fichier, est contenu le flag en clair :
<pre>ESNHACK{H77P_i5_no7_v3ry_s3cur3}</pre>

