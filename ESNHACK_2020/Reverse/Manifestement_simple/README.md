Encore une catégorie que je n'avais pas réellement exploré.
Nous avons à disposition un fichier `.apk`.

Ayant déjà fait un peu d'Android, je devine avec le titre que le flag est en relation avec le fichier `AndroidManifest.xml` contenu à la racine du fichier.
Pour extraire les données de l'apk, trois solutions :
- L'ouvrir avec Android Studio
- Utiliser le package `apktool`
- Le renommer en `.zip` et le dézipper

Pour ma part, j'ai utilisé apktool :
<pre>$apktool d esnhack1.apk</pre>

Pour lire le fichier `AndroidManifest.xml`, un simple `$cat AndroidManifest.xml` suffit.
Parmi les lignes on y trouve bien le flag.

<pre>ESNHACK{@lway5_ch3cK_Man1f3s7}</pre>
