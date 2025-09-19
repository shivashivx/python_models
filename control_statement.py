# a=2
# while True:
#     if a%6==0 and a%7==0:
#         print(a)
#         break

#     a+=2

num=int(input("Enter a number:"))
a=int(input("Enter startng num:"))
b=int(input("Enter ending num:"))

i=a
print("Mult table of {num} from {a} and {b}: ")

while i<=b:
    print(f"{num} x {i} = {num*i}")
    i+=1