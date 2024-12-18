name=input("Enter your name")
age=int(input("Enter your age"))
if(age>16 and age<30):
    weight=float(input("Enter your weight"))
    if(weight>30 and weight<90):
        print(f"{name} you can join the military")
    else:
        print(f"{name} your weight is not efficient")
else:
    print(f"Sorry {name} you cannot join military")