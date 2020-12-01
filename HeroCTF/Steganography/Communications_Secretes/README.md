# Communications secrètes

### Description

Le BDE a découvert que certains professeurs de l'IUT communiquaient à travers des PDF de cours. Nous avons réussi à intercepter le PDF en question ainsi qu'une archive. Nous pensons que le PDF peut aider à ouvrir cette archive.

Nous comptons sur vous.

Format: HERO{flag}

### Solution

Le fichier donné est un `.zip`.

Après extraction on obtient un PDF ainsi qu'une archive protégée par mot de passe.
On devine alors qu'il va falloir trouver le mot de passe dans le PDF.

Une technique souvent utilisées consiste à cacher des données dans le code hexa du fichier, ou plus simplement, écrire avec le l'encre blanche.
Pour contourner ça, deux solution :
- Sélectionner tout le texte et normalement votre lecteur PDF affichera le texte caché,
- Convertir le PDF en texte.

Pour ma part, je l'ai converti en texte.
```bash
$ pdftotext how_to_sftp_pjwebb.pdf > pass1.txt
```
Après courte exploration du texte, vers la fin on voit : `f1rs7_p4$$word`

Après extraction avec mot de passe, on obtient une deuxième archive dans laquel il y a un fichier flag.txt
Le deuxième mot de passe ne peut pas être caché dans le zip il doit donc être dans le même pdf qu'avant.

Je décide de regarder les metadata du pdf.
```bash
$exiftool how_to_sftp_pjwebb.pdf
...
XMP Toolkit                     : Image::ExifTool 12.08
Creator                         : 5EC0ND_P4SSW0RD
Producer                        : Microsoft® Word pour Microsoft 365
...
```

Bingo !

On extrait le fichier du flag.

Flag : `HERO{F1N4LLY}`
