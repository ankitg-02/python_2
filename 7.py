p=int(input("enter the principal:"))
t=int(input("enter the time:"))
r=int(input("enter the rate of interest:"))
si=(p*r*t)/100
print("the simple interest:",si)
a=p*(1+(r/100))**t
ci=a-p
print("the compound interest:",ci)