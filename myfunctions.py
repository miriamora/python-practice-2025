def hello():
    print("Hello!")

def customHello(name):
    print(f"Hello {name}")

def nameAge(name,age):
    print(f"Hello {name}, you are {age} years old.")

def addition(a,b):
    print(a+b)

def substraction(c,d):
    return c-d

hello()
customHello('Don')
nameAge('Obi',25)
addition(5,9)

test=(substraction(25,19))
print(test)
