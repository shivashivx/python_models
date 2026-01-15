# student=["shiva","kerish","ajith","reneesh"]
# for k in student:
#     print(k,end=" ")

num = int(input("Enter a number: "))
print(f"\nMultiplication Table of {num}:\n")

for i in range(1, 11):  
    print(f"{num} x {i} = {num * i}")