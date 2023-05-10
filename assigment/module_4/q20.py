'''Q.  Write python program that user to enter only odd numbers, else will
raise an exception.'''


try:
    num = int(input("Enter a number: "))
    assert num % 2
    print("That's an odd number...")
except:
    print("Please enter only odd number !")


