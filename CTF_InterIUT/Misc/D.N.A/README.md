---
title: "D.N.A"
document: pdf_document
---
# D.N.A

### Description

### Solution

In this challenge we have to go on this page `http://interiutwzsx3dvp.onion`

Because I don't want't to use TOR proxy, I will use the extension `.ws` which allow us to visit `.onion` website without proxy.

Tha page says :
>  We'll start this journey by checking that you're not a Sentinel. POST a request to the /challenge URL and decode the secret language. You must return the unleeted value with the key "payload".
```bash 
curl -X POST -H 'Content-Type: application/json' --data '{"token": "df1cb36f2cf37abd4c74e454ceac07605fec600e68f2fa3895cb6fac06a23154", "payload": "unleeted_text"}' this.server/challenge
```
With the description of the challenge and the name of the payload to send, we understand that it will be necessary to send in loop the text translated from 1337 (leet) into text until we see the flag.

I tried to do it by hand, but after 5 translation I thought about scripting x)

My script isn't perfect but that's what I came up to in 10 minutes...

I had issues with characters that wheren't translated so I had to add them to the dictionnary.

```python
#*-* coding: utf-8 *-*
import requests
from utilitybelt import change_charset

#Fonction de traduction leet en text
def leetTranslate(text, before=None):
    #Dictionnaire 1337
    d = {
    '1':'l',
    '3':'e',
    '4':'a',
    '5':'s',
    '7':'t',
    '8':'b',
    '0':'o',
    'u2026':'...',
    'u2014':'-',
    '\\':''
    }
    #remplacement des lettres
    if not text: return text
    before = before or str.lower
    t = before(text)
    for key, value in d.items():
        t = t.replace(key, value)
    return t
    
flag=""
leet = "unleeted_text"

while "H2G2" not in leet:
    payload = leetTranslate(leet)
    headers = {
    'Content-Type': 'application/json',
    }
    
    req = requests.Session()
    url = "http://interiutwzsx3dvp.onion.ws/challenge"
    
    data = '{"token": "df1cb36f2cf37abd4c74e454ceac07605fec600e68f2fa3895cb6fac06a23154", "payload": "'+payload+'"}'                          
    #Request/Response
    response = req.post(url=url, headers=headers, data=data)
    leet = str(response.text)[10:]
    leet = leet[:-3]
    print("[-] :"+leet)
    print("[+] : "+payload)
print(payload)
```
After like 100 translation, the flag finally comes.
Really interesting challenge btw !
Flag : `H2G2{th3r3_1s_n0_SP00N}`