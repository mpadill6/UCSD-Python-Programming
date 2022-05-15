# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:27:40 2020

@author: mpadilla
"""

#Question 1
footer="-"*60

print("This Program is to made to calculate age of a defined user")
name=input("Please input your name: ") #Ask user for name
age=int(input("Please input your current age as of today: ")) #Ask user for age
years_ahead=100-age #Calculate how many more years to reach 100
age_100=2020+years_ahead #Calculate year at which user is 100
print("Hello",name,"you will be 100 years old on this date in the year of",age_100) #Print final statement with name and year 100
print("End of Question 1")
print(footer)
#%%
#Question 2
a=[1,1,2,3,5,8,13,21,34,55,89] #List 1
b=[1,2,3,4,5,6,7,8,9,10,11,12,13] #List 2

set1=set(a) #Change list to set in order to remove duplicates. Also allows for intersection function
set2=set(b) #Change list to set in order to remove duplicates. Also allows for intersection function

intersection=list(set1.intersection(set2)) #Run intersection function on sets and change final answer to list
print("The list with common elements is",intersection) #print answer
print("End of Question 2")
print(footer)

#%%
#Question 3
SampleString=input("Please enter a long string of words: ") #input a list of words
SampleList=SampleString.split() #Make a list with each word as entry
String_Backward=SampleList[-1:-len(SampleList)-1:-1] #make new list by using negative index notation
final=" ".join(String_Backward) #join entries of reverse list
print(final)
print("End of Question 3")
print(footer)

#%%
#Question 4
a=[5,10,15,20,25] #sample list
temp=[] #make blank list to append
def First_Last(a): #define function
    temp.append(a[0]) #append first entry of list
    temp.append(a[-1]) #append last entry of list
First_Last(a) #run function
print("Your new list with the first and last numbers of the entered list respectively are", temp) #return final list
print("End of Question 4")
print(footer)
#%%
#Question 5
str1="America"
str2="Japan"
first_1=str1[0] #First letter of string 1
first_2=str2[0] #First letter of string 2
middle_1=str1[int((len(str1)-1)/2)] #middle letter of string 1
middle_2=str2[int((len(str2)-1)/2)] #middle letter of string 2
last_1=str1[-1] #last letter of string 1
last_2=str2[-1] #last letter of string 2
output=first_1+first_2+middle_1+middle_2+last_1+last_2 #Overload + operator to concatenate string elements
print(output)
print("End of Question 5")
print("End of Assignment")
