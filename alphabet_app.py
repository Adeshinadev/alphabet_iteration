Alphabets = 'abcdefghijklmnopqrstuvwxyz'
i = 0
for a in range(len(Alphabets)):
    print(f'{Alphabets[i:27]}{Alphabets[0:i]}')
    i = i+1


