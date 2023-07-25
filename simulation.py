import random
while True:
    x = input('choose roll amount (500k): ')
    x = int(x)
    sum = 0
    for i in range(x):
        roll = random.randint(1,1000)
        if roll <= 650:
            print('access keycard')
            sum = sum + 166500
        elif roll <= 900:
            print('blurry keycard')
            sum = sum + 250000
        elif roll <= 965:
            print('yellow keycard')
            sum = sum + 2400000
        elif roll <= 985:
            print('black keycard')
            sum = sum + 4000000
        elif roll <= 993:
            print('violet keycard')
            sum = sum + 5800000
        elif roll <= 997:
            print('blue keycard')
            sum = sum + 15500000
        elif roll <= 999:
            print('green keycard')
            sum = sum + 28700000
        else:
            print('red keycard')
            sum = sum + 35000000

    spent = x*500000
    print(f'Spent: {spent}')
    print(f'Money made {sum}')
    profit = sum - spent
    print(f'Net profit: {profit}')
    percentage = sum*100//spent
    print(f'Percentage return {percentage}%')
    print('')
    continue