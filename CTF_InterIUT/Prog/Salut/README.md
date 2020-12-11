# 1110011 1100001 1101100 1110101 1110100

### Description

2202 1110 10121 10220 11001 10202 11020 10121 10220 11021 1012 11021 10121 11101 11010 10220 11020 1012 10200 11010 11001 11001 10202 11002 11022 1012 10210 10121 10220 11020 10202 1012 11100 11002 10202 1012 10122 11010 11002 11002 10202 1012 11011 11100 11020 10202 10202

salut.interiut.ctf:1337

### Solution

First of all, we have to translate the title and description to get hints about the challenge.

The title is obviously in binary format.

We can either use website converters of build a little script in python to do it because I assume it will be useful...

```python
#*-* coding: utf-8

encoded = input('\nInput your base encoded text : ')
base = int(input('\nBase of encoded text : '))
parts = encoded.split(' ')
decoded = ""
for part in parts:
	decoded += ''.join(str(chr(int(part,base))))
print("\nDecoded text : "+decoded)
```
Of course if you don't know the base of the text you can bruteforce it with a loop from base 2 to base(i)

- `int(part,base)` => convert base input to ascii code
- `(chr(int(part,base)` => convert an ascii code to text

With the title it gives :
```bash
$ python3 basetotext.py
Input your base encoded text : 1110011 1100001 1101100 1110101 1110100

Base of encoded text : 2

Decoded text : salut
```

Not giving such info

With the description now, which doesn't weem to be binary.

```bash
> python3 basetotext.py

Input your base encoded text : 2202 1110 10121 10220 11001 10202 11020 10121 10220 11021 1012 11021 10121 11101 11010 10220 11020 1012 10200 11010 11001 11001 10202 11002 11022 1012 10210 10121 10220 11020 10202 1012 11100 11002 10202 1012 10122 11010 11002 11002 10202 1012 11011 11100 11020 10202 10202

Base of encoded text : 3

Decoded text : J'aimerais savoir comment faire une bonne puree
```

I'm lucky it was base 3 - if not I would have bruteforce it.

The title and the description give us absolutely no information except that the text refers to a song from the band "Salut c'est cool".

I decide to connect to the server with netcat.

It gives back a base 2 string. With my super tool I'm able to translate it
> Je s4is dej4 f4ire l4 r4t4touille, les endives 4u j4mbon, le gr4tin

Searching for the lyrics of the song, the string received is the lyric that comes after 
> J'aimerais savoir comment faire une bonne puree

From there, I guessed that I had to send the translation back to the server to unroll all the lyrics and maybe at the end have the flag.

After sending the first tanslation :

```bash
$ nc salut.interiut.ctf 1337

nc salut.interiut.ctf 1337
1001010 1100101 100000 1110011 110100 1101001 1110011 100000 1100100 1100101 1101010 110100 100000 1100110 110100 1101001 1110010 1100101 100000 1101100 110100 100000 1110010 110100 1110100 110100 1110100 1101111 1110101 1101001 1101100 1101100 1100101 101100 100000 1101100 1100101 1110011 100000 1100101 1101110 1100100 1101001 1110110 1100101 1110011 100000 110100 1110101 100000 1101010 110100 1101101 1100010 1101111 1101110 101100 100000 1101100 1100101 100000 1100111 1110010 110100 1110100 1101001 1101110 
Je s4is dej4 f4ire l4 r4t4touille, les endives 4u j4mbon, le gr4tin
```
It replies me back with a base 3 encoded string.

I assume that after each translation the base will then increase.

Time for scrypting then.

To connect, send and get responses from the netcat server I used the pown library.

```python
# *-* coding: utf-8 *-*
from pwn import *

#Connection parameters
hostname = "salut.interiut.ctf"
port = 1337

conn = remote(hostname, port)
decoded = ""

#First text received is in binary format
base = 2

while True:
    #After each text there is a '\n' so we must consider it
    data = conn.recvuntil('\n').decode('utf-8')
    print("received : "+data)
    
    #We must pick decode each block of text  wich are separated by spaces
    parts = data.split(' ')
    for i in range(len(parts)-1):
        part = parts[i]
        decoded += ''.join(str(chr(int(part,base))))
    print("sending : "+decoded)

    #Send decoded text to server
    conn.sendline(decoded)

    #Reinitialising decoded text
    decoded = ""

    #Get flag
    base += 1
    if "H2G2" in data:
        print("[+] Flag = "+data)
        exit()
```

The script has been slightly modified due to errors. It's is not quite optimised but works perfectly !

After a few seconds, I get the flag :)

```bash
[+] Flag = H2G2{D0_y0u_l1k3_14_pur33_?}
```
