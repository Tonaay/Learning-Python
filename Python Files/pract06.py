#-------------------------------------------------------------------------------
# Practical Worksheet 6: if statements and for loops
# Tony Van
# UP821148
#-------------------------------------------------------------------------------

from graphics import *
import math
import random

#Q1
def fastFoodOrderPrice():
    orderPrice = eval(input("Enter order price : "))
    deliveryCharge = orderPrice + 1.50
    
    if orderPrice >= 10:
        print("£{:.2f} with no delivery costs".format(orderPrice))
    else:
        print("£{:.2f} with delivery cost of £1.50".format(deliveryCharge))

#Q2
def whatToDoToday():
    temperature = eval(input("Enter temperature today : "))
    
    if temperature > 25:
        print("Swim in the sea")
        
    elif temperature >= 10 and temperature <= 25:
        print("Shop at Gunwharf Quays is a good idea")
        
    else:
        print("It's best to watch a film at home")
        
#Q3
def displaySquareRoots(start, end):
    
    for i in range(start,end+1):
        
        print("The square root of {} is {:.3f}".format(start, math.sqrt(start)))
        start += 1
    
#Q4
def calculateGrade(mark):
    if mark >= 16 and mark <= 20:
        return "A"
    elif mark >= 12 and mark <= 15:
        return "B"
    elif mark >= 8 and mark <=11:
        return "C"
    elif mark > 0 and mark < 8:
        return "F"
    else:
        return "X"
    

#Q5
def peasInPod(peas):
    win = GraphWin("Peas in a pod",(peas*100),100)
    
    centre = 50
    for i in range(peas):
        circle = Circle(Point(centre,50),50)
        circle.setFill("lightgreen")
        circle.setWidth(0)
        circle.draw(win)
        centre += 100
    
#Q6
def ticketPrice(distance,age):
    
    ticketNormal = (distance * 0.15) + 3
    ticketDiscount = ticketNormal - (ticketNormal * 0.4)
    if age < 60 and age > 15:
        return "Your ticket will cost £{:.2f}".format(ticketNormal)
    elif age < 0:
        return "Invalid age"
    else:
        return "Your ticket will cost £{:.2f} with a discount of 40% off".format(ticketDiscount)
        
    
#Q7
#Only used for 4 squares
def numberedSquare(number):
    n1 = number
    
    spacedNumbers = ""
    
    for i in range(number):
        print("{} {} {} {}".format(n1,n1+1,n1+2,n1+3))
        n1 -= 1
        
def numberedSquare2(number):
    
    for i in range(number, 0, -1):
        for j in range(i, i + number):
            
            adjust = j
            
            print("{:>2}".format(adjust), end=" ")
        print("")
            
            
# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)
    

# For exercise 8 
def drawColouredEye(win, centre, radius, colour):
    drawCircle(win, centre, radius, "white")
    drawCircle(win, centre, radius/2, colour)
    drawCircle(win, centre, radius/4, "black")
    
def eyePicker():
    
    centreX = eval(input("Enter x coordinate : "))
    centreY = eval(input("Enter y coordinate : "))
    radius = eval(input("Enter radius of eye : "))
    colour = input("Enter eye colour : ")
    
    if colour == "blue" or colour == "grey" or colour == "green" or colour == "brown":
        win = GraphWin("Eye colour picker")
        drawColouredEye(win, Point(centreX,centreY), radius, colour)
    else:
        print("Not a valid eye colour")
        
#Q9
def drawPatchWindow():
    win = GraphWin("Patch designs", 100,100)
    
    for i in range(10):
        
        point1 = Point(i*5,i*5)
        point2 = Point(100-(i*5), 100-(i*5))
        square = Rectangle(point1, point2)
        square.setWidth(0)
        
        if i%2 == 0:
            square.setFill("red")
        else:
            square.setFill("white")
        
        square.draw(win)
        
def drawPatchWindow2():
    win = GraphWin("Patch designs", 100,100)
    x = 0
    y = 0
    x2 = 100
    y2 = 100
    for i in range(10):
      
        point1 = Point(x,y)
        point2 = Point(x2,y2)
        square = Rectangle(point1, point2)
        square.setWidth(0)
        
        if i%2 == 0:
            square.setFill("red")
        else:
            square.setFill("white")
        
        square.draw(win)
        x += 5
        y += 5
        x2 -= 5
        y2 -= 5
       
#Q10
def drawPatch(win, x, y, colour):
    width = 0
    height = 100
    for i in range(2):
        
        for i in range(3):
            for i in range(10):
        
                point1 = Point((i*5)+x, width+(i*5))
                point2 = Point(y-(i*5), height-(i*5))
                square = Rectangle(point1, point2)
                square.setWidth(0)
        
                if i%2 == 0:
                    square.setFill(colour)
                else:
                    square.setFill("white")
        
                square.draw(win)
            x += 100
            y += 100
        x = 0
        y = 100
        width += 100
        height += 100
        
def drawPatchWork():
    win = GraphWin("Patch designs", 300,200)
    x = 0
    y = 100
    colour = input("Enter colour of patches :")
    
    drawPatch(win, x, y, colour)
    
#Q11
def eyesAllAround():
    win = GraphWin("Eyes all around", 500,500)
    colour = ["blue", "grey", "green", "brown"]
    
    for i in range(30):
        centre = win.getMouse()
        #using Modulo to find the remainder of i/4 to loop the list
        drawColouredEye(win, centre, 30, colour[i % 4])
        
#Q12
def archeryGame():
    win = GraphWin("Archery Game")
    centre = Point(100,100)
    radius = 80
    
    drawCircle(win, centre, radius, "blue")
    drawCircle(win, centre, radius/2,"red")
    drawCircle(win, centre, radius/4, "yellow")
    
    points = 0
    
    for i in range(10):
        
        p = win.getMouse()
        pX = p.getX()
        pY = p.getY()
        
        randomizer = random.randint(1,100)
        pX = pX + randomizer
        pY = pY + randomizer
        
        hit = Circle(Point(pX,pY),2)
        hit.setFill("black")
        hit.draw(win)
        
        distance = distanceBetweenPoints(Point(pX,pY), Point(100,100))

        if distance > 40 and distance <= 80:
            points += 2
        elif distance > 20 and distance <= 40:
            points += 5
        elif distance <= 20:
            points += 10
        else:
            points += 0
            
    score = Text(Point(100,190), "You have scored {} points".format(points))
    score.draw(win)
        
        
def distanceBetweenPoints(p1, p2):
    return math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)
    
