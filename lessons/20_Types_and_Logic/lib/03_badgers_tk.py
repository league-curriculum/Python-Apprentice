"""

* If the number is evenly divisible by 5, print 'fizz'
* If the number is evenly divisible by 3, print 'buzz'
* If it is divisible by neither, print the number


"""


import  jtl_lib  # type: ignore
jtl_lib.add_path()
from lib.badgers import FizzBuzzer

# Make fizzbuzz function work with graphics
# Inside the fizzbuzz function:
#   return 'snake' to display the snake image, 
#   return 'badger' to display the badger image, and 
#   return 'mushroom' to display the mushroom image.
#   return a number to display the number in black text.
#   If you return anything else it will display in red. 

# You can change the image files in lib/images to anything you like, but they have to be .gif
# and have the names snake.gif, badger.gif, and mushroom.gif


def fizzbuzz(number):
    
    # Put your fizzbuz code here. 
    
    return 'mushroom' # Always show a snake


fb = FizzBuzzer(fizzbuzz)
fb.run()
