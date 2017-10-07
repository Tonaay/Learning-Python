#-------------------------------------------------------------------------------
# Practical Worksheet 5: Using functions
# Tony Van
# UP821148
#-------------------------------------------------------------------------------

from graphics import *
import math

# For exercises 1 and 2
def areaOfCircle(radius):
    return math.pi * radius ** 2
    
def circumferenceOfCircle(radius):    
    return 2 * math.pi * radius
    
def circleInfo():
    radius = eval(input("Enter radius : "))
    print("The area is {:.3f} and circumference is {:.3f}".format
    (areaOfCircle(radius),circumferenceOfCircle(radius)))
    
# For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)        
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawBrownEyeInCentre():
    win = GraphWin()
    centre = Point(100,100)
    radius = [60,30,15]
    colour = ["white", "brown", "black"]
    for i in range(3):
        drawCircle(win, centre, radius[i], colour[i])
#Q4
def drawStars(width, height):
    for i in range(height):
        print("*" * width)
    

def drawBlockOfStars():
    x = eval(input("Enter width : "))
    y = eval(input("Enter height : "))
    drawBlockOfStars(x,y)
    
    
def drawLetterE():
    drawStars(8,2)
    drawStars(2,2)
    drawStars(5,2)
    drawStars(2,2)
    drawStars(8,2)


# For exercise 5
def drawBrownEye(win, centre, radius):
    win = GraphWin()
    circle = Circle(centre, radius)        
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)
    
def drawPairOfBrownEyes():
    win = GraphWin("Pair of brown eyes", 270, 200)
    centre = Point(75,100)
    centre2 = Point(195,100)
    radius = [60,30,15]
    colour = ["white", "brown", "black"]
    for i in range(3):
        drawCircle(win, centre, radius[i], colour[i])
        drawCircle(win, centre2, radius[i], colour[i])
        
#Q6
def distanceBetweenPoints(p1, p2):
    return math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)
    
def points():
    p1 = Point(1,2)
    p2 = Point(4,6)
    print(distanceBetweenPoints(p1, p2))
    
    
#Q7
def drawBlocks(space1, width1, space2, width2, height):
    for i in range(height):
        print(" " * space1 + "*" * width1 + " " * space2 + "*" * width2)

def drawBlocks2():
    drawBlocks(0,5,4,3,2)
    
def drawLetterA():
    drawBlocks(4,8,0,0,2)
    drawBlocks(3,2,6,2,2)
    drawBlocks(3,10,0,0,2)
    drawBlocks(3,2,6,2,3)
    
#Q8
def drawFourPairsOfEyes2():
    win = GraphWin("Four pairs of eyes", 1000,600)
    
    colour = ["white", "brown", "black"]
    
    for i in range(4):
        
        pair1 = win.getMouse()
        pair2 = win.getMouse()
    
        radiusCircumference = math.sqrt((pair2.getX() - pair1.getX())**2 + (pair2.
        getY() - pair1.getY())**2)
    
        radi = radiusCircumference / 2
        brown = radi / 2
        black = brown / 2
    
        radius = [radi,brown,black]

        for i in range(3):
            drawCircle(win, pair1, radius[i], colour[i])
            drawCircle(win, pair2, radius[i], colour[i])
    
#Q9
def displayTextWithSpaces(win,size,word,point):
    wordList = list(word)
    spacedLetters = ""
    
    for letter in wordList:
        spacedLetters += letter + " "
        
    sentence = Text((point), spacedLetters)
    sentence.setSize(size)
    sentence.draw(win)
    

def constructVisionChart():
    win = GraphWin("Vision chart",500,220)
    inputBox = Entry(Point(250,20),20)
    inputBox.draw(win)
    
    size = [30,25,20,15,10,5]
    height = [50,80,110,140,170,200]
    
    
    for i in range(6):
        win.getMouse()
        word = inputBox.getText()
        
        displayTextWithSpaces(win,size[i],word,Point(250,height[i]))
        
    inputBox.undraw()

#Q10
def drawStickFigureFamily():
    win = GraphWin("Stick family", 500,180)
    
    drawStickFigure(win,Point(100,60),23)
    drawStickFigure(win,Point(200,60),20)
    drawStickFigure(win,Point(300,60),15)
    drawStickFigure(win,Point(400,60),10)


def drawStickFigure(win,point,size):
    
    x = point.getX()
    y = point.getY()

    head = Circle(point, size)
    head.draw(win)
    
    scaleHeight = y+size+40
    
    body = Line(Point(x, y+size), Point(x, scaleHeight))
    body.draw(win)
    
    armHeight = y+size+10
    arm1 = Line(Point(x-size*2, armHeight), Point(x, armHeight))
    arm1.draw(win)
    
    arm2 = Line(Point(x, armHeight), Point(x+size*2, armHeight))
    arm2.draw(win)
    
    leg1 = Line(Point(x, scaleHeight), Point(x-size, scaleHeight+40))
    leg1.draw(win)
    
    leg2 = Line(Point(x, scaleHeight), Point(x+size, scaleHeight+40))
    leg2.draw(win)
    
    
  