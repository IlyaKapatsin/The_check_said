def check(arefmetic_expression):
    counter = 0
    number1 = 0
    number2 = 0
    scor = 0
    s = list(arefmetic_expression)
    index = int(len(arefmetic_expression))
    for y in range(index):
        if s[y] == "(":
            number1 += 1
        if s[y] == ")":
            number2 += 1
    for i in range(index):
       if (s[i] == "(") and (s[i] != ")"):
           for x in range(index):
              if s[x] == ")":
                 counter = 1
                 s[x] = "-"
       if s[i] == ")":
           scor = 1
           break

       if  counter > 0:
           counter = 0
       if counter == 1:
           scor = 1
           break
    if scor == 0:
        if number1 == number2:
            print("скобки правельные")
        else:
            print("скобки не правельные")
    else:
        print("скобки не правельные")
