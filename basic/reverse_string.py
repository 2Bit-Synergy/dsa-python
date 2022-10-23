s = "Hello"

# Option 1
# -1 => start from end of string
print(s[::-1])

# start=0
# string[start:stop:step]
# string[::step]

# Option 2
# using reversed function
reverse_word = "".join(reversed(s))

# behind the scenes
# "".join(["o", "l", ....])
print(reverse_word)

