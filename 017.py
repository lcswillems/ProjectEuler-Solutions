units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
other = ['hundred', 'thousand', 'and']

result = 0

for i in range(1, 1001):
	unit = i%10
	ten = (i//10)%10
	hundred = (i//100)%10
	thousand = (i//1000)%10

	if thousand != 0:
		result += len(units[0]) + len(other[1])

	if i%1000 != 0:
		if hundred != 0:
			result += len(units[hundred-1]) + len(other[0])
			if i%100 != 0:
				result += len(other[2])

		if i%100 != 0:
			if ten < 2:
				result += len(units[i%100-1])
			else:
				result += len(tens[ten-2])
				if unit != 0:
					result += len(units[unit-1])

print(result)