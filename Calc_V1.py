def main():
    cal = "Y" 
    print("Hey this is my first stand alone project so I decided to make a calculator")
    num = input("What is your first number?")
    intnum = int(num)
    while cal == "Y":
            num2 = input("What is your second number?")
            intnum2 = int(num2)
            op = input("how would you like to calculate this?(add,sub,div,mult)")
            if op.lower() == "add":
                ans = (intnum + intnum2)
            if op.lower() == "sub":
                ans = (intnum - intnum2)
            if op.lower() == "div":
                ans = (intnum / intnum2)
            if op.lower() == "mult":
                ans = (intnum * intnum2)
            intans = int(ans)
            print(intans)
            intnum = intans
            cal = input("Do you want to calculate more?(Y,N)")
            if cal == "N":
                break
main()