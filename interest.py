def compound_interest():
    a=p*(1+r/100)**(n*t)
    ci=a-p
    print("Compound interest=KSH",format(ci,".2f"))
p=float(input("Enter the principle amount: "))
r=float(input("Enter the annual interest rate: "))
n=float(input("Enter the number of times interest is compounded in a year: "))
t=float(input("Enter the number of years: "))
compound_interest()