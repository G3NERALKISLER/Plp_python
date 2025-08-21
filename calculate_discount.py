

def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        final_price = price - (price * discount_percent/100)
        return final_price 
    else: 
        return price    
print(calculate_discount(1000, 10))
print(calculate_discount(1000, 20))

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)
if final_price < price:
    print("Discount applied! Final price:", final_price)
else:
    print("No discount applied. Price remains:", price)