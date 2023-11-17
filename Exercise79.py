from random import randrange
number = 100
max_num = randrange(1, number + 1)
print(max_num)
updates = 0
count = 1
while count < number:
    current = randrange(1, number + 1)
    if current > max_num:
        max_num = current
        updates = updates+ 1
        print(current,  '<= Update')
    else:
        print(current)
    count = count+ 1
print('The maximum number found was', max_num)
print('The maximum number was updated', updates, 'times')