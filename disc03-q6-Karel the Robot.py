#这道题似乎没有题解,所以写在下面
#I found that there isn't an official solution for this question, so I wrote one below (it may be incorrect).
# write any code you want
from karel.stanfordkarel import *

def main():
   # your code here...
   if front_is_clear():
      move()
      if front_is_clear():
         move()
      main()
   if front_is_blocked():
      turn_left()
      turn_left()
   else:
      move()