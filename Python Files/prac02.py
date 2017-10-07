#Tony Van
#UP821148
import math


def circumferenceOfCircle():
    radius = eval(input("Enter Radius :"))
    circumference = 2 * math.pi * radius
    print("The circumference is", circumference)
    
def areaofCircle():
    radius = eval(input("Enter Radius :"))
    Area = math.pi * radius**2
    print("The area is", Area)
    
def costOfPizza():
    diameter = float(input("Enter diameter :"))
    radius2 = diameter/2
    area2 = math.pi * radius2**2
    cost = area2*1.5/100
    print("Pizza will cost £",round(cost,2))
    
    #Exercise 5 and 6 - distanceBetweenPoints
def slopeOfLine():
    x1 = eval(input("Enter x1: "))
    y1 = eval(input("Enter y1: "))
    x2 = eval(input("Enter x2: "))
    y2 = eval(input("Enter y2: "))
    slope = (y2-y1) / (x2-x1)
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("Slope is =", slope ,"Distance is =",distance)
    
def travelStatistics():
    averageSpeed = eval(input("Input average speed in km/hour: "))
    duration = eval(input("Enter duration in hours: "))
    distance2 = averageSpeed * duration
    litreUsed = 0.2*distance2
    print("Distance travelled =" , distance2 , " || Fuel used in litres =" , litreUsed)
    
def sumOfNumbers():
    numberInput = int(input("Enter number: "))
    numberAddition = range(numberInput+1)
    sumOfRange = sum(numberAddition)
    print(sumOfRange)    
    
def sumNum2():
    numInput = eval(input("Enter number : "))
    
    for i in range(1, numInput+1):
        sum = 0
        for i2 in range(1, i+1):
            sum = sum + i2
        print(str(sum))
    
def volL():
    radius4 = eval(input("enter radius"))
    volume = math.pi/3*4*radius4**3
    print(volume)
    
def averageOfNumbers():
    amountNo = eval(input("How many numbers to input: "))
    total = 0
    for i in range(amountNo):
        total = total + eval(input("Enter numbers"))
    average = total/amountNo
    print("Average number is ", average) 

def selectCoins():
    startingCoin = eval(input("Enter starting amount"))
    amountRemaining = startingCoin
    twoPound = startingCoin // 200
    amountRemaining -= twoPound * 200
    onePound = amountRemaining // 100
    amountRemaining -= onePound * 100
    pence50 = amountRemaining // 50
    amountRemaining -= pence50 * 50
    pence20 = amountRemaining // 20
    amountRemaining -= pence20 * 20
    pence10 = amountRemaining // 10
    amountRemaining -= pence10 * 10
    pence5 = amountRemaining // 5
    amountRemaining -= pence5 * 5
    pence2 = amountRemaining // 2
    amountRemaining -= pence2 * 2
    pence1 = amountRemaining // 1
    amountRemaining -= pence1 * 1
    
    print("£2 x ", twoPound,"|| £1 x ", onePound, "|| 50p x ", pence50, "|| 20p x ", pence20, "|| 10p x ", pence10, "|| 5p x ", pence5, "|| 2p x ", pence2, "|| 1p x ", pence1)
    
def selectCoins2():
    startingCoin = eval(input("Enter starting amount: "))
    
    coinType = [200,100,50,20,10,5,2,1]
    nextCoin = [0,0,0,0,0,0,0,0]   
    amountRemaining = startingCoin
    
    for i in range(8):
        nextCoin[i] = amountRemaining // coinType[i]
        amountRemaining -= nextCoin[i] * coinType[i]
        
        
    pounds = 100
    pennyList = ["2.00","1.00",50,10,5,2,1]
    print("£ :", pennyList, "Minimum coin amount :", nextCoin)
    

    
    
    