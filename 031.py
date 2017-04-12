result = 0

remainder = 200
for a in range(0, remainder+1, 200):
	remainder = 200 - a
	for b in range(0, remainder+1, 100):
		remainder = 200 - a - b
		for c in range(0, remainder+1, 50):
			remainder = 200 - a - b - c
			for d in range(0, remainder+1, 20):
				remainder = 200 - a - b - c - d
				for e in range(0, remainder+1, 10):
					remainder = 200 - a - b - c - d - e
					for f in range(0, remainder+1, 5):
						remainder = 200 - a - b - c - d - e - f
						for g in range(0, remainder+1, 2):
							result += 1

print(result)