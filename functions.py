import tkinter


def Calculation(Zahl, InputLine, CalcNumber):
    if Zahl == "C":
        InputLine.delete(0, tkinter.END)
        CalcNumber.clear()

    elif Zahl != "=":
        if(Zahl == "+" or Zahl == "*" or Zahl == "/"):
            try:
                if(CalcNumber[-1] != "+" and CalcNumber[-1] != "-" and CalcNumber[-1] != "*" and CalcNumber[-1] != "/"):
                    CalcNumber.append(Zahl)
                    InputLine.insert(tkinter.END, Zahl)
                else:
                    CalcNumber[-1] = Zahl
                    print(InputLine.delete(0, tkinter.END))
                    for i in CalcNumber:
                        InputLine.insert(tkinter.END, i)
            except IndexError:
                if(Zahl == "-"):
                    FirstNumberNegative = True
                    InputLine.insert(tkinter.END, Zahl)
                    CalcNumber.append(Zahl)
                print("No number entered yet!")
                # Außer es wurde Minus gedrückt wegen Vorzeichen
        else:
            if(CalcNumber):
                if(CalcNumber[-1] != "+" and CalcNumber[-1] != "-" and CalcNumber[-1] != "*" and CalcNumber[-1] != "/"):
                    CalcNumber[-1] = CalcNumber[-1] + str(Zahl)
                else:
                    CalcNumber.append(str(Zahl))
            else:
                CalcNumber.append(str(Zahl))
            InputLine.insert(tkinter.END, Zahl)
    else:
        if len(CalcNumber) == 0:
            print("Please enter at least two Numbers and an Operator!")
        elif len(CalcNumber) == 1:
            print("Please enter at least a second Numbers and an Operator!")
        elif len(CalcNumber) % 2 == 0:
            print("Please enter a final number!")
        else:
            while (CalcNumber.count("*") != 0 or CalcNumber.count("/") != 0):
                MultiplyExists = False
                DivideExists = False
                Positions = []
                try:
                    PostionMultiply = CalcNumber.index("*")
                except:
                    MultiplyExists = True

                try:
                    PostionDivide = CalcNumber.index("/")
                except:
                    DivideExists = True

                if(DivideExists == True or (MultiplyExists == False and PostionMultiply < PostionDivide)):
                    resultCalc = int(
                        CalcNumber[PostionMultiply - 1]) * int(CalcNumber[PostionMultiply + 1])

                    print("resultCalc:", resultCalc)
                    print(PostionMultiply)

                    CalcNumber.pop(PostionMultiply - 1)
                    CalcNumber.pop(PostionMultiply - 1)
                    CalcNumber.pop(PostionMultiply - 1)
                    CalcNumber.insert(PostionMultiply - 1, resultCalc)

                    print(CalcNumber)
                    InputLine.delete(0, tkinter.END)
                    for i in CalcNumber:
                        InputLine.insert(tkinter.END, i)
                else:
                    resultCalc = int(
                        CalcNumber[PostionDivide - 1]) / int(CalcNumber[PostionDivide + 1])

                    print("resultCalc:", resultCalc)
                    print(PostionDivide)

                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.insert(PostionDivide - 1, resultCalc)

                    print(CalcNumber)
                    InputLine.delete(0, tkinter.END)
                    for i in CalcNumber:
                        InputLine.insert(tkinter.END, i)

    print(CalcNumber)
    return CalcNumber
