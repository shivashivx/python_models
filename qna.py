# print elements from a given list present at odd index position 
"""my_list=[1,4,11,5,20,15]
print("elemenets in odd index poosition ")
print(my_list[1::2])"""


"""check a number is prime or not"""

num=int(input("Enter the number : "))
flag=True
if num>1:
    for k in range(2,int(num//2)+1):
        if num%k==0:
            flag=False
            print(num,"is not a prime number")
            break
    if flag:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")





