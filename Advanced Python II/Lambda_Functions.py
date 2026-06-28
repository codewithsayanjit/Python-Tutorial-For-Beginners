'''
Functnon created usnng an expressnon usnng ‘lambda’ keyword.
Syntax:
        lambda arguments: expression
'''

# def square(n):
#     return n*n
# square(7)

square = lambda n: n*n

print(square(5))

sum = lambda a,b,c:a+b+c
print(sum(4,8,6))