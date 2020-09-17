# Here we use ininstance method to handle the errors 

# Function to add two numbers
def add(num1, num2):
    # Addition Logic
    if (isinstance(num1,(int,float)) and isinstance(num2,(int,float))):
        addition = num1 + num2
        return addition
    else:
        return 0

# Function to subtract two numbers
def subtract(num1, num2):
    # Substraction Logic
    if (isinstance(num1,(int,float)) and isinstance(num2,(int,float))):
        Substraction = num1 - num2
        return Substraction
    else:
        return 0

# Function to multiply two numbers
def multiply(num1, num2):
    # Multiplication Logic
    if (isinstance(num1,(int,float)) and isinstance(num2,(int,float))):
        multiplication = num1*num2
        return multiplication
    else:
        return 0

# Function to divide two numbers
def divide(num1, num2):
    # DivisionLogic
    if (isinstance(num1,(int,float)) and isinstance(num2,(int,float))):
        if(num2==0 and num1==0):
            return 'Not defined'
        if(num2==0):
            return 'infinity'
        division = num1/num2
        return round(division,3)
    else:
        return 0

# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function

def power(num1, num2): #num1 ^ num2
	#DivisionLogic 
    if (isinstance(num1,(int,float)) and isinstance(num2,(int,float))):
        power=1
        num2=int(num2)
        for x in range(abs(num2)):
            if(num2>=0):
                power*=num1
            else:
                power/=num1
        return round(power,3)
    else:
        return 0

# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function

def printGP(a, r, n): 
    gp=[]

    if(isinstance(a,(int,float)) and isinstance(r,(int,float)) and isinstance(n,(int,float))):
        n = int(n)
        if(n<0):
            return 0
            
        if(n>1):
            gp.append(a)

        for x in range(1,n):
            a*=r
            gp.append(a)
        return gp
    else:
        return 0


# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function

def printAP(a, d, n):
    ap=[]

    if (isinstance(a,(int,float)) and isinstance(d,(int,float)) and isinstance(n,(int,float))):
        n=int(n)
        if(n<0):
            return 0
        if(n>1):
            ap.append(a)

        for x in range(1,n):
            a+=d
            ap.append(a)
        return ap
    else:
        return 0    

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function

def printHP(a, d, n): 
	hp=[]
	return hp
