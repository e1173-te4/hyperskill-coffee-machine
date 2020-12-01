# put your python code here
sequence = input().split()
x = input()
positions = [str(i) for i in range(len(sequence)) if sequence[i] == x]
print(' '.join(positions) if len(positions) > 0 else 'not found')
