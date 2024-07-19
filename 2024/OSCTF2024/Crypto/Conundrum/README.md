## **Cipher Conundrum**

author: met4sploit

### **Description:**

*Given the base64 code:*

NDc0YjM0NGMzNzdiNTg2NzVmNDU1NjY2NTE1ZjM0NTQ2ODM5NzY0YTZiNmI2YjZiNmI3ZA==

Find the flag.

### **Solution:**

base64 -> convert to hex -> bytes -> ascii

```python
 encoded_string = "NDc0YjM0NGMzNzdiNTg2NzVmNDU1NjY2NTE1ZjM0NTQ2ODM5NzY0YTZiNmI2YjZiNmI3ZA=="

decoded_bytes = base64.b64decode(encoded_string)

decoded_string = decoded_bytes.decode('utf-8')

hex_string = "474b344c377b58675f455666515f34546839764a6b6b6b6b6b7d"

bytes_object = bytes.fromhex(hex_string)

ascii_string = bytes_object.decode('utf-8')

print(ascii_string)
```

GK4L7{Xg_EVfQ_4Th9vJkkkkk}

It’s almost there, so we convert this string by bruteforce caesar cipher with number, [https://planetcalc.com/8572/](https://planetcalc.com/8572/), it turns out the flag OScTf{5o_M3nY_c1ph3Rsssss}

