# Default arguments are the arguments that we can provide a default value for. If we do not provide a value for that argument when we call the function, it will use the default value.

def goodDay(name, ending="Thank you"): # name is a required parameter, ending is an optional parameter with a default value of "Thank you"
    print(f"Good Day, {name}")
    print(ending)

goodDay("Sayanjit", "Thanks")
goodDay("Rohan")