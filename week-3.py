"""Python week3 assignment"""

def calculate_discount(price: int = None, discount_percent: int = None):
    """Calculates  the final price after applying a discount"""
    if not discount_percent:
        print("Product\'s Price is:")
        return price
    
    else:
        new_price = price * (discount_percent / 100)
        print(f"Product\'s Price after Discount is:")
        return new_price
        
print(calculate_discount(1500, 90))
    
# grade = int(input("Input your grade: "))

# if grade >= 90:
#     print("A")
# elif grade >= 80:
#     print('B')
# elif grade >= 70:
#     print("C")
# elif grade >= 60:
#     print("D")
# else:
#     print('F')
    
# tp = ["PLP Python" * x for x in range(5)]
# print(tp)


# def calculatePow(base, exp):
#     """Calculate the power of base by exponent"""
#     result = base ** exp
#     if result > 5000:
#         print(True)
#     else:
#         print(False)
#     return result

# print(calculatePow(100, 2))