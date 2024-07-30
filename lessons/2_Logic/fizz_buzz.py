# TODO: Fizz Buzz

# Write a program that prints the numbers from 1 to 100. But for multiples of
# three print “Fizz” instead of the number and for the multiples of five print
# “Buzz”. For numbers which are multiples of both three and five print
# “FizzBuzz”."

#   -
#   Print your results to the console.
#   -
#   If your code is correct, the output will be:
#   -
#   1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz


for i in range(1,21):
    if i%15 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)