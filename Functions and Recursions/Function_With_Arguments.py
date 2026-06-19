# A function can accept some value it can work with. We can put these values in the parentheses.

def goodDay(name, ending): # name and ending are parameters of the function. They are like placeholders for the values that we will pass to the function when we call it.
    print("Good Day, " + name)
    print(ending)
    return "ok"

a = goodDay("Harry", "Thank you") 
print(a)