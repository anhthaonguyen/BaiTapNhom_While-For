import math
points = []
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
x = float(input("Nhap phan x cua toa do: "))
y = float(input("Nhap phan y cua toa do: "))
points.append((x, y))
total_distance = 0.0
while True:
    x_input = input("Nhap phan x cua toa do (de trong de thoat): ")
    if x_input == "":
        break
    y_input = float(input("Nhap phan y cua toa do: "))
    x = float(x_input)
    y = float(y_input)
    last_x, last_y = points[-1]
    total_distance += distance(last_x, last_y, x, y)
    points.append((x, y))
first_x, first_y = points[0]
last_x, last_y = points[-1]
total_distance += distance(last_x, last_y, first_x, first_y)
print(f"Chu vi của da giac do la {total_distance}")