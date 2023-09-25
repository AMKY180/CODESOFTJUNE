a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
l = ["Addition" , "Subtraction" , "Multiplication" , "Divison"]
print("This is your choise ")
for i in l:
    print(i)
m = input("Enter you choise ")
m = m.lower()
if m == "addition":
    print("Addition of ",a ,"and ",b, "is ", a+b)
elif m == "subtraction":
    print("subtraction of ",a, "and ",b, "is ", a-b)
elif m == "multiplication":
    print("multiplication of ",a, "and ",b ,"is ", a*b)
else:
    print("divison of ",a, "and ",b ,"is ", a/b)
