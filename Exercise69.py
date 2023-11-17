approximation = 3.0
denominator = 2

for _ in range(15):
    term = 4 / (denominator * (denominator + 1) * (denominator + 2))
    approximation += term if _ % 2 == 0 else-term
    denominator += 2
    print("Approximation of π:", approximation)