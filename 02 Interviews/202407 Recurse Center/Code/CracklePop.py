i = 1

while i <= 100:
    isDivisibleBy5 = i % 5 == 0
    isDivisibleBy3 = i % 3 == 0

    if isDivisibleBy5 and isDivisibleBy3:
        print("CracklePop")
    elif isDivisibleBy5:
        print("Pop")
    elif isDivisibleBy3:
        print("Crackle")
    else:
        print(i)

    i += 1
    