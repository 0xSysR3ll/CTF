# Endianness

## Description

File : `Endianness.pcapng`

After opening the file with Wireshark it seems that we have to do an ICMP payload exfiltration.

For that I have a magic command :

```bash
$ tshark -T fields -e "data" -r Endianness.pcapng | xxd -p -r
4d4354467b4e337633725f473176335f55707d
4d4354467b4e337633725f473176335f55707d
...
7D6C616D31633364617833685F6E6168745F797833735F3372306D5F73695F7972616E31427B4654434D
...
4d4354467b4e337633725f473176335f55707d
4d4354467b4e337633725f473176335f55707d
```

The result gives the same hex data on each line but one is interesting : 

`7D6C616D31633364617833685F6E6168745F797833735F3372306D5F73695F7972616E31427B4654434D`

After decoding it we obtain the flag in reverse.

`}lam1c3dax3h_naht_yx3s_3r0m_si_yran1B{FTCM`

A little bit of python code and...

```python
>>> str="}lam1c3dax3h_naht_yx3s_3r0m_si_yran1B{FTCM"  # initial string
>>> stringlength=len(str) # calculate length of the list
>>> slicedString=str[stringlength::-1] # slicing
>>> print(slicedString) # print the reversed string
MCTF{B1nary_is_m0r3_s3xy_than_h3xad3c1mal}
```





