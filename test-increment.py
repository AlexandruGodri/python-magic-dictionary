from md import md

x = md()
x.l1.l2.l3.name = "John Doe"
x.l1.l2.l3.score += 5
x.l1.l2.l3.score += 3

# will result in the 'score' property with the value 8
# the md library detects that an increment and initializes the values with 0
print x
