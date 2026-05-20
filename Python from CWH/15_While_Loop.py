i = int(input("Enter start number: "))
n = int(input("Enter end number: "))
while(i < n+1): #If condition is true the the code run
    print(i, end=",")
    i = i+1

print("\n")

count = 5
while(count > 0):
    print(count, end=",")
    count = count - 1
else:
    print("\nI am inside else.")

#Do while loop
while True:
    number = int(input("Enter a number greater than 10: "))
    print(f"You entered {number}")

    if number>10:
        print("Successful!")
        break
    else:
        print("Try again....")
