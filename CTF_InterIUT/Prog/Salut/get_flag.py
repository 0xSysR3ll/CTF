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

    #Inscrease base
    base += 1
    
    #Get flag

    if "H2G2" in data:
        print("[+] Flag = "+data)
        exit()