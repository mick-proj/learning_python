square_meters_for_landscaping = float(input('Enter the size of the field in square meters: '))
price = square_meters_for_landscaping * 7.61
discount = 0.18 * price
final_price = price - discount

print(f'The final price is: {final_price} lv.')
print(f'The discount is {discount} lv.')