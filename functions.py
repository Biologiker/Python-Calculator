import tkinter


def Calculation(Zahl, InputLine, CalcNumber):
    if Zahl == "C":
        InputLine.delete(0, tkinter.END)
        CalcNumber.clear()

    elif Zahl == "<-":
        InputLine.delete(len(InputLine.get()) - 1)
        if(CalcNumber[-1] != "+" and CalcNumber[-1] != "-" and CalcNumber[-1] != "*" and CalcNumber[-1] != "/"):
            if(len(str(CalcNumber[-1])) > 1):
                CalcNumber[-1] = float(str(CalcNumber[-1])[:-1])
            else:
                CalcNumber.pop()
        else:
            CalcNumber.pop()

    elif Zahl != "=":
        if(Zahl == "+" or Zahl == "*" or Zahl == "-" or Zahl == "/"):
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
                    InputLine.insert(tkinter.END, Zahl)
                    CalcNumber.append(Zahl)
                print("No number entered yet!")
        else:
            if(CalcNumber):
                if(CalcNumber[-1] != "+" and CalcNumber[-1] != "-" and CalcNumber[-1] != "*" and CalcNumber[-1] != "/"):
                    CalcNumber[-1] = CalcNumber[-1] + str(Zahl)
                elif(CalcNumber[-1] == "-" and len(CalcNumber) == 1):
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
                    resultCalc = float(
                        CalcNumber[PostionMultiply - 1]) * float(CalcNumber[PostionMultiply + 1])

                    CalcNumber.pop(PostionMultiply - 1)
                    CalcNumber.pop(PostionMultiply - 1)
                    CalcNumber.pop(PostionMultiply - 1)
                    CalcNumber.insert(PostionMultiply - 1, resultCalc)

                    InputLine.delete(0, tkinter.END)
                    for i in CalcNumber:
                        InputLine.insert(tkinter.END, i)
                else:
                    resultCalc = float(
                        CalcNumber[PostionDivide - 1]) / float(CalcNumber[PostionDivide + 1])

                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.insert(PostionDivide - 1, resultCalc)

                    InputLine.delete(0, tkinter.END)
                    for i in CalcNumber:
                        InputLine.insert(tkinter.END, i)

            while (CalcNumber.count("+") != 0 or CalcNumber.count("-") != 0):
                MultiplyExists = False
                DivideExists = False
                Positions = []
                try:
                    PostionMultiply = CalcNumber.index("+")
                except:
                    MultiplyExists = True

                try:
                    PostionDivide = CalcNumber.index("-")
                except:
                    DivideExists = True

                if(DivideExists == True or (MultiplyExists == False and PostionMultiply < PostionDivide)):
                    resultCalc = float(
                        CalcNumber[PostionMultiply - 1]) + float(CalcNumber[PostionMultiply + 1])

                    CalcNumber.pop(PostionMultiply - 1)
                    CalcNumber.pop(PostionMultiply - 1)
                    CalcNumber.pop(PostionMultiply - 1)
                    CalcNumber.insert(PostionMultiply - 1, resultCalc)

                    InputLine.delete(0, tkinter.END)
                    for i in CalcNumber:
                        InputLine.insert(tkinter.END, i)
                else:
                    resultCalc = float(
                        CalcNumber[PostionDivide - 1]) - float(CalcNumber[PostionDivide + 1])

                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.insert(PostionDivide - 1, resultCalc)

                    InputLine.delete(0, tkinter.END)
                    for i in CalcNumber:
                        InputLine.insert(tkinter.END, i)

    print(CalcNumber)
    return CalcNumber
