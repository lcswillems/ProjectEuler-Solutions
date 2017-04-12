def name_score(name):
	score = 0
	for i in name:
		score += ord(i) - 64
	return score

with open("022_names.txt") as file:
	names = sorted(list(eval(file.read())))

result = sum(map(
	lambda i, name: (i+1)*name_score(name),
	enumerate(names)
))
print(result)