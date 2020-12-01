dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
ok = True
for word in input().split():
    if word not in dictionary:
        print(word)
        ok = False
if ok:
    print('OK')