num=int(input("Enter your number"))
# for i in range(1,11):
#     print(f"{num} * {i} ={num*i}")
count=1
while count<=10:
    result=count*num
    print(f"{num} * {count} = {result}")
    count +=1
