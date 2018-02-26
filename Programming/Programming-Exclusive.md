# Programming: Exclusive - 20 points

Given two integers `a` and `b`, return `a` xor `b`. Remember, the xor operator is a bitwise operator that's usually represented by the `^` character.

For example, if your input was `5 7`, then you should print `2`.

### Solution
###### Writeup by asinggih

This is a simple programming exercise. I did this on python3

```python
#!/usr/bin/env python3

userinput = input().split()

a,b = int(userinput[0]), int(userinput[1])

print(a ^ b)
```



