import base64

encoded_string = "NDc0YjM0NGMzNzdiNTg2NzVmNDU1NjY2NTE1ZjM0NTQ2ODM5NzY0YTZiNmI2YjZiNmI3ZA=="
decoded_bytes = base64.b64decode(encoded_string)
decoded_string = decoded_bytes.decode('utf-8')
print(decoded_string)

hex_string = "474b344c377b58675f455666515f34546839764a6b6b6b6b6b7d"
bytes_object = bytes.fromhex(hex_string)
ascii_string = bytes_object.decode('utf-8')
print(ascii_string)

ans = 'GK4L7{Xg_EVfQ_4Th9vJkkkkk}'


decode = 'OS4T7{Fo_MDnY_4Bp9dRsssss}'
decode = 'OSCTF{Fo_MDnY_CBpHdRsssss}'
#OS4T7{Fo_MDnY_CBpHdRsssss} OScTf{5o_M3nY_c1ph3Rsssss}

#ceasar cipher with number conversion