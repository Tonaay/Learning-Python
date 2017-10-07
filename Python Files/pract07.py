#-------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# Tony Van  
# UP821148
#-------------------------------------------------------------------------------

from graphics import *
import time
import math
import random

#Q1
def getName():
    name = input("Enter name :")
    while name.isalpha() == False:
        name = input("Invalid name, please re-enter:")
    print("Hello " + name)


# For exercise 2
def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        time.sleep(5)
        amber.setFill("yellow")
        time.sleep(5)
        red.setFill("black")
        amber.setFill("black")
        green.setFill("green")
        time.sleep(5)
        green.setFill("black")
        amber.setFill("yellow")
        time.sleep(5)
        amber.setFill("black")
        red.setFill("red")
    
#Q3
def calculateGrade(mark):
    
    # mark = eval(input("Enter coursework mark:"))
    while mark < 0 or mark > 20:
        mark = eval(input("Invalid mark, please re-enter:"))
        
    if mark >= 16 and mark <= 20:
        return "A"
    elif mark >= 12 and mark <= 15:
        return "B"
    elif mark >= 8 and mark <=11:
        return "C"
    elif mark >= 0 and mark < 8:
        return "F"
            
            
#Q4
def orderPrice():
    price = eval(input("Enter price of product (£):"))
    quantity = eval(input("Enter quantity of product:"))
    additionalQuantity = input("Are there any more products in order? (y/n):")
    
    while additionalQuantity == "y":
        nextQuantity = eval(input("Enter next quantity of product:"))
        quantity += nextQuantity
        additionalQuantity = input("Are there any more products in order? (y/n):")
       
    total = price * quantity
    print("The total order price is £{:.2f}".format(total))
    
#Q5
def drawEye(win,radius,colour):
    eye = Circle(Point(150,150),radius)
    eye.setFill(colour)
    eye.draw(win)
    
def clickableEye():
    win = GraphWin("Clickable eye",300,300)
    
    radius = 100
    
    drawEye(win,radius,"white")
    drawEye(win,radius/2,"brown")
    drawEye(win,radius/4,"black")
    
    message = Text(Point(150,280),"Click on any part of eye")
    message.draw(win)
    
    p = win.getMouse()
    pX = p.getX()
    pY = p.getY()
    distance = distanceBetweenPoints(pX,pY)
    
    while distance < 100:
        if distance > 50 and distance <= 100:
            message.setText("Sclera")
            
            p = win.getMouse()
            pX = p.getX()
            pY = p.getY()
            distance = distanceBetweenPoints(pX,pY)
        elif distance > 25 and distance <= 50:
            message.setText("Iris")
            
            p = win.getMouse()
            pX = p.getX()
            pY = p.getY()
            distance = distanceBetweenPoints(pX,pY)
        elif distance <= 25:
            message.setText("Pupil")
            
            p = win.getMouse()
            pX = p.getX()
            pY = p.getY()
            distance = distanceBetweenPoints(pX,pY)
    win.close()

def distanceBetweenPoints(p1, p2):
    return math.sqrt((150 - p1)**2 + (150 - p2)**2)

# For exercise 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32

def temperatureConverter():
    typeConverter = input("Enter conversion type (f2c or c2f):")
    
    while typeConverter == "f2c":
        f2c = eval(input("Enter temperature in fahrenheit:"))
        print(fahrenheit2Celsius(f2c))
        print()
        typeConverter = input("Enter conversion type:")
        
    while typeConverter == "c2f":
        c2f = eval(input("Enter temperature in celsius:"))
        print(celsius2Fahrenheit(c2f))
        print()
        typeConverter = input("Enter conversion type:")
    
    print("Converter stopped")
    
    
#Q7
def guessTheNumber():
    randomNumber = random.randint(1,100)
    guessesAmount = 6
    guessesRemaining = 7
    print("You have {} guesses remaining".format(guessesRemaining))
    guess = eval(input("Guess a number from 1 to 100:"))
        
    while guessesAmount > 0: 
        guessesAmount -= 1
        guessesRemaining -=1   
        
        if guess < randomNumber:
            print()
            print("Too low")
            print()
            print("You have {} guesses remaining".format(guessesRemaining))
            guess = eval(input("Guess a number from 1 to 100:"))
            
        elif guess > randomNumber:
            print()
            print("Too high")
            print()
            print("You have {} guesses remaining".format(guessesRemaining))
            guess = eval(input("Guess a number from 1 to 100:"))
        
        else:
            print()
            print("You have guessed correctly!")
            guessesAmount = -1
            guessesRemaining = -1
            
    if guessesAmount == 0:
        print()
        print("You lose! - the number was {}".format(randomNumber))

    
