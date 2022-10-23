# Option 1
s = "Wonderful"

if len(s) < 6:
    print("")

else:
    new_string = s[:3] + s[len(s)-3:]
    print(new_string)

nums_chars = 3

# Option 2
if len(s) < nums_chars*2:
    print("")
else:
    new_string = s[:nums_chars] + s[len(s) - nums_chars:]
    print(new_string)

