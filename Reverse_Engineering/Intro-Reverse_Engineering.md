# Intro: Reverse Engineering - 30 points

What does this [Python program](../problem_files/mystery_problem.py) do? And more specifically, what input would give this output below?

```6500c2a1c280c2afc28ac2bac296c3bb017bc3a33b4cc3951a5319035bc2a3674dc39bc3b13cc3acc2bc```

### Solution
###### Writeup by asinggih

Just like what the title says, I had to reverse engineer the given python code. However, I did a little modification to it, to know what it does. 

```Python

import binascii

#chr() ----> converts Unicode to chars
#ord() ----> converts chars to Unicode

key = "saiSsfzk"
def mystery(s):
    r = ""
    for i, c in enumerate(s):	
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
    # print(r)			
    temp = bytes(r, "utf-8")
    return binascii.hexlify(temp), temp   # I returned 2 items here, to see 
    					# before and after hexlify function

```

From the given code above, i created a decoder of the output from the function above.
Since the function is utilising a simple XOR operation, the reverse engineering does not involve a lot of changes.

e.g., 
```
5 ^ 2 == 7
7 ^ 2 == 5
5 ^ 7 == 2
```

```python

import binascii

def decoder(s):
	out = ""
	temp = binascii.unhexlify(s)		# First step is to unhexlify the string
	temp2 = temp.decode("utf-8")		# decode the string into utf-8 format
	for i, c in enumerate(temp2):		# loop each char and perform an XOR function
						# to reverse it back to the original string
		out += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))

	return out

if __name__ == '__main__':
	s = "6500c2a1c280c2afc28ac2bac296c3bb017bc3a33b4cc3951a5319035bc2a3674dc39bc3b13cc3acc2bc"
	# s is the hexlified output of the mystery() function.

	x =(decoder(s))
	print(x)
```

Note: I know that binascii has an unhexlify function through checking the items inside
the package using ```dir(packagename)```

```python

>>> dir(binascii)
['Error', 'Incomplete', '__doc__', '__file__', '__loader__', '__name__',  
'__package__', '__spec__', 'a2b_base64', 'a2b_hex', 'a2b_hqx', 'a2b_qp', 'a2b_uu', 
'b2a_base64', 'b2a_hex', 'b2a_hqx', 'b2a_qp', 'b2a_uu', 'crc32', 'crc_hqx', 'hexlify', 
'rlecode_hqx', 'rledecode_hqx', 'unhexlify']
>>> 
```






