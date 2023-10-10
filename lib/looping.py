#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
        print("Happy New Year!")
    

int_list = [1, 2, 3, 4, 5]

def square_integers(int_list):
    int_list = [num * num for num in int_list]
    return int_list
    
# Write a function fizzbuzz() that prints the numbers from 1 to 100. 
# For multiples of three, print "Fizz" instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five, print "FizzBuzz".

def fizzbuzz():
    i = 1

    while i <= 100:
        if i % 3 ==0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
    
