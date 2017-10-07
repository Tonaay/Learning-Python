# Practical Worksheet 3: Graphical Programming
# Liem Tony Van, up821148

from graphics import *
import math

#Q1
def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    
    arm1 = Line(Point(50, 90), Point(100, 90))
    arm1.draw(win)
    
    arm2 = Line(Point(100, 90), Point(150, 90))
    arm2.draw(win)
    
    leg1 = Line(Point(100, 120), Point(70, 160))
    leg1.draw(win)
    
    leg2 = Line(Point(100, 120), Point(130, 160))
    leg2.draw(win)

#Q2
def drawCircle():
    win = GraphWin("Circle drawer")
    radius = eval(input("Enter radius :"))
    
    circle = Circle(Point(100,100), radius)
    circle.draw(win)
#Q3    
def drawArcheryTarget():
    win = GraphWin("Archery Target Drawer")
    
    centre = Point(100,100)
    blueCircle = Circle(centre, 60)
    blueCircle.setOutline("blue")
    blueCircle.setFill("blue")
    blueCircle.draw(win)
    
    redCircle = Circle(centre, 40)
    redCircle.setOutline("red")
    redCircle.setFill("red")
    redCircle.draw(win)
    
    yellowCircle = Circle(centre, 20)
    yellowCircle.setOutline("yellow")
    yellowCircle.setFill("yellow")
    yellowCircle.draw(win)

#Q4    
def drawRectangle():
    win = GraphWin("Rectangle drawer")
    
    rectangleWidth = eval(input("Enter width of rectangle: "))
    rectangleHeight = eval(input("Enter height of rectangle: "))
    
    p1 = (200 - rectangleWidth)/2
    p2 = (200 - rectangleHeight)/2
    
    widthPoint = rectangleWidth + p1
    HeightPoint = rectangleHeight + p2
    
    rectangle = Rectangle(Point(p1,p2),Point(widthPoint,HeightPoint)) 
    rectangle.draw(win)

#Q5
def blueCircle():
    win = GraphWin("Click on location")
    p = win.getMouse()
    
    x = p.getX()
    y = p.getY()

    circle = Circle(Point(x,y),50)
    circle.draw(win)
    
#Q6    
def drawLine2():
    win = GraphWin("10 Line drawer")
    message = Text(Point(100,100), "Click on first point")
    message.draw(win)
    
    for i in range(10):
        
        pointOne = win.getMouse()
        message.setText("Click on next point")
        pointTwo = win.getMouse()
        
        line = Line(pointOne, pointTwo)
        line.draw(win)
         
    message.setText("")

#Q7    
def tenStrings():
    win = GraphWin("Ten Strings", 400,300)
    message = Text(Point(200, 50), "Enter String & click mouse")
    message.draw(win)
    
    inputBox = Entry(Point(200,20),10)
    inputBox.draw(win)
        
    for i in range(10):
    
        point = win.getMouse()
        
        message2 = Text(point, inputBox.getText())
        message2.draw(win)
        
    message.setText("")    
        
#Q8
def tenColouredRectangles():
    
    win = GraphWin("Ten Coloured Rectangles", 500,500)
    message = Text(Point(250,50), "Enter colour blue and click twice for rectangle")
    message.setSize(8)
    message.draw(win)
    
    inputBox = Entry(Point(250,20),10)
    inputBox.draw(win)
    
    for i in range(10):
        
        
        p1 = win.getMouse()
        p2 = win.getMouse()
        
        rectanglez = Rectangle(p1,p2)
        rectanglez.setFill(inputBox.getText())
        rectanglez.draw(win)
        
    message.setText("")
    
#Q9
def fiveClickStickFigure():
        win = GraphWin("Clicking Stick Figure", 500,600)
        pointOne = win.getMouse()
        x1 = pointOne.getX()
        y1 = pointOne.getY()
        
        headCentre = Circle(pointOne,20)
        headCentre.draw(win)
        
        pointTwo = win.getMouse()
        headCentre.undraw()
        
        x2 = pointTwo.getX()
        y2 = pointTwo.getY()
        
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        head2 = Circle(Point(x1,y1), distance)
        head2.draw(win)
        
        pointThree = win.getMouse()
        
        y3 = pointThree.getY()
        y4 = y1 + distance
        
        body = Line(Point(x1, y3), Point(x1, y4))
        body.draw(win)
        
        pointFour = win.getMouse()

        x4 = pointFour.getX()
        y5 = pointFour.getY()
        y6 = y1 + (y3/5)
        arm = x1 - x4
        secondArm = x1 + arm
        
        arm1 = Line(Point(x4,y5),Point(x1,y6))
        arm1.draw(win)
        arm1 = Line(Point(secondArm,y5),Point(x1,y6))
        arm1.draw(win)
        
        pointFive = win.getMouse()
        
        xLeg = pointFive.getX()
        yLeg = pointFive.getY()
        leg = x1 - xLeg
        secondLeg = x1 + leg
        
        legs = Line(Point(xLeg,yLeg), Point(x1,y3))
        legs.draw(win)
        legs = Line(Point(secondLeg,yLeg), Point(x1,y3))
        legs.draw(win)
        
#Q10
def plotRainFall():
    
        win = GraphWin("Rainfall Histogram", 300,400)
        x = [10,50,90,130,170,210,250]
        
        inputBox = Entry(Point(50,15),10)
        inputBox.draw(win)
        
        for i in range(7):
            
            win.getMouse()
            numberPoint = x[i] + 20
            x2 = x[i] + 40
            height = inputBox.getText()
            
            rainFallNumber = Text(Point(numberPoint,395), height)
            rainFallNumber.setFill("green")
            rainFallNumber.draw(win)
            
            newHeight = (380 - int(height))

            
            rainBar = Rectangle(Point(x[i],newHeight), Point(x2,380))
            rainBar.setOutline("white")
            rainBar.setFill("pink")
            rainBar.draw(win)
        