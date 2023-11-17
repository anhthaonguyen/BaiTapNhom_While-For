n= input("Enter 8 bits: ")
while n != "":
  if n.count("0") + n.count("1") != 8 or len(n) != 8:
    print("That wasn't 8 bits... Try again")
  else:
    m = n.count("1")
    if m % 2 == 0:
      print("The parity bit should be 0")
    else:
      print("The parity bit should be 1")
  n = input("Enter 8 bits: ")