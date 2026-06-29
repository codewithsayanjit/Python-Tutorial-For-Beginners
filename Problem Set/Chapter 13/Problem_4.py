# Write a program to filter a list of numbers which are divisible by 5

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a  = [1,2,344,53,6235,643, 65,754,45,55]

f = list(filter(divisible5, a))
print(f)