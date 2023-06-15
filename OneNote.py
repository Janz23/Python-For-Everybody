hrs = input("Enter Hours:")
rate = input("Enter Rate per our:")

try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print("ERROR 404: Please type number!")
    quuit()

def computepay(hrs, rate):
    lefthrs = hrs - 40
    ratea40 = rate * 1.5

    if hrs > 40:
        pay40 = 40 * rate
        payrest = lefthrs * ratea40
        pay = pay40 + payrest
    else:
        pay = hrs * rate
    return pay

print("Pay", computepay(hrs, rate))
