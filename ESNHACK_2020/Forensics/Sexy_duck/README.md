Fichier mis à disposition : inject.bin

Ce fichier n'est pas un fichier bin comme les autres, il s'agit enfait d'un payload pour une clé USB <a href="https://docs.hak5.org/hc/en-us/categories/360000982554-USB-Rubber-Ducky">RubberDucky</a>.

Pour faire court, cette clé une fois branchée se comporte comme un clavier. On peut alors lui demander d'effectuer une combinaison de touches etc.

Pour extraire les données de ce fichier bien il y avait deux solutions.
Soit télécharger l'encoder/decoder mis à disposition<a href="https://github.com/hak5darren/USB-Rubber-Ducky ">ici</a> ou bien utiliser le site <a href="https://ducktoolkit.com/decode">DuckToolKit</a>

On obtient ensuite le payload sous format brut (txt) :

<pre>
DELAY
https://www.youtube.com/watch?v=dQw4w9WgXcQ
ENTER
DELAY
DELAY
notepad.exe
ENTER
DELAY
sOnG iS cOoL hUh ? - So KiTsCh ToVaRiTcH
ENTER
                                           -y. .`ENTER
                                            :yd/`ENTER
                                          `/o:.ENTER
                                     ./::+o.ENTER
                                   -syoho/ENTER
                                .:yhos/`ENTER
                              ./+/+yoENTER
                           `-++/:++:ENTER
                         /ydh/:/+-ENTER
                       :ydho//+-ENTER
                     `+hdmdo/:`ENTER
                   .oddddds-ENTER
                 -sdmdddmh-ENTER
              `/ydddmdmmmmmds+:-.``.ENTER
            `+hdddddoyhohmmmmmmmmmmm-ENTER
            sddddds:``.  `:oyhdmmmmmsENTER
            sdddmmy``          `....`ENTER
          .:+s+:smm/ENTER
       ``--:+-   smm/ENTER
     .-:-::/`     ods.ENTER
  `----://-ENTER
.:-----//`ENTER
+://+/o/ENTER
`/o/+o/ENTER
  .o:`ENTER
ENTER
Blyat ! Learn to lock your computer !ENTER
ENTER
Stay cheeki breeki my friendENTER
Here is the flag you wanted :ENTER
DELAY
cmd
ENTER
curl https://pastebin.com/raw/mK66NJ9h
ENTER
x
</pre>

Ce payload ne fonctionne pas en réalité.
La vidéo youtube correpond à la musique 'Never Gonna Give You Up' de Rick Astley, qui n'a rien à voir avec le challenge.

Cependant, le lien pastebin contient lui le flag <pre>ESNHACK{Lien expiré :( }</pre>

Challenge sympa que je n'aurai pu résoudre si je n'avais pas eu la connaissance des RubberDucky.
