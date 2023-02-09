quantity = float(input("Enter a quantity : "))
discount_value = 10 # 10%
unit = 100

if quantity > 1000:
    cost = quantity*unit
    discounted_value = cost * 0.1
    total_cost = cost - discounted_value
    print("Total cost is ", total_cost)
else:
    cost = quantity*unit
    print("Total cost is ", cost)
