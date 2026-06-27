while True:
    try:
        inp1 = int(input("a="))
        fac = 1
        while inp1 > 1:
            fac = fac * inp1
            inp1 = inp1 - 1
        print(fac)
    except:
        print("invalid input")
