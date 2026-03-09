num1 = int(input('enter your number:'))
num2 = int(input('enter your number:'))
num3 = int(input('enter your number:'))

if num1 > num2 and num1 > num3:
    print('biggest number is', num1)
elif num2 > num1 and num2 > num3:
    print('biggest number is', num2)
else:
    print('biggest number is', num3)