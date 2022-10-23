# Option 1
s = "Hello"
n = 1

if not len(s) or n >= len(s):
    print(s)
else:
    new_s = ""
    for i in range(len(s)):
        if i != n:
            new_s += s[i]
    print(new_s)


