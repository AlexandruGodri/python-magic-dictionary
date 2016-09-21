# Magic Dictionary library for Python

Ever had a case when from an empty dictionary (a = {}) you needed to write some stuff somewhere deep in that dictionary?
Ever had a dictionary whose keys (and sub keys in case of a deep dictionary) you wanted to access with the 'dot' notation?

I am pretty sure there are other ways of doing that, but nevertheless, here is my version, a library that does exactly that.

**Instead of:**

```python
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

score = a["l1"]["l2"]["l3"]["score"]
```

**we can do:**

```python
m = md.createFromDict(**a)
m.l1.l2.l3.score
```

Once we have that, we can also do:

```python
m.l1.l2.l4.score = 9
m.l4.l5.l6.score = 5
```

which would result in:

```python
{
	"l4": {
		"l5": {
			"l6": {
				"score": 5
			}
		}
	},
	"l1": {
		"l2": {
			"l4": {
				"score": 9
			},
			"l3": {
				"score": 10,
				"name": "John Doe"
			}
		}
	}
}
```

That, and much more, can be done using this little library i came up with. You can import and export dictionaries, create deep dictionaries in a heartbeat, add a number to a key even though it doesn't exist.

There are several examples which explain most of the features and possibilities offered by the library.

Any feedback will be much appreciated!
