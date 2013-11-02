sequence_length = {1: 0}

def collatz_sequence_length(nb):
    global sequence_length

    if nb in sequence_length:
        return sequence_length[nb]
    
    if nb%2 == 0:
        length = collatz_sequence_length(nb//2)
    else:
        length = collatz_sequence_length(3*nb + 1)
        
    length += 1
    sequence_length[nb] = length
    return length

resultat = 0
longest = 0

for i in range(1, 1000000):
    length = collatz_sequence_length(i)
    if length > longest:
        resultat = i
        longest = length

print(resultat)
