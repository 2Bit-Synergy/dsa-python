s = "Something"
i = 0

print(len(s))

# Option 1

if not s: # or len(s) == 0:
    print("Empty String")
elif i < len(s):
    print(s[i])
else:
    print("i is out of range")

