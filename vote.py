name=input("Enter your name")
age=int(input("Enter your age"))
print(f"{name} you can vote" if age>=18 else f"{name} your age is not matching")