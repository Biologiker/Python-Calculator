from functions import Calculation
import tkinter

CalcNumber = []

Fenster = tkinter.Tk()

Fenster.title("Calculator")
Fenster.geometry("300x400")


InputLine = tkinter.Entry(
    text="Relative placement"
)
InputLine.place(relx=1, y=2, relwidth=1, relheight=0.09, anchor='ne')

Button1 = tkinter.Button(
    text="1",
    command=lambda: Calculation(1, InputLine, CalcNumber)
)
Button1.place(relx=0.25, rely=0.09, relwidth=0.25, relheight=0.18, anchor='nw')

Button2 = tkinter.Button(
    text="2",
    command=lambda: Calculation(2, InputLine, CalcNumber)
)
Button2.place(relx=0.5, rely=0.09, relwidth=0.25, relheight=0.18, anchor='nw')

Button3 = tkinter.Button(
    text="3",
    command=lambda: Calculation(3, InputLine, CalcNumber)
)
Button3.place(relx=0.75, rely=0.09, relwidth=0.25, relheight=0.18, anchor='nw')

Button4 = tkinter.Button(
    text="4",
    command=lambda: Calculation(4, InputLine, CalcNumber)
)
Button4.place(relx=0.25, rely=0.27, relwidth=0.25,
              relheight=0.18, anchor='nw')

Button5 = tkinter.Button(
    text="5",
    command=lambda: Calculation(5, InputLine, CalcNumber)
)
Button5.place(relx=0.5, rely=0.27, relwidth=0.25,
              relheight=0.18, anchor='nw')

Button6 = tkinter.Button(
    text="6",
    command=lambda: Calculation(6, InputLine, CalcNumber)
)
Button6.place(relx=0.75, rely=0.27, relwidth=0.25,
              relheight=0.18, anchor='nw')

Button7 = tkinter.Button(
    text="7",
    command=lambda: Calculation(7, InputLine, CalcNumber)
)
Button7.place(relx=0.25, rely=0.45, relwidth=0.25,
              relheight=0.18, anchor='nw')

Button8 = tkinter.Button(
    text="8",
    command=lambda: Calculation(8, InputLine, CalcNumber)
)
Button8.place(relx=0.5, rely=0.45, relwidth=0.25, relheight=0.18, anchor='nw')

Button9 = tkinter.Button(
    text="9",
    command=lambda: Calculation(9, InputLine, CalcNumber)
)
Button9.place(relx=0.75, rely=0.45, relwidth=0.25,
              relheight=0.18, anchor='nw')

Button0 = tkinter.Button(
    text="0",
    command=lambda: Calculation(0, InputLine, CalcNumber)
)
Button0.place(relx=0.25, rely=0.63, relwidth=0.25,
              relheight=0.18, anchor='nw')

ButtonEqual = tkinter.Button(
    text="=",
    command=lambda: Calculation("=", InputLine, CalcNumber)
)
ButtonEqual.place(relx=0.5, rely=0.63, relwidth=0.5,
                  relheight=0.18, anchor='nw')

ButtonPlus = tkinter.Button(
    text="+",
    command=lambda: Calculation("+", InputLine, CalcNumber)
)
ButtonPlus.place(relx=0, rely=0.09, relwidth=0.25,
                 relheight=0.18, anchor='nw')

ButtonMinus = tkinter.Button(
    text="-",
    command=lambda: Calculation("-", InputLine, CalcNumber)
)
ButtonMinus.place(relx=0, rely=0.27, relwidth=0.25,
                  relheight=0.18, anchor='nw')

ButtonMultiply = tkinter.Button(
    text="*",
    command=lambda: Calculation("*", InputLine, CalcNumber)
)
ButtonMultiply.place(relx=0, rely=0.45, relwidth=0.25,
                     relheight=0.18, anchor='nw')

ButtonDivide = tkinter.Button(
    text="/",
    command=lambda: Calculation("/", InputLine, CalcNumber)
)
ButtonDivide.place(relx=0, rely=0.63, relwidth=0.25,
                   relheight=0.18, anchor='nw')

ButtonClear = tkinter.Button(
    text="C",
    command=lambda: Calculation("C", InputLine, CalcNumber)
)
ButtonClear.place(relx=0, rely=0.81, relwidth=0.5,
                  relheight=0.18, anchor='nw')


Fenster.mainloop()
