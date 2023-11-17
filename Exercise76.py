num=int(input("Enter an integer(2 or greater): "))
factors=[]
if num<2:
  print("Error")
while num % 2==0:
  factors.append(2)
  num//=2
  
divisor=3
while num!=1 and divisor <= num:
  if num % divisor==0:
    factors.append(divisor)
    num//=divisor
  else: 
    divisor+=2
print("The prime factors of are:")
for i in range (len(factors)):
 print(factors[i],end="\n")

