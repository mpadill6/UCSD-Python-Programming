###Question 1
print("Question 1")
class Strings:
    def __init__(self,word): #Constructor
        self.word=word
    def get_String(self):  #Function to get string
        self.string=self.word
    def print_String(self): #Function to change string to upper with .upper()
         self.UPPER=self.string.upper()
         print("Your output string in Upper case is:",self.UPPER)
x=Strings('Hello my name is Mario and this should then be returned in uppercase')
x.get_String()
x.print_String()

#Question 2
print("Question 2")
class Calc:  #parent class with functions
    def add(self, a, b):
        return  a + b
    def subtract(self, a, b):
        return a - b
        
    def multiply(self,a,b):
        return a * b
        
    def divide(self, a, b):
        if b==0:
            raise ValueError('Cannot divide by zero!')
        return a / b
class Update_Calc(Calc):  #child class with mod function
    def mod(self, a,b):
        return a % b
Mathematical=Update_Calc() #Instantiate 
print(Mathematical.add(10,5))
print(Mathematical.subtract(10,5))
print(Mathematical.multiply(10,5))
print(Mathematical.divide(10,5))
print(Mathematical.mod(10,5))

#Question 4
print("Question 4")
fhand=open("About_Python.txt") #Create handle
countline=0 #initialize line count
countword=0 #initialize word count
for line in fhand: #for loop 
    countline+=1  #count line
    words=line.split() #split line by words
    countword=countword+len(words) #add word count of line to running sum
print("The total number of lines in the file is:", countline)
print("The total number of words in the file is:", countword)


#Question 5
print("Question 5")
fhand=open("About_Python.txt") #create handle
inp=fhand.read() #read file
def reverse (x): #define function that will reverse text
    return x [::-1] #Use negative index
y=reverse(inp)
reversefhand=open("Reverse_About_Python.txt","w") #Create new file to write reverse text
reversefhand.write(y)
reversefhand.close()



