seq = [int(x) for x in input()]
summ = 0
new_seq = []
for x in seq:
    summ += x
    new_seq.append(summ)
print(new_seq)
