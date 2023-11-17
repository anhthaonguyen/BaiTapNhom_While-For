total_cost = 0

while True:
    item_price_str = input("Nhap gia mat hang (de trong se ket thuc): ")
    
    if not item_price_str:
        break  
    
    try:
        item_price = float(item_price_str)
        total_cost += item_price
    except ValueError:
        print("Gia khong hop le.Vui long nhap lai")

rounded_total = round(total_cost, 2)
coins_needed = int(rounded_total * 100) % 5
adjusted_total = rounded_total - (coins_needed / 100)

print("\nTong chi phi: $" + str(rounded_total))
print("So tien phai tra: $" + str(adjusted_total))