#Q8
def tableTennisScorer():
    win = GraphWin("Table tennis scorer")
    half = Line(Point(100,0),Point(100,200))
    half.setWidth(6)
    half.draw(win)
    
    player1 = 0
    player2 = 0

    score1 = Text(Point(50,100),player1)
    score1.draw(win)
    score2 = Text(Point(150,100),player2)
    score2.draw(win)
    winner = Text(Point(50,130),"Win")
    point = win.getMouse()
    pX = point.getX()
    
    while player1 >= 0 and player2 >= 0:
        point = win.getMouse()
        pX = point.getX()
       
        if pX < 100:
            player1 += 1
            score1.setText(player1)
            
            if player1 >= 11 and player1 >= player2 + 2:
                winner.draw(win)
                player1 = -1
            
        else:
            player2 +=1
            score2.setText(player2)
            if player2 >= 11 and player2 >= player1 + 2:
                winner.move(100,0)
                winner.draw(win)
                player2 - 1


#Q9
def clickableBoxOfEyes(columns,rows):
    rows2 = rows * 100 + 100
    columns2 = columns * 100 + 100
    
    win = GraphWin("Box of eyes",rows2, columns2)
    box = Rectangle(Point(50,50),Point(rows2 - 50,columns2 - 50))
    box.draw(win)
    message = Text(Point(rows2/2,columns2-25),"")
    message.draw(win)
    centreEyeX = []
    centreEyeY = []
    
    for i in range(rows):
        for j in range(columns):
            drawEye2(win,Point(i*100+100,j*100+100),50,"white")
            drawEye2(win,Point(i*100+100,j*100+100),25,"lightblue")
            drawEye2(win,Point(i*100+100,j*100+100),12.5,"black")
            
            centrePoint = i*100+100
            centreEyeX.append(i*100+100)
            centreEyeY.append(j*100+100)

    point = win.getMouse()
    pointX = point.getX()
    pointY = point.getY()
    
    while pointX > 50 and pointX < rows*100+50 and pointY > 50 and pointY < columns*100+50:
        temp = distanceBetweenPoints2(centreEyeX[0], centreEyeY[0], pointX, pointY)
        
        for i in range(rows*columns):
            distance = distanceBetweenPoints2(centreEyeX[i], centreEyeY[i], pointX, pointY)
            if temp >= distance:
                temp = distance
                newX = centreEyeX[i]
                newY = centreEyeY[i]
            
            
        #nearest centre point
        distance = distanceBetweenPoints2(pointX, pointY, newX, newY)
        
        
        if distance > 50:
            message.setText("Between Eyes")
            
        else:
            message.setText("Eye at row {}, column {}".format(newY//100, newX//100))
    
        point = win.getMouse()
        pointX = point.getX()
        pointY = point.getY()
        
        
        
    win.close()

        
def drawEye2(win,point,radius,colour):
    eye = Circle(point,radius)
    eye.setFill(colour)
    eye.draw(win)
    
def distanceBetweenPoints2(p1, p2, p3, p4):
    return math.sqrt((p3 - p1)**2 + (p4 - p2)**2)

    
#Q10
def findTheCircle():
    win = GraphWin("Circle game")
    
    x = random.randint(30,170)
    y = random.randint(30,170)
    radius = 30
    circle = Circle(Point(x,y),radius)
 
    previousAttempt = 30
    attempts = 10
    score  = 10
    
    points = Text(Point(100,20),"")
    points.draw(win)
    message = Text(Point(100,180),"")
    message.draw(win)
    winner = Text(Point(100,40),"Click to continue")
    
    while attempts >= 1:
        p = win.getMouse()
        pX = p.getX()
        pY = p.getY()
        distance = distanceBetweenPoints3(Point(pX,pY),Point(x,y))
        
        if distance > 30:
            attempts -= 1
            score -= 1
         
            if distance > previousAttempt:
                message.setText("Getting further away")
                previousAttempt = distance
            else:
                message.setText("Getting closer")
                previousAttempt = distance
        else:
            points.setText("{} Points".format(score))
            winner.draw(win)
            circle.draw(win)
            win.getMouse()
            circle.undraw()
            winner.undraw()
            message.setText("")
            score += 10
            attempts = 10
            radius = radius * 0.90
            x = random.randint(30,170)
            y = random.randint(30,170)
            circle = Circle(Point(x,y),radius)
            
    message.setText("You lose")
    points.setText("{} Points".format(score))
    circle.draw(win)
    
    
def distanceBetweenPoints3(p1, p2):
    return math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)
    
            
    
           
            
        
        