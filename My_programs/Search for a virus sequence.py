# How to find a position of a sequence (e.g. virus or insertion sequence) we are interested at

DNA = 'AATAGTTCCCGGGAATAGATTT'
name = 'TAG'
indices = [] # Creates an emply list for indices
for i in range(len(DNA)):
    if DNA[i:i+3] == name:
        print(f'TAG нашлось в позиции {i}')
        indices.append(i) # Adds found indices to the indices list
print(indices)
