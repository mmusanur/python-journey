orginal_price = int(input("Enter Your Price: "))
possible_discount = orginal_price>=1000
discount_price = orginal_price * 0.10 * possible_discount
final_price = orginal_price - discount_price
print("\n========Your Shopping Bill==========")
print("Orginal Price:", orginal_price)
print("Discount Price:", discount_price)
print("Final Price:", final_price)