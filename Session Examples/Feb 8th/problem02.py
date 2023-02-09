# 1 --- 100 unit No charge
# 100 -- 200 5Rs
# 200 above 10Rs
# total unit 350

unit = float(input("Enter a total unit : "))

if unit > 0 and unit <= 100:
    print("No charge")
elif unit > 100 and unit <= 200:
     charge = (unit - 100)*5  
elif unit > 200:
     charge = (unit - 200) * 10 + 500
else:
    print("Unit is less than 0")

print("Total charge ", charge)


