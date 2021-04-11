# Codage couche basse

## Description

> Vous avez intercepté des échanges sur un réseau legacy Ethernet 10mbps. Pourrez vous récupérer les données encodées ?

File : `ethernet_10mbps.txt`

The data in the file could look like binary, but after decoding it it gives nothing relevant.

```
0110100110100110011010010101101001101010011001010110100101101001011010101001101001101001011010100101101001010101011001101010101001101001101001100101101001100101011010011010100101100101010110100110100110010101010110100101101001011010011001100110101001100101010110100101101001100110010110010110101010100110
```

:arrow_right: `i¦iZjeiij.ijZUfªi¦Zei©eZi.ZZZfjeZZfYj¦`

Taking a look at the title, I thought about the first layer of the OSI model and coding techniques that may be used.

The one was Manchester. See on [dcode](https://www.dcode.fr/manchester-code)

After decoding, it gives me a new code, in binary this time.

```
01101101011000110111010001100110011110110110011100110000010111110110110100110100011011100100001101101000001100110011010101110100001100110101001001111101
```

Decoded : `mctf{g0_m4nCh35t3R}`



