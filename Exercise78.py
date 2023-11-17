decimal = int(input("Enter a decimal number: "))
result = ""
for q in range(decimal, 0, -1):
    r = q % 2
    result = str(r) + result
    q //= 2
print("The binary representation of", decimal, "is:", result)
