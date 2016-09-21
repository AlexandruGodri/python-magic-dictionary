from md import md

x = {
	"a": 1,
	"b": {
		"c": 2,
		"d": [
			{ "t": 1, "r": 2 },
			{ "t": 3, "r": 4 }
		]
	}
}

y = md.createFromDict(**x)

z = md()
z.importDict(**x)

# the following should be the same
print y
print z
