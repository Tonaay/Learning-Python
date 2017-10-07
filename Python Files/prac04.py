#Prac04
#Liem Tony Van
#UP821148

from graphics import *
import math
import os

#Q1
def personalGreeting():
    name = input("Enter your name? : ")
    print("Hello {}, nice to meet you!".format(name))
    
#Q2    
def formalName():
    firstName = input("Enter first name : ")
    surName = input("Enter surname : ")
    print("{}. {}".format(firstName[0], surName))
    
#Q3    
def kilos2Pounds():
    kilos = eval(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos    
    print("The weight {:.2f} kilos to pounds is {:.2f}".format(kilos,pounds))
    
#Q4
def generateEmail():
    firstName = input("Enter first name : ")
    surName = input("Enter surname : ")
    
    year = eval(input("Enter year : "))
    yearString = str(year)
    
    print("{}.{}.{}.myport.ac.uk".format(firstName[:4],surName[0],
    yearString[-2:]).lower())
    
#Q5
def gradeTest():
    gradeInput = eval(input("Enter grade : "))
    grade = "FFFFCCBBAAA"
    print("Your grade is {}".format(grade[gradeInput]))
    
#Q6
def graphicLetters():
    textInput = input("Enter a word : ")
    counter = textInput.count('')
    print(counter)

    win = GraphWin("Letter Input",500,300)
    
    for i in range(counter-1):
        p = win.getMouse()
        
        x = p.getX()
        y = p.getY()
        
   
        letterInput = Text(Point(x,y), "{}".format(textInput[i]))
        letterInput.setSize(30)
        letterInput.draw(win)
    
#Q7
def singASong():
    songName = input("Enter song name : ")
    songLines = eval(input("How many lines for the song? : "))
    songRepeats = eval(input("Input amount of repeated words : "))
    for i in range(songLines+1):
        print("{}".format((songName + " ")* songRepeats))
        
#Q8
def exchangeTable():
    for i in range(21):
        pounds = i
        euros = i / 1.15
        print("£{:<2} = €{:<.2f}".format(pounds,euros))
        
#Q9
def makeAcronym():
    phrase = input("Enter phrase : ")
    words = phrase.split()
    for letter in words:
        print(letter[0].upper(), end="")
        
#Q10        
def nameToNumber():
    phrase = input("Enter phrase : ")
    phrase = phrase.lower()
    numberList = []
    for i in phrase:
        number = ord(i) - 96
        numberList.append(number)
    total = sum(numberList)
    print(numberList)
    print(total)
    
#Q11
def fileInCaps():
    fileName = input("Enter file name : ")
    inFile = open(fileName + ".txt", "r")
    contents = inFile.read()
    print(contents.upper())
    
#Q12
def rainfallChart():
    numbers = [None] * 9
    cities = [None] * 9
    
    inFile = open("rainfall.txt", "r")
    listLines = inFile.readlines()
    inFile.close()
    
    for i in range(9):
        splitText = listLines[i].split()
        numbers[i] = splitText[1]
        cities[i] = splitText[0]
        stars = "*" * int(numbers[i])
        print("{:<12} {:<12}".format(cities[i], stars))  
        
#Q13
def rainfallInInches():
    numbers = [None] * 9
    cities = [None] * 9
    
    inFile = open("rainfall.txt", "r")
    listLines = inFile.readlines()
    inFile.close()
    
    for i in range(9):
        splitText = listLines[i].split()
        numbers[i] = splitText[1]
        cities[i] = splitText[0]
        inches = int(numbers[i]) / 25.4
        print("{:<12} {:.2f}".format(cities[i], inches))
        
def graphicalRainfallChart():
    
    win = GraphWin("Rainfall chart", 570,500)
    numbers = [None] * 9
    cities = [None] * 9    
    
    inFile = open("rainfall.txt", "r")
    listLines = inFile.readlines()
    inFile.close()
    x = 10
    

    for i in range(9):
        splitText = listLines[i].split()
        numbers[i] = splitText[1]
        cities[i] = splitText[0]
        
        numberPoint = x + 35
        x2 = x + 60

        height = cities[i]
            
        rainFallNumber = Text(Point(numberPoint,295), height)
        rainFallNumber.setFill("green")
        rainFallNumber.setSize(8)
    
        rainFallNumber.draw(win)
            
        newHeight = (280 - int(numbers[i]))

            
        rainBar = Rectangle(Point(x,newHeight), Point(x2,280))
        rainBar.setOutline("white")
        rainBar.setFill("black")
        rainBar.draw(win)
        print(x,x2)
        print(height)
        print(newHeight)
        x = x + 60

    print(numbers)
    print(cities)

    
#Q14
def wc():
    fileName = input("Enter file name : ")
    
    inFile = open(fileName, "r")
    listLines = inFile.readlines()
    inFile.close()

    wordCount = 0
    characterCount = 0
    
    for line in listLines:
        
        wordCount += len(line.split())
        characterCount += len(line)
    

    print("Line Count : ", len(listLines))
    print("Word Count : ", (wordCount))
    print("Character Count : ", (characterCount))


    
        
 
    

    
    
    


        
    
        
        
