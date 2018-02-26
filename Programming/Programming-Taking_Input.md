# Programming: Taking input - 30 points

OK, OK, you got Hello, world down, but can you greet specific people?

You'll be given the input of a certain name. Please greet that person using the same format. For example, if the given input is `Michael`, print `Hello, Michael!`.

- For Python, consider the `input()` function.
- For Java, consider `System.in`.
- For C, consider including `stdio.h` and reading input using `read`.
- For C++, consider including `iostream` and reading input using `cin`.

### Solution
###### Writeup by asinggih

```python
#!/usr/bin/env python3

def greet():
	userinput = input()
	print("Hello, {}!".format(userinput))

if __name__ == '__main__':
	greet()

```