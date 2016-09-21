from md import md

x = md()
x.a.b = 1
x.a.c = [1, 2, 3]

y = md()
y.q.w.e = 999
x.a.d = y

print x
