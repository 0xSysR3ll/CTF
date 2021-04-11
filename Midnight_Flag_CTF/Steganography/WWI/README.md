# WWI

## Description

> Un enregistrement audio datant de la Première Guerre mondiale a été retrouvé. Il a été transmis depuis un sous-marin français. Pouvez-vous vérifier qu'il ne contient pas de message caché ?

File : `audio.mp3`

Listening to the audio file, it is obviously morse code and the title confirms it by referring to first world war.

Drawing the spectrogram with Sonic Visualiser we got the code.

![code.png](code.png)

`.-.. ...-- -.-. .... ....- -. - -.. ..- .-.. ----- ..- .--.` = `L3CH4NTDUL0UP`

Decoded with [dcode](https://www.dcode.fr/code-morse)

Flag : `MCTF{L3CH4NTDUL0UP}`