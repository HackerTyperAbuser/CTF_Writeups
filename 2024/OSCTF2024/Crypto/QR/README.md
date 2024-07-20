# QR
Author: TriDuong070803

# Problem
'''
from Crypto.Util.number import *
from random import *

flag = b'REDACTED'

p = 96517490730367252566551196176049957092195411726055764912412605750547823858339
a = 1337

flag = bin(bytes_to_long(flag))[2:]
encrypt = []

for bit in flag:
    encrypt.append(pow(a, (randint(2, p) * randrange(2, p, 2)) + int(bit), p))
    

print(encrypt)
'''

# Analyze

First we can see that the flag is changed to binary string without the prefix '0b'. After that, the author create a for loop by letting a new value called "bit" running through the flag. This means the value of bit is 1 or 0 because flag is a binary string. In the loop, there is a formula to encrypt each bit to a random number. So, to solve this problem, we need to recover the original binary string from the values in the encrypt. As you can see, we need to find out the "bit" that used to calculate the encrypt is 0 or 1. In this case, we can use a method called quadratic residue. 

Khúc này nói tiếng Việt nha huhu, tiếng Anh diễn tả rồi quá. Từ cái công thức đề bài thì mình thấy được từng cái giá trị trong cái encrypt list sẽ được tính bằng: 
                            a^x % p, với x= (randint(2, p) * randrange(2, p, 2)) + int(bit)
Ta thấy được (randint(2, p) * randrange(2, p, 2)) luôn luôn là số chẵn. Nên là nếu bit = 0 thì x sẽ tiếp tục chẵn, còn bit = 1 thì x sẽ là số lẽ. Nên từ đây ta áp dụng quadratic residue (thặng dư bậc 2). Thì định nghĩa thặng dư bậc 2 như sau: một số m bất kỳ là thặng dư của n khi tồn tại l^2 sao cho l^2 ≡ m (mod n).

Áp dụng phương pháp này vào bài trên nếu x là số chẵn thì chắc chắn sẽ tồn tại thặng dư bậc 2 vì khi đó ta có giá trị dưới dạng a^2k mod p cũng như (a^k)^2 mod p. Còn nếu x là số lẽ thì sẽ không có thặng dư bậc 2. Qua đây ta kết luận được khi giá trị của 1 số trong encrypt tồn tại thặng dư bậc 2 thì bit = 0 và ngược lại bit = 1

# Solution:

b'OSCTF{d0_y0U_L0v3_m47H_?_<3}'
The code solution is in solve.py
 
