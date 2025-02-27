# number=int(input("Enter your number"))

# i.	Write a program to check if a given number is positive,  negative, or zero. 
# # if number >0:
# #     print("give number is positive")
# # elif number<0:
# #     print("given number is negetive")
# # else:
# #     print("number is zero")

# ii.	Determine if a number is odd or even.  
# # check give number is even or odd
# if number%2==0:
#     print("given number is even")
# else:
#     print("odd")


#  iii.  Check if a person is eligible to vote (age >= 18).
# age = int(input("Enter your age here"))

# print("you eligible for vote") if age>=18 else print("your not eligible for vote")


# v.	Print "Pass" if a student scores more than 40 marks;  otherwise, print "Fail." 

# marks=int(input("Enter your marks here"))
# print("Pass") if marks>40 else print("Fail")


# vi.Write a program to display the day of the week based on a  number input (1 for Monday, 2 for Tuesday, etc.). 
# number=int(input("Enter a number between 1 to 7 only : "))
# if number ==7:
#     print("sunday")
# elif number==1:
#     print("Monday")
# elif number==2:
#     print("tuesday")
# elif number==3:
#     print("wednesday")
# elif number==4:
#     print("thursday")
# elif number==5:
#     print("friday")
# elif number==6:
#     print("staturday")
# else:
#     print("invalid number")


# number = int(input("Enter your number between 1 to 12 only"))

# if number>12 and number>0:
#     print("invalid number")
# elif number==1:
#     print("january")
# elif number==2:
#     print("february")
# elif number==3:
#     print("march")
# elif number==4:
#     print("april")
# elif number==5:
#     print("may")
# elif number==6:
#     print("june")
# elif number==7:
#     print("july")
# elif number==8:
#     print("august")
# elif number==9:
#     print("september")
# elif number==10:
#     print("october")
# elif number==11:
#     print("november")
# else:
#     print("december")
    

# vii.	Implement a simple calculator to perform addition,  subtraction, multiplication, and division. 
# input= input("operation do you need to perform ")
# num1  = float(input("Enter number1:"))
# num2= float(input("Enter number2: "))
# if 






# b,medium level questions

# i.	Write a program to find the greatest of three numbers. 
# #
# num1=float(input("num1"))
# num2=float(input("num2"))
# num3=float(input("num3"))
# if num1==num2 and num2==num3:
#     print("all are equal number")
# elif (num1>num2) and (num1>num3):
#     print("num1 is greatest number")
# elif (num2>num3):
#     print("num2 is greatest number")
# else:
#     print("num3 is greatest number")

# ii.	Check if a year is a leap year. 
# year = int(input("year"))
# if (year%4 == 0 and year%100 != 0) or (year%400==0):
#     print("leap year")
# else:
#     print("not a leap year")

# iii.	Write a program to classify a character entered by the user  as a vowel, consonant, or neither. 
# value=input('enter ').lower()
# vowels='aeiou'
# if value in vowels and len(value)==1:
#     print("vowel")
# elif value.isalpha() and len(value)==1:
#     print('consonent')
# else:
#     print("neither")


# iv.	Calculate the grade of a student based on the marks they  score: 
# 1.	90-100  : Grade A 
# 2.	80-89  : Grade B 
# 3.	70-79  : Grade C 
# 4.	<70  : Fail. 


# marks=int(input("Enter your marks here"))

# if marks>=90 and marks<=100:
#     print("Grade A")
# elif marks>=80 and marks<=89:
#     print("Grade B")
# elif marks>=70 and marks<=79:
# elif marks<69 and marks>=1:
#     print("Fail")
# elif  marks<=-1 or marks>0:
#     print("please enter valid marks here")


#  Write a program to check if three sides length form a valid  triangle. 

# a= float(input("1st side length"))
# b= float(input("2nd side length"))
# c=float(input("3rd side length"))

# if a+b>c and b+c>c and a+c>b:
#     print("all side are euqal")
# else:
#     print("ivalid length's")
    
# i.	Print all numbers from 1 to 100 using a  for  loop. 
# for i in range(1,101):
#     print(i)


# num =3
# num2=5
# for i in range(1,101):
#     if i%3==0:
#         if i%5==0:
#             print(i)

#  print prime number between 1 to 100
# for num in range(2, 101): 
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):  
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)
#  gcd
# n1=int(input("enter fst number :"))
# n2=int(input("enter sec number :"))
# small=0
# lrg=0
# gcd=0
# if n1>n2:
#     lrg =n1
#     small=n2
# else:
#     lrg=n2
#     small=n1

# for i in range(1,small+1):
#     if lrg%i==0 and small%i==0:
#         gcd=i
# print(gcd)

# lcm

# num1=int(input("Enter a number :"))
# num2 = int(input(" Enter a number :"))
# high =0
# low=0
# if num1>num2:
#     high=num1
#     low=num2
# else:
#     high=num2
#     low=num1
# if high%low==0:
#     print(high,"lcm fo ",num1,num2)
# else:
#     temp=high
#     while True:
#         if temp%low==0 and temp%high==0:
#             print(temp,"is the lcm of ",num1,num2)
#             break
#         temp+=high


# next prime number is
# num = int(input("Enter a number: "))  
# next_num = num + 1  

# while True:  
#     is_prime = True  
#     for i in range(2, int(next_num ** 0.5) + 1):  
#         if next_num % i == 0:  
#             is_prime = False  
#             break  

#     if is_prime:  
#         print("Next prime number is:", next_num)  
#     next_num += 1  


