# crackme-py
## Description
```
Tags: Reverse Engineering, PicoCTF 2021

none

Hints:
none
```
## Writeup
Downloading the file, we quickly figured out this a python file by the .py file extension. Running the file we see it is finding the largest number between two inputs.
```bash
└─$ python3 crackme.py                                       
What's your first number? 1
What's your second number? 2
The number with largest positive magnitude is 2
```
![alt text](https://github.com/HackerTyperAbuser/CTF_Writeups/blob/main/2021/PicoCTF/RE/crackme-py/picture1.png)
Viewing the source code we can observe there are two functions, yet only choose_greatest() is being called. Here we found an interesting variable called bezos_cc_secret and function decode_secret(secret) that is not called
![alt text](https://github.com/HackerTyperAbuser/CTF_Writeups/blob/main/2021/PicoCTF/RE/crackme-py/picture2.png)
This function is performing a ROT47 decode, here i tried calling the function with the parameter bezos_cc_secret by adding the line.
```python
decode_secret(bezos_cc_secret)
```
From that running the script, the flag is captured!
```bash
└─$ python3 test.py   
picoCTF{1|\/|_4_p34|\|ut_f3bc410e}
```
