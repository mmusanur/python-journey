product_price = int(input("Enter your product price :"))
discount_check = product_price >= 5000
final_price = product_price * 0.15*discount_check
print("Your Discount Price Is:", final_price)