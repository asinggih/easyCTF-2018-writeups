# Programming: Over and Over - 30 points

over and over and over and over and over and ...

Given a number `N`, print the string "over [and over]" such that the string contains `N` "over"s. There should _not_ be newlines in the string.

For example:

- For `N` = 1, print "over".
- For `N` = 5, print "over and over and over and over and over".

- For Python, consider using `for` and `range`.
- For Java/CXX, consider using a `for` loop.

Try doing it with `while` too for practice!

### Solution
###### Writeup by asinggih

Maybe there's a more elegant solution, but this was what I had in mind.

```python
#!/usr/bin/env python3


n = int(input())

result = ""
for i in range(n):
    if i+1 == n:
        result += "over"
    else:
        result += "over and "

print(result)
```



