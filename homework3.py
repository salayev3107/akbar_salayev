import random
computer = random.randint(1,100)
urinishlar = 0
while True:
  player = input('guess the number: ')
  player = int(player)
  if player<computer:
    print('Kattaroq son kiriting')
    urinishlar+=1
  elif player>computer:
    print('Kichikroq son kiriting')
    urinishlar+=1
  else:
    player==computer
    print(f'you win,the number was {computer}')
    print('sizni urinishlaringiz:', urinishlar)
    break



# math funksiyalari

# math ceil
import math 
print(math.ceil(2.6)) # returns 3 
print(math.ceil(1.1)) # returns 2

# fabs()
print(math.fabs(-5.5)) # returns 5.5
print(math.fabs(5.4))  # returns 5.4

# floor()
print(math.floor(4.6))  # returns 4
print(math.floor(3.2))  # returns 3

# exp(x) = e**x
print(math.exp(0))  # returns 1
print(math.exp(1))  # returns 2.718281828459045

# sin(x)
from math import pi
print(math.sin(0))  # returns 0
print(math.sin(pi/2)) #  returns 1

# cos(x)
print(math.cos(-pi))  # returns -1
print(math.cos(pi/3)) # returns 1/2

# tan(x)
print(math.tan(3*pi/4))  # returns -1
print(math.tan(pi/4))  # returns 0.9999=1

# degrees(x)
print(math.degrees(pi/2)) # returns 90
print(math.degrees(pi))  # returns 180

# radians(x)
print(math.radians(180))  # returns pi=3.14159265...
print(math.radians(360)) # returns 6.283185307179586

# e 
print(math.e) # returns 2.718281828459045