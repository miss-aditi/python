# using and operator 
name = input("enter your name ")
mark = int(input("enter your Marks: "))

if ((mark > 40) & (mark < 60)):
  print(" you got C grade")
elif((mark > 60) & (mark < 80)):
  print("you got B grade") 
elif((mark > 80) & (mark <= 100)):
  print("you got A grade")
else:
  print("your fail")   

   
# logical or operator
num = int(input(" Enter number  of assignments you submit")) 
score = int(input("Enter your test score "))
if( num > 3 or score > 50) :
  print("your elligible for exam ")
else:
  print("your not elligible for exam")
  
  