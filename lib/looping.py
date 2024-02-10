#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")
    pass

def square_integers(int_list):
    squared_list = [x**2 for x in int_list]
    return squared_list

def fizzbuzz():
    for i in range(1, 101):  # Loop from 1 to 100 inclusive
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
