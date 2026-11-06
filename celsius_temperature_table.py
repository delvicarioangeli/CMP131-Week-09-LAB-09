#Angelina Del Vicario
#CMP131
#Lab 09
#Week 09
#Temprature
#11/04/26
def celsius(fahrenheit): 
    return (5 / 9) * (fahrenheit - 32)

def main():
    print('fahrenheit','celsius')
    print ("the fahrenheight to celsius table")

    for f in range(21):
        c = celsius(f)

        print(f,c)

main()
