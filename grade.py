name=input("Enter your name")
per=float(input("Enter your percentage"))
if(per>=90):
    print(f"Congrats {name} you have got A grade")
elif(per>=75 and per<90):
    print(f"Congrats {name} you have got B grade")
elif(per>=50 and per<75):
    print(f"Congrats {name} you have got C grade")
else:
    print(f"Sorry {name} you fail in exam")