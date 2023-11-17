number = float(input("Nhap so can tinh can bac hai: "))
def square_root(number):
    guess = number / 2
    while abs(guess * guess - number) > 1e-12:
        guess = (guess + number / guess) / 2
    return guess
result = square_root(number)
print(f"Can bac hai cua {number} la: {result}")