Pour ce challenge de sténographie, on a à disposition un fichier audio `monster.wav`.
Il y a plusieurs façons de cacher des informations dans ce genre de fichier.

- Soit dans les metadata
- soit la vitesse, gain, sens de lecture a été modifié sur le fichier
- ou encore, il est possible de cacher des informations dans le spectre du signal audio

Dans le cas de notre fichier `monster.wav`, le rendu audio est un miaulement de chat. Difficile donc d'imaginer qu'un flag est caché dedans.
On va donc plus s'intéresser au rendu spectrale. Pour ça il existe <a href="https://www.sonicvisualiser.org/">Sonic Visualizer</a> ou si on ne veut pas s'embêter à installer un logiciel pour l'occasion, encore une fois on fait appel à <a href="https://www.dcode.fr/spectral-analysis">dcode.fr</a>

Il suffit alors d'importer le fichier et de le jouer. Le flag apparaîtra.
