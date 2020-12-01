a, b, h = int(input()), int(input()), int(input()),
if b >= h >= a:
    print('Normal')
elif h < a:
    print('Deficiency')
elif h > b:
    print('Excess')
