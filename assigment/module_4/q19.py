'''Q.  How Do You Handle Exceptions With Try/Except/Finally In Python?
Explain with coding snippets.'''

try:
    a=int(input("Enter a :"))
    b=int(input("Enter b :"))
    print("Sum of a & b :",a+b)
except Exception as e:
    print(e)
finally:
    print("This is finally block....")

