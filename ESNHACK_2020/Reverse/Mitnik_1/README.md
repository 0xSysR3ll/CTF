Pour ce challenge de reverse, le fichier à étudier une un fichier `bin` de type `ELF 64-bit`

Un outil intéressant pour ce genre de fichier : `radare2`. Il permet de faire des belles analyses du code.

<pre>$radare2 c1.bin</pre>

Pour analyser tout le code on va venir afficher les entrées de type `sym.`
<pre>[0x00001090]>aa
[x] Analyze all flags starting with sym. and entry0 (aa)</pre>

Puis on affiche les informations sur les `Strings`
<pre>[0x00001090]>iz</pre>

Et oilà, la première ligne affiche le flag :

<pre>0   0x00002008 0x00002008 42  43   .rodata ascii ESNHACK{CL43R_STR1NGS_4R3_T00_1Z1_T0_F1ND}</pre>
