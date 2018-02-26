# XOR - 30 points

A flag has been encrypted using single-byte xor. Can you decrypt it? [file](../problem_files/sb_xor.txt)

### Solution
###### Writeup by asinggih

Since the flag is encrypted with single byte XOR, brute forcing is very possible. single byte = 8 bits. Again, I utilised python to do the bruteforcing

Note: I downloaded the given file, and named it "encrypted.txt"

```python
#!/usr/bin/env python3

def brute(input_data):
	out = []
	for i in range(2**8):		# Trying every single possible number that can 
					# be contained in 8 bits
		result=""
		for chars in input_data:
			result += chr(ord(chars) ^ i)
		out.append(result)
	return out

if __name__ == '__main__':
	input_data = open("encrypted.txt", 'r').read()
	result_data=brute(input_data)
	for i in result_data:
		if "easyctf" in i:
			print(i)

```