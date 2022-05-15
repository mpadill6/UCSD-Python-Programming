# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:07:55 2020

@author: mpadilla
"""

#%%Question 1
a=[1,4,9,16,25,36,49,64,81,100]
new=[elem for elem in a if elem%2==0]
print(new)

#%% Question 2
import random #import random module
print("This is a random number guessing game!")
NUMBER=random.randint(0,100) #Generate random number
Max_Attempts=int(input("Please select the max number of attempts for guessing: ")) #Set Max Attempts number for guessing
Attempts=1 #Initialize Attempt Counter
while Attempts<=Max_Attempts: #While loop for when attempt is lower than max_attempt
    Guess=int(input("Please type in your guess: ")) #prompt user for guess
    if Guess==NUMBER:       #situation where user guesses correctly
        print("Congratulations you guessed correctly!")
        print("You took",Attempts,"to guess correctly. ")
        break               #break out of loop and terminate program if guess is correct
    elif Guess<NUMBER:      #situation where Guess is lower than correct number
        print("The guessed number is lower than the correct number.")
        Attempts+=1
    elif Guess>NUMBER:      #situation where Guess is larger than correct number
        print("The guessed number is greater than the correct number.")
        Attempts+=1
if Attempts>Max_Attempts:  #situation where user has run out of attempts and loses game.
    print("Sorry you have run out of your",Attempts-1,"attempts. GAME OVER.")
    print("The correct number was:",NUMBER)
#%% Question 3
print ("This is the hearts and spades game!")
import random
Digit_One=random.randint(0,9) #random int 1
Digit_Two=random.randint(0,9) #random int 2
while Digit_Two==Digit_One:
    Digit_Two=random.randint(0,9) #check if repeated and get new number if so.
Digit_Three=random.randint(0,9) #random int 3
while Digit_Three==Digit_One or Digit_Three==Digit_Two:  #check for repeat on 1 or 2 
    Digit_Three=random.randint(0,9)
Digit_Four=random.randint(0,9)
while Digit_Four==Digit_One or Digit_Four==Digit_Two or Digit_Four==Digit_Three: #check for repeat on 1/2/3
    Digit_Four=random.randint(0,9)
Number_List=[Digit_One,Digit_Two,Digit_Three,Digit_Four]  #List with 4 digits
Attempts=1  #Attempt counter
Max_Attempts=1000000000000000000     #arbitrarily large amount of attempts
while Attempts<Max_Attempts:
    hearts=0
    hits=0
    Guess=list(input("Please guess a 4 digit number from 0000-9999: "))
    for i in range(4): #check each digit in list of 4 digits for matching in correct spot
        if int(Number_List[i])==int(Guess[i]):
            hearts+=1
    for j in range(4): #check if digit appears in list, also counts for hearts here.
        if int(Guess[j]) in Number_List:
            hits+=1
    print(hearts,"Hearts",hits-hearts,"Spades") #spades is the subtraction of hits and hearts
    Attempts+=1
    if hearts==4:
        print("You have correclty guessed the number!")
        print("It took you", Attempts-1,"to guess correctly.")
        break
#%% Question 4
numbers=int(input("Please type how many numbers in the Fibonacci sequence to output: "))
Fib=[]
def Fibonacci(n):
    if n==1:
        return 0   
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print("The Fibonacci Sequence with length of", numbers,"is:")
for i in range(1,numbers+1): #Run Fibonnaci recursive as many times as user chooses.
    print(Fibonacci(i))
#%% Question 5
number=int(input("Please selects a number: "))
def prime(n):
    a=n-1
    for i in range(a,1,-1): #Divide number by all previous numbers up to 2.
        if n%i!=0: #if not divisble by number, pass to next.
            pass
        elif n%i==0: #if divisible print "not prime" and break
            print("This number is not prime!")
            break
        if i==2 and n%i!=0: #if reaches 2 and not divisible, it is called prime
            print("This number is prime!")
    if n==2: #case in which 2 is chosen.
        print("This number is prime!")
prime(number)