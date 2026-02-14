# Programme to cheak EVEN ODD

# number = int(input("Enter the number: "))

#if number % 2 == 0:
    #print("even")

#else:
    #print("odd") 

# prime number check programme

#num = int(input("Enter the number: "))

#if num > 1:
    #for i in range(2, num):
        #if num % i == 0:
            #print("Not Prime")
            #break
    #else:
        #print("Prime Number")

#else:
    #print("Not Prime")


# Programe for fibonacci Series
#n = int(input("Enter number of terms: "))

#a, b = 0, 1

#for i in range(n):
    #print(a, end="")
    #a, b = b, a+b

# Palindrome String

#text = input("Enter a srting: ")

#if text == text[::-1]:
    #print("Palindrome")

#else:
    #print("Not Palindrome")

#Reverse list

#numbers = [1, 2, 3, 4, 5]

#numbers.reverse()

#print("Reversed list:", numbers)


#Word count in sentence

#sentence = input("Enter a sentence: ")
#words = sentence.split()

#print("word count: ", len(words))

#  Simple calculater function

#def calculator(a, b, operator):
    #if operator == "+":
        #return a + b
    #elif operator == "-":
        #return a - b
    #elif operator == "*":
        #return a* b
   # elif operator == "/":
        #return a/b
    
#num1 = float(input("Enter the first number: "))
#num2 = float(input("Enter the second number: "))

#op  = input("Enter the operator(+ , -, *, /): ")

#result = calculator(num1, num2, op)
#print("Result: ", result)

#Number Guessing Mini Game

import random
secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess number between 1-10: "))

    if guess == secret_number:
        print("Correct ")
        break
    elif guess > secret_number:
        print("Too high")
    else:
        print("Too low")




