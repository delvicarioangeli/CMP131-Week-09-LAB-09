#Angelina Del Vicario
#CMP131
#Lab 09
#Week 09
#Future Value
#11/04/26

def futureVal(p, i, t):
#calcs and returns future value of the account
    f = p * ((1 + i) ** t)
    return f

def main():
    print("Future Value Calculator")

    present = float(input("Enter current account value: "))
    monthly = float(input("Enter Monthly intrest rate: "))
    months = int(input("Enter number of months: "))

    result = futureVal(present,monthly,months)
    r= round(result,2)
    print("The future value is: $", r)

main()
