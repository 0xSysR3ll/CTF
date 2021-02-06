Pas fan de la cryptographie, le challenge était noté `facile` je me lance dans sa résolution.

A disposition, un fichier `encoded.txt` qui contien la chaîne suivante :

<pre>Li4uLi0gLi4uLi4gLi4uLi4gLi4uLS0gLi4uLi0gLiAuLi4uLSAtLS0uLiAuLi4uLSAuLS0tLSAuLi4uLSAuLi4tLSAuLi4uLSAtLi4uIC0tLi4uIC0uLi4gLi4uLS0gLi4uLS0gLi4uLi0gLiAtLi4uLiAuLi4tLSAuLi4tLSAtLS0tLSAtLi4uLiAuLi4uLSAuLi4tLSAuLi4uLSAtLi4uLiAtLS4uLiAuLi4tLSAuLi4tLSAuLi4uLiAuLi0uIC4uLi4uIC0uLi4uIC4uLi0tIC4uLi4uIC4uLi4uIC4uLS4gLS4uLi4gLi4uLS0gLi4uLi0gLS0tLi4gLi4uLS0gLi0tLS0gLS4uLi4gLS4uLi4gLi4uLi0gLS4uLi4gLS0uLi4gLi4tLS0gLi4uLS0gLi4uLS0gLS4uLi4gLS4uIC0uLi4uIC4uLi4uIC0uLi4uIC4gLi4uLS0gLS0uLi4gLS0uLi4gLS4uIC0tLS0tIC4tCg==</pre>

En voyan `==` à la fin, je pense évidemment à un encodage <a href="https://fr.wikipedia.org/wiki/Base64">base64</a>

Code qui après décodage nous donne un code en semblerait-il <a href="https://fr.wikipedia.org/wiki/Code_Morse_international">Morse</a> :
<pre>
....- ..... ..... ...-- ....- . ....- ---.. ....- .---- ....- ...-- ....- -... --... -... ...-- ...-- ....- . -.... ...-- ...-- ----- -.... ....- ...-- ....- -.... --... ...-- ...-- ..... ..-. ..... -.... ...-- ..... ..... ..-. -.... ...-- ....- ---.. ...-- .---- -.... -.... ....- -.... --... ..--- ...-- ...-- -.... -.. -.... ..... -.... . ...-- --... --... -.. ----- .-
</pre>
Pour le décoder, rien de tel que le site <a href="">dcode.fr<a> qui est une mine d'or !

Forcément, le résultat est encore un nouvel encodage...
<pre>ATTUAT&TA4AURDNTUUANTU�TAURDTUUTETNTUTTENTU&TU�NTRDTVUFNNTNTTÉDN�E
NEEGNE�EN9NGKWAEGGNAEG�ENGKWEGGETEAEGEETAEG�EG�AEKWE�GQAAEAEEÑWA�T
H�6�T�N6B6TVV�B6K�BTT�B6T4�B����A�6T�NT4�T4�BBT4U��TVVUN
��1�E�A1J1E���J1R�JEE�J1E9�J����N�1E�AE9�E9�JJE9G��E��GA
45534E4841434B7B334E6330643467335F56355F634831664672336D656E377D0A
90089T9396989J2J889T1885198912880Q01800Q189386119127881W101T822W5N</pre>

Pour moi les 4 première lignes sont à exclure car elles contiennent des erreurs et ne ressemblent pas à un encodage particulier.
La dernière ne semble être ni de l'ASCII ni de l'héxadécimal.

Je teste donc de décoder la ligne qu'il me reste en héxadécimal:

<pre>$echo 45534E4841434B7B334E6330643467335F56355F634831664672336D656E377D0A | xxd -r -p
$ESNHACK{3Nc0d4g3_V5_cH1fFr3men7}</pre>
