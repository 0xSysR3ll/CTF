# Origami de format de document portable

### Description

En nous baladant dans l'IUT nous avons trouvé une clé USB contenant un document étrange. après quelques recherches, nous pensons qu'elle peut contenir des données sensibles. Nous comptons sur vous les extraires.

### Solution

Encore une fois, le titre nous donne des informations sur le prncipe du challenge.

Traduit en anglais : Portable Document Format (PDF) Origami

Pour ce type de challenge, il est intéressant d'analyser le fichier PDF avec l'outil `pdf-parser`. 

Cet outil nous permet d'avoir des informations sur les objets contenus dans le document. 
Et en général, si des fichiers sont cachés à l'intérieur, on observera la mention `/Embeddedfiles`

```bash
$ pdf-parser steg.pdf
...
obj 8 0
 Type: /EmbeddedFile
 Referencing: 
 Contains stream

  <<
    /Length 76661
    /Filter /FlateDecode
    /Type /EmbeddedFile
  >>
...
```

En parcourant rapidement, on observe que l'objet n°8 embarque un fichier de taille `76 661 octets`.

Une autre information importante : `/Filter FlateDecode` qui veut dire que si on veut extraire le fichier, il faudra utiliser le paramètre --filter sinon le fichier ne sera pas lisible.

Extraction du fichier :
```bash
pdf-parser -o 8 -f -d EmbeddedFile steg.pdf
```

Après extraction, il semble s'agir d'une image `JPEG` avec tchoupi...

En faisant une analyse de l'entête du fichier, il semblerait qu'elle ait été modifiée.

```bash
$ hexeditor EmbeddedFile.jpg

00000000   FF D8 FF E0  00 10 4A 46  49 46 00 01  01 00 00 01  ......JFIF......
00000010   00 01 00 00  FF DB 00 43  00 03 02 02  08 08 08 08  .......C........
00000020   08 08 64 65  61 64 62 65  65 66 31 32  33 34 08 08  ..deadbeef1234..
```
Cette mention de `deadbeef1234` me fait penser à un mot de passe...
Par hasard, j'essaye donc d'extraire les fichiers qui pourraient être cachés dans l'image avec ce mot de passe.

```bash
$ steghide extract -sf EmbeddedFile.jpg -p deadbeef1234
```

Bingo ! On obtient une image `a3bef5.png` avec le flag écrit à l'interieur.

Flag : `Hero{B3_C4R3FUL}`
