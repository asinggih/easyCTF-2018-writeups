# Teaching old tricks new dogs - 40 points

You can decode a Caesar cipher, but can you write a program to decode a Caesar cipher?

Your program will be given 2 lines of input, and your program needs to output the original message.

- First line contains `N`, an integer representing how much the key was shifted by. `1 <= N <= 26`
- Second line contains the ciphertext, a string consisting of lowercase letters and spaces.

For example:

```
6
o rubk kgyeizl
```

You should print

```
i love easyctf
```

### Solution
###### Writeup by asinggih


```python
#!/usr/bin/env python3

def caesar(text, shift):
	out = ""
	for i in text:
		if i.isalpha():
			out += chr(x[x.index(ord(i)) - shift])
		else:
			out += i

	return out

if __name__ == '__main__':
	try:
		shift = int(input())
	except ValueError:
		shift = -1										# brute force flag

	text = input()

	x =[i for i in range(97,123)]

	if shift != -1:
		print("+{}: ".format(shift) + caesar(text, shift))

	else:	# let's try all of them
		for shift in range(26):
			print("+{:2}: ".format(shift) + caesar(text, shift))


```


we can use it by specifying the shift like the problem above e.g.,

```bash
❯ ./caesar_shift.py 
6
o rubk kgyeizl
+6: i love easyctf
```


Or leaving the shift empty, to do a brute force

```bash
❯ ./caesar_shift.py

o rubk kgyeizl
+ 0: o rubk kgyeizl
+ 1: n qtaj jfxdhyk
+ 2: m pszi iewcgxj
+ 3: l oryh hdvbfwi
+ 4: k nqxg gcuaevh
+ 5: j mpwf fbtzdug
+ 6: i love easyctf
+ 7: h knud dzrxbse
+ 8: g jmtc cyqward
+ 9: f ilsb bxpvzqc
+10: e hkra awouypb
+11: d gjqz zvntxoa
+12: c fipy yumswnz
+13: b ehox xtlrvmy
+14: a dgnw wskqulx
+15: z cfmv vrjptkw
+16: y belu uqiosjv
+17: x adkt tphnriu
+18: w zcjs sogmqht
+19: v ybir rnflpgs
+20: u xahq qmekofr
+21: t wzgp pldjneq
+22: s vyfo okcimdp
+23: r uxen njbhlco
+24: q twdm miagkbn
+25: p svcl lhzfjam
```


