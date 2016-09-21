from md import md

a = {
	"l1": {
		"l2": {
			"l3": {
				"name": "John Doe",
				"score": 10
			}
		}
	}
}

m = md.createFromDict(**a)
m.l1.l2.l3.score

m.l1.l2.l4.score = 9
m.l4.l5.l6.score = 5

print m
