# FreePassXC

### Description

Nous avons retrouvé le gestionnaire de mot de passe d'un pirate, à vous de retrouver le mot de passe associé.

Format: Hero{password}

### Solution

On a en notre possession un fichier `.kdb` qui correspond à une base de donnée KeePassXC (gestionnaire de mots de passe)

Premier reflèxe quand on nous demande de bruteforcer un mot de passe, on utilise l'outil `John The Ripper` avec la wordlist `rockyou.txt`.

Ici je ne sais pour quelle raison, `john` avait décidé de ne pas fonctionner j'ai dû utiliser `hashcat`.

```bash
#Récupération du hash de la base de données avec keepass2john
$ keepass2john s3cr3t.kdb > s3cr3t.kdb.hash
```

En observant le contenu du fichier hash généré, on s'aperçoit qu'il n'est pas conforme.
En effet, un hash kepass doit être sous cette forme :
`$keepass$*1*50000*0*7c27c16c99d2222ae71a33281eaeac5b*b53f59fc7185c0d342fbaae0ae5c907cd[...]`
<br/><br/>
Il faut donc supprimer `s3cr3t.kdb:-` en début de fichier
Après ça, laisser hashcat faire son travail.

```bash
# -m 13400 => Type de hash (Keepass)
# -a 0 => Attaque par dictionnaire
# -w 1 => Latence courte
$ hashcat -m 13400 -a 0 -w 1 s3cr3t.kdb.hash rockyou.txt --show
$keepass$*1*50000*0*7c27c16c99d2222ae71a33281eaeac5b*b53f59fc7185c0787e70ce4e4f226058b4a8844fa78b0f[...]:jesuscristo
```

On peut vérifier que le mot de passe trouvé est le bon en ouvrant la kdb avec Keepass.

Flag : `Hero{jesuscristo}`
