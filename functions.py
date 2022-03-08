import tkinter


def Calculation(Zahl, InputLine, CalcNumber):
    InputLine.config(state='normal')
    if Zahl == "C":
        InputLine.delete(0, tkinter.END)
        CalcNumber.clear()

    elif Zahl == "(":
        print("Klammer auf")
        InputLine.insert(tkinter.END, Zahl)
        CalcNumber.append(Zahl)

    elif Zahl == ")":
        print("Klammer zu")
        InputLine.insert(tkinter.END, Zahl)
        CalcNumber.append(Zahl)

    elif Zahl == "<-":

        InputLine.delete(len(InputLine.get()) - 1)
        if(CalcNumber[-1] != "+" and CalcNumber[-1] != "-" and CalcNumber[-1] != "*" and CalcNumber[-1] != "/"):
            if(len(str(CalcNumber[-1])) > 1):
                CalcNumber[-1] = str(CalcNumber[-1])[:-1]
            else:
                CalcNumber.pop()
        else:
            CalcNumber.pop()
    elif Zahl == ",":
        if(InputLine.get()[-1] != ","):
            InputLine.insert(tkinter.END, ",")
            CalcNumber[-1] = CalcNumber[-1] + str(".")

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
        elif(Zahl == "(") or (Zahl == ")"):
            try:
                if(CalcNumber[-1] != "(" and CalcNumber[-1] != ")"):
                    CalcNumber[-1] = CalcNumber[-1] + str(Zahl)
                    InputLine.insert(tkinter.END, Zahl)
                else:
                    CalcNumber.append(Zahl)
                    InputLine.insert(tkinter.END, Zahl)
            except IndexError:
                None

        else:
            if(CalcNumber):
                if(CalcNumber[-1] != "+" and CalcNumber[-1] != "-" and CalcNumber[-1] != "*" and CalcNumber[-1] != "/"):
                    CalcNumber[-1] = str(CalcNumber[-1]) + str(Zahl)
                elif(CalcNumber[-1] == "-" and len(CalcNumber) == 1):
                    CalcNumber[-1] = str(CalcNumber[-1]) + str(Zahl)
                else:
                    CalcNumber.append(str(Zahl))
            else:
                CalcNumber.append(str(Zahl))
            InputLine.insert(tkinter.END, Zahl)
    else:
        if(CalcNumber[-1] != "+" and CalcNumber[-1] != "-" and CalcNumber[-1] != "*" and CalcNumber[-1] != "/" and CalcNumber[-1] != "("):
            if(CalcNumber.count("(") != 0):
                KlammerAufExists = False

                try:
                    PostionKlammerAuf = CalcNumber.index("(")
                except:
                    KlammerAufExists = True

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
                    CalcNumber.insert(PostionMultiply - 1, str(resultCalc))

                    InputLine.delete(0, tkinter.END)
                    for i in CalcNumber:
                        InputLine.insert(tkinter.END, i)
                else:
                    resultCalc = float(
                        CalcNumber[PostionDivide - 1]) / float(CalcNumber[PostionDivide + 1])

                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.insert(PostionDivide - 1, str(resultCalc))

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
                    CalcNumber.insert(PostionMultiply - 1, str(resultCalc))

                    InputLine.delete(0, tkinter.END)
                    for i in CalcNumber:
                        InputLine.insert(tkinter.END, i)
                else:
                    resultCalc = float(
                        CalcNumber[PostionDivide - 1]) - float(CalcNumber[PostionDivide + 1])

                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.pop(PostionDivide - 1)
                    CalcNumber.insert(PostionDivide - 1, str(resultCalc))

                    InputLine.delete(0, tkinter.END)
                    for i in CalcNumber:
                        InputLine.insert(tkinter.END, i)

    print(CalcNumber)
    InputLine.config(state='readonly')
    return CalcNumber
