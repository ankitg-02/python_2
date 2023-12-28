q=int(input("enter the quantity:"))
v=int(input("enter the value:"))
d=int(input("enter the discount:"))
t=int(input("enter the tax:"))
amount=q*v
discount_amount=amount*(d/100)
final_amount=amount-discount_amount
tax_price=(t/100)*final_amount
bill_amount=final_amount+tax_price
print("bill amount:",bill_amount)
