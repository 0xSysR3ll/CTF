# Promenade binaire

## Description

???

### Solution

Pour ce challenge, nous sommes encore avec un fichier PDF.
Le créateur [@ThXb35](https://github.com/ThXb35) aime bien les titres explicites et cacher des fichiers dans des PDF x)

Promenade binaire fait tout de suite penser à `binwalk`, qui permet justement de se promener binairement dans un fichier.

```bash
$ binwalk SteganoPDF.pdf

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PDF document, version: "1.4"
70            0x46            PNG image, 200 x 200, 8-bit/color RGBA, non-interlaced
606           0x25E           Zlib compressed data, best compression
517608        0x7E5E8         Zip archive data, at least v2.0 to extract, name: ZipArchive/
517649        0x7E611         Zip archive data, encrypted compressed size: 36165, uncompressed size: 235914, name: ZipArchive/pizza.html
554083        0x87463         End of Zip archive, footer length: 22

```
Grâce à cette commande, on voit qu'il y une archive chifrée cachée.
Pour l'extraire, on va utiliser la commande `dd` avec l'offset de l'archive.

```bash
$ dd if=SteganoPDF.pdf of=Archive.zip bs=1 skip=517608
```

Cette archive est chiffrée, comme binwalk l'indiquait.
Dans le précédent résultat du binwalk, on peut également voir qu'il y a une image PNG. Je pense que le mot de passe se cache à l'intérieur.

```bash
$ dd if=SteganoPDF.pdf of=image.png bs=1 skip=70
```
L'image extraite semble juste être un fond blanc; mais en stéga, une image cache toujours des secrets.

Un petit coup de stegsolve pour appliquer des filtres sur l'image et hop le mot de passe `S0M3_FFF` !

![img](https://github.com/0xSysR3ll/CTF/blob/master/HeroCTF_v2/Steganography/Promenade_binaire/password.png)

On peut maintenant dézippper l'archive.
Le fameux fichier `pizza.html` réapparaît mais cette fois-ci complet.

Il s'agit de la copie d'un article Wikipédia sur la pizza, rien de bien intéressant.

Le format du flag étant HERO{flag}, il suffit de faire
```bash
$ cat pizza.html | grep 'HERO'
HEROCTF - YnJhdm8sIHBhcyB0cm9wIGR1ciBuJ2VzdCBjZSBwYXMgPyBGbGFnID0gSGVyb3tQMVpaNF9IV059
```
La chaîne de caractères après HERO semble être en base64.

```bash
$ echo -n "YnJhdm8sIHBhcyB0cm9wIGR1ciBuJ2VzdCBjZSBwYXMgPyBGbGFnID0gSGVyb3tQMVpaNF9IV059" | base64 -d
bravo, pas trop dur n'est ce pas ? Flag = Hero{P1ZZ4_HWN}
```
