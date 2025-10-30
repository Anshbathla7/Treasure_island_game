from art import treasure_art
print(treasure_art)
print('welcome to the treasure island. Your mission is to find the treasure!')
direction = input('where you wanna go! left or right. ')
if direction == 'right':
    print('game over,you died from fire. ')
elif direction == 'left':
    print('you are at the island. ')
boat = input('Now do you wanna wait or boat or you wanna swim! Press B for boat and S for swim. ')
b=boat.lower()
if b == 's':
    print('you died because you are eaten by sharks. ')
elif b == 'b':
    print('congrulations! you are at the doors. ')

doors = input('Now choose a single door in which you think you will find the treasure.Press b for blue gate or R for red gate and g for green gate. ')
d = doors.lower()
if d == 'b':
    print("you died because of bomb's trap. ")
elif d == 'r':
    print('congrulation you found the treasure. ')
else:
    print('you died because of Arrows trap. ')