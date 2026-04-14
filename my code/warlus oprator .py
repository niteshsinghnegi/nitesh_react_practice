numbers=[1,2,3,4]
while(n:=len(numbers))>0:
    print(numbers.pop())

    

happy=False
print(happy )
print(happy:=True)

foods = []   

while True:
    item = input("What food do you like most? (type 'quit' to stop): ")
    if item.lower() == "quit":
        break
    foods.append(item)

print("Your favorite foods are:", foods)

3