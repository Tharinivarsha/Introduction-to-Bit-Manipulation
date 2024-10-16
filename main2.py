def evenodd(n):
    if(n^1==n+1):
      return True
    else:
       return False
number=int(input("Enter the number: "))
if evenodd(number):
   print("Number is even.")
else:
   print("Number is odd.")