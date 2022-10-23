# Option 1
s = "Coding"

new_s = ""

# Get event characters index
for i in range(len(s)):
    if i % 2 != 0:
        new_s += s[i]

print(new_s)

# Option 2
# generate odd indices
# range(1, len(s), 2)
# range(start, length, increment)
# 1, 3, 5, 7

# reset string
new_s = ''

for i in range(1, len(s), 2):
    new_s += s[i]

print(new_s)

