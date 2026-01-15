# Keep asking the user to enter numbers and add them. Stop when the user enters 0.
'''total=0
while True:
     num=int(input("enter the number"))
     if num==0:
        break
     total+=num
print(total)'''

# Take an integer and calculate the sum of its digits using a while loop.
# Example: 1234 → 10

num=int(input("enter a number"))
total=0
while num>0:
    