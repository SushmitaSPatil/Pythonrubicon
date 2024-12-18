name=input("Enter your name")
age=int(input("Enter your age"))
if(age>=21):
    weight=float(input("Enter your weight"))
    if(weight>40 and weight<90):
        print(f"Thank you {name}, you are eligible!")
    else:
        print(f"Sorry {name}, you're weight is not matching")
else:
    print(f"Sorry {name}, you have to wait {21-age} years")