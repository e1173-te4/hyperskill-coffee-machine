# put your python code here
number = int(input())
sum = number
sq = abs(number ** 2)
while sum != 0:
    number = int(input())
    sum += number
    sq += abs(number ** 2)
print(sq)
