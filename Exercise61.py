print("Nhap gia tri de tinh trung binh và nhap 0 de ket thuc")
count = 0
sum = 0
number = 1

while number != 0:
  number = int(input())
  sum = sum + number
  count += 1

if count == 1:
  print("Nhap gia tri")
else:
  average = sum / (count - 1)
  average = float('{:.3f}'.format(average))
  print("Trung binh: ", average)