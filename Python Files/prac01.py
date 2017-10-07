#Liem Tony Van
#UP821148

def sayName():
    print("Tony")
    
def sayHello2():
    print("Hello")
    print("World")    

def euros2pounds():
    euros = eval(input("Input Euro amount: "))
    pounds = euros /1.15
    print("£", "{:.2f}".format(pounds))    
    
def addUP():
    
    firstNum = eval(input("Enter first number: "))
    secondNum = eval(input("Enter second number: "))
    print(firstNum + secondNum)
    
def changeCounter():
    onePence = eval(input("Enter amount of 1p's:"))
    twoPence = eval(input("Enter amount of 2p's: "))
    fivePence = eval(input("Enter amount of 5p's: "))
    
    totalOne = 1*onePence
    totalTwo = 2*twoPence
    totalFive = 5*fivePence
    print(totalOne+totalTwo+totalFive)
    
def tenHellos():
    for i in range(0, 10):
     print("Hello, World")
     
def count():
    for i in range(1, 11):
        print(i)     
        
def weightsTables():
    for i in range(0,110,10):
     pounds = i*2.2
     print(i, "{:.2f}".format(pounds))

def futureValue():
    principle = eval(input("Enter starting amount: "))
    principle = float(principle)
    rate = 5.5
    years = eval(input("Enter amount of years: "))
    totalAmount = (principle * (1 +(float(rate)/100))**years)
    Interest = (totalAmount - principle)
    print("Compound interest is :", Interest)
    print("Total Amount is :", totalAmount)
