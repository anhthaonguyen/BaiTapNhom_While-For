print("Temperature Conversion Table (Celsius to Fahrenheit)")
print("Celsius      Fahrenheit")
for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(str(celsius) + "         " + str(fahrenheit))
