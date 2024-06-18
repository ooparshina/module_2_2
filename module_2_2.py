first = int(input('Напишите первое число '))
second = int(input('Напишите второе число '))
third = int(input('Напишите третье число '))

if (first + second) == (third * 2):
    print(0)
elif first ==  second or first == third or second == third:
    print(1)
else:
    print(3)
