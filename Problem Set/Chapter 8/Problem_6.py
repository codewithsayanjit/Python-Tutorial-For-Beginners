# Write a python function which converts inches to cms. The formula is 1 inch = 2.54 cms.

def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))

print(f"The corresponding value in cms is {inch_to_cms(n)}")