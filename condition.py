# age=int(input("enter your age:"))
# if age>=18:
#     print("eligibile to vote")
# else:
#     print("not eligible for vote") 
    

# Example: Nested if in Python

#  age = 2
#  country = "India"

# if age >= 18:
#     print("You are an adult.")
    
#     if country == "India":
#         print("You are eligible to vote in India.")
#     else:
#         print("You are an adult, but not from India.")
# else:
#     print("You are not an adult yet.")

a=int(input("enter the number:"))
b=int(input("enter the number:"))
print("1add/n2sub/n3multioly")
choice=int(input("enter a choice"))
if choice==1:
   print(a+b)
elif choice==2:
   print(a-b) 
elif choice==3:
    print(a*b)
else:
   print("invalied")
