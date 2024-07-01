import random

rand = random.randint(1,6)

while True:
    number = int(input('Think any number from 1 to 6:'))

    if(number==rand):
        print("you think a correct number!")
        break
    elif (number>rand):
        print('you think grater number.please think a small number.')
    else:
        print('you think smaller number.please think a large number.')
