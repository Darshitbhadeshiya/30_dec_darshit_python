str=input("enter a string:")

if len(str)>2:
    if str.endswith('ing'):
        str+='ly'
    else:
        str+='ing'
print("str")
