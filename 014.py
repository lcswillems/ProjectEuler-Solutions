collatz_seq_lens = {1: 0}

def collatz_seq_len(nb):
	global collatz_seq_lens

	if nb in collatz_seq_lens:
		return collatz_seq_lens[nb]
	
	if nb%2 == 0:
		length = collatz_seq_len(nb//2)
	else:
		length = collatz_seq_len(3*nb + 1)
		
	length += 1
	collatz_seq_lens[nb] = length
	return length

result = 0

max_length = 0

for i in range(1, 1000000):
	length = collatz_seq_len(i)
	if length > max_length:
		result = i
		max_length = length

print(result)