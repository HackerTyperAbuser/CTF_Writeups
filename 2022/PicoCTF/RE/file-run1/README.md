# file-run1 

Writeup Author: Nguyen Nghia Hiep

## Challenge Description
```
Tags: Reverse Engineering, PicoCTF2022

A program has been provided to you, what happens if you try to run it on the command line?
Download the program

Hints:
1. To run the program at all, you must make it executable (i.e. $ chmod +x run)
2. Try running it by adding a '.' in front of the path to the file (i.e. $ ./run)
```
## Writeup

Very simple challenge and hints give away the answer. Always check file permissions.
```bash
$ ls -la
drwxrwxr-x  2 fakevapour fakevapour  4096 Jul 11 15:30 img
-rwxr-xr-x  1 fakevapour fakevapour 16736 Mar 16  2023 run
```
File permission allows for program execution. We can grant permission with
```bash
$ chmod +x run
```
 The flag is given to us.
 ![alt text](https://github.com/HackerTyperAbuser/CTF_Writeups/blob/main/2022/PicoCTF/RE/file-run1/filerun1.png)

