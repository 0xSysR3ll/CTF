Challenge divisé en trois épisodes.
On dispose d'un fichier `challenge.raw`, qui provient sûrement d'une capture mémoire faite sur un PC sous Windows.

Pour analyser ce fichier on va utiliser l'outil `volatility`.

Pour les 3 épisodes, il s'agira d'utiliser la même image.

<br/>
<strong>ESNHACK Computer 1 : Récupérer le mot de passe de l'utilisateur ESN'HACK</strong>

La première étape consiste à déterminer le `--profile` de l'image. Celui-ci sera utilisé pendant tout le long de l'analyse.

<pre>$volatility -f challenge.raw imageinfo
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : WinXPSP2x86, WinXPSP3x86 (Instantiated with WinXPSP2x86)
</pre>

Ensuite, volatility dispose de nombreux `plugins` pour exploiter les images.
Vous pouvez en retrouver une list assez complète <a href="http://repository.root-me.org/Forensic/EN%20-%20Volatility%20cheatsheet%20v2.4.pdf">ici</a>


Pour afficher les identifiants/mot de passe hashés, on utilise `hashdump`

<pre>$volatility -f challenge.raw --profile=WinXPSP2x86 hashdump

Volatility Foundation Volatility Framework 2.6
Administrateur:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Invit:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
HelpAssistant:1000:3cf54e12eafdcdf36d62c41d4a1daecb:81b2be3e89b7f236ec28dcffd2cde734:::
SUPPORT_388945a0:1002:aad3b435b51404eeaad3b435b51404ee:3b895d32baf7d48355c7495bf4e705b9:::
Esn'Hack:1004:74542d2dc6c9615a259cbc5abd49b99f:835452652dbdd91ce74c632340ce09d7:::
</pre>

Maintenant, le mot de passe que l'on cherche correspond à `835452652dbdd91ce74c632340ce09d7` et est hashé avec la méthode NTLM.
Généralement, dans ces challenges le mot de passe peut-être "cracké" car il est connu.
Pour ce faire, je ne connais qu'une seule solution pour le moment : <a href="https://crackstation.net/">CrackStation</a>

Qui nous donne : <pre>ESNHACK{mortymorty}</pre>

<br/>
<strong>ESNHACK Computer 2 : Déterminer le programme qui se lance au lancement de l'ordinateur</strong>

Pour ce challenge, on va utiliser la même base que précédement.

Généralement, les programmes malveillants s'inscrivent au niveau d'un clé de registre: `'HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run'`
De cette manière, ils seront lancés automatiquement au démarrage de l'ordinateur.

Pour afficher les entrées de cette clé, il suffit d'utiliser le plugin `prinkey` ainsi :

<pre>$volatility -f challenge.raw --profile=WinXPSP2x86 printkey -K 'Software\Microsoft\Windows\CurrentVersion\Run'

Registry: \Device\HarddiskVolume1\Documents and Settings\Esn'Hack\NTUSER.DAT
Key name: Run (S)
Last updated: 2020-03-02 22:55:51 UTC+0000

Subkeys:

Values:
REG_SZ        CTFMON.EXE      : (S) C:\WINDOWS\system32\ctfmon.exe
REG_SZ        FLAG            : (S) ESNHACK{4llW4y5_Ch3cK_r3gI57rY_K3y}

</pre>

<br/>
<strong>ESNHACK Computer 3 : Trouver le nom de l'ordinateur</strong>

Enfin dans cette troisième partie, on nous demande de trouver le nom de la machine.

Pas plus compliqué que le précédent, il suffit de se balader sur le registre de Windows.
Le nom de la machine est situé à cet endroit : `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName`
Cependant vous verrez que le chemin diffère légèrement dans la commande :

<pre>$ volatility -f Challenge1.raw --profile=WinXPSP2x86 printkey -K 'ControlSet001\Control\ComputerName\ComputerName'     
Volatility Foundation Volatility Framework 2.6
Legend: (S) = Stable   (V) = Volatile

----------------------------
Registry: \Device\HarddiskVolume1\WINDOWS\system32\config\system
Key name: ComputerName (S)
Last updated: 2020-02-25 22:48:29 UTC+0000

Subkeys:

Values:
REG_SZ        ComputerName    : (S) V0LD07PY15C00L
</pre>

Le flag est donc `ESNHACK{V0LD07PY15C00L}`

