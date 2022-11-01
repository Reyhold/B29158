while True:

    a = int(input("Введите число №1: "))
    b = int(input("Введите число №2: "))
    cas = input("Введите действие "
                " 1 - сумма"
                " 2 - разность"
                " 3 - умножение"
                " 4 - деление"
                " 5 - поменять"
                " 6 - вийти: ")
    if cas == "1":
        result = a + b
        print(result)
    if cas == "2":
        result = a - b
        print(result)
    if cas == "3":
        result = a * b
        print(result)
    if cas == "4":
        result = a / b
        print(result)
    if cas == "5":
        a = int(input("Введите число №1: "))
        b = int(input("Введите число №2: "))
        cas = input("Введите действие "
                    " 1 - сумма"
                    " 2 - разность"
                    " 3 - умножение"
                    " 4 - деление"
                    " 5 - вийти: ")
        if cas == "1":
            result = a + b
            print(result)
        if cas == "2":
            result = a - b
            print(result)
        if cas == "3":
            result = a * b
            print(result)
        if cas == "4":
            result = a / b
            print(result)
        if cas == "5":
            break
    if cas == "6":
        break
    print("Пока")
