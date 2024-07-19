## **Efficient RSA**

author: met4sploit

### **Problem:**

n = 13118792276839518668140934709605545144220967849048660605948916761813

e = 65537

enc = 8124539402402728939748410245171419973083725701687225219471449051618

```python
from Cryptodome.Util.number import getPrime, bytes_to_long
Flag = bytes_to_long(b"REDACTED")

p = getPrime(112)

q = getPrime(112)

n = p*q

e = 65537

ciphertext = pow(Flag, e, n)

print([n, e, ciphertext])
```

### **Solution:**

As the p and q are randomly generated, and n is not too big compared to e. I use factordb.com to factorize it and calculate as follows.

phi_n = (p - 1) * (q - 1)

d = inverse(e, phi_n)

m = pow(enc, d, n)

decrypted_flag = long_to_bytes(m)

print(f'Decrypted flag: {decrypted_flag.decode()}')

