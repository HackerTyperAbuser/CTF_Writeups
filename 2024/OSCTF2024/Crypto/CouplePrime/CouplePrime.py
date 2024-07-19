from Crypto.Util.number import *
import math

n = 13118792276839518668140934709605545144220967849048660605948916761813
e = 65537
c = 8124539402402728939748410245171419973083725701687225219471449051618


def fermat_factorization(n):

    a = math.isqrt(n) + 1
    b2 = a * a - n
    b = math.isqrt(b2)

    while b * b != b2:
        a += 1
        b2 = a * a - n
        b = math.isqrt(b2)

    p = a + b
    q = a - b

    return p, q

p, q = fermat_factorization(n)
print(f"Prime factors of {n} are {p} and {q}")



phi_n = (p - 1) * (q - 1) 
d = inverse(e, phi_n)
m = pow(c, d, n)

decrypted_flag = long_to_bytes(m)
print(f'Decrypted flag: {decrypted_flag.decode()}')
