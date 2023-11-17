n = int(input("n="))
m = int(input("m="))

d = min(n, m)

while d > 1:
    
    for i in range(2, d + 1):
        if n % i == 0 and m % i == 0:
            d = i
            break
    else:
        d -= 1

print("Uoc chung lon nhat", n, "và", m, "la:", d)