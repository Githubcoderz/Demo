print("hello world")
input("your name")
input("age")

#length of sring
str1 ="wipro"
len1 =len(str1)
print(len1)

str2 ="training" 
len2 =len(str2)
print(len2)

final_str = str1+str2
print(final_str)
print(len(final_str))

 #if elif statement
age=21
if(age>=18):
 print("can vote & apply for license")
elif(age<18):
 print("underage")

 #if elif else statement
 light= "yellow"
 if(light == "red"):
  print("stop")
 elif( light == "green"):
  print("go")
 elif( light ==" yellow"):
  print(" wait")
 else:
  print ("light is broken")

#for num is smaller or greater
num=5
if(num > 2):
 print("greater than 2")
 if(num > 3):
  print("greater than 3")

  #odd or even

  num = int(input("enter number"))
  if(num % 2 == 0):
   print("EVEN")
  else:
   print("ODD")

 #gretest of 3 num 
 a = int(input("enter first number"))
 b = int(input("enter second number" ))
 c = int(input("enter third number"))
 if (a >=b and a>=c ):
  print("first number is greatest", a) 
 elif( b>= c):
  print("second number is greatest", b)
 else :
  print("third is largest", c)

  #multiple of num
  x = int(input("enter number: "))
  if(x % 7 ==0):
   print("multiple of 7")
  else:
   print("not a multiple")

#primenumber
num= int(input("Enter A number"))
if num > 1:
 for i in range(2, num):
  if num % i ==0:
   print (num, "Is NOT a prime number")
   break
  else:
   print(num, "IS a prime number")
 else:
  print(num, "Is not a prime number")

#LEAP YEAR
years = [1990, 2100, 2000, 2200, 1992]

for year in years:
    is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    print(f"{year} is leap year: {is_leap}")

#COUNT OF NUMBER
str_val = "36242525526636637"
count_3 = str_val.count('3')
print(f"Count of 3: {count_3}")