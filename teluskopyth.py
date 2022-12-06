lower = int(input("Enter lower range:"))
upper = int(input("enter:"))
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               print(num,"is a composite number")
       else:
           print(num,"is a prime number")