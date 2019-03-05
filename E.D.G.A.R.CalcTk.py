from tkinter import *
from math import *
root = Tk()
root.title("E.D.G.A.R.")
root.geometry("368x278")
Operation = 0
eq=0
def f1():
    global Output
    Output['text'] += "1"                       #кнопкa 1
def f2():
    global Output                               
    Output['text'] += '2'                        #кнопка 2
def f3():
    global Output
    Output['text'] += '3'                        #кнопка 3
def f4():
    global Output
    Output['text'] += '4'                        #кнопка 4
def f5():
    global Output
    Output['text'] += '5'                        #кнопка 5 
def f6():
    global Output
    Output['text'] += '6'                        #кнопка 6 
def f7():
    global Output
    Output['text'] += '7'                        #кнопка 7
def f8():
    global Output
    Output['text'] += '8'                        #кнопка 8
def f9():
    global Output
    Output['text'] += '9'                        #кнопка 9
def f0():
    global Output
    Output['text'] += '0'                        #кнопка 0
def addition():
    global Output, Operation, Var1
    Operation = 1
    Var1 = int(Output['text'])
    Output['text'] = ''
def subtraction():
    global Output, Operation, Var1
    Operation = 2
    Var1 = int(Output['text'])
    Output['text'] = ''
def multiplication():
    global Output, Operation, Var1
    Operation = 3
    Var1 = int(Output['text'])
    Output['text'] = ''
def division():
    global Output, Operation, Var1
    Operation = 4
    Var1 = int(Output['text'])
    Output['text'] = ''
def power():
    global Output, Operation, Var1
    Operation = 5
    Var1 = int(Output['text'])
    Output['text'] = ''
def radical():
    global Output, Operation, Var1
    Operation = 6
    Var1 = int(Output['text'])
    Output['text'] = ''
def div():
    global Output, Operation, Var1
    Operation = 7
    Var1 = int(Output['text'])
    Output['text'] = ''
def mod():
    global Output, Operation, Var1
    Operation = 8
    Var1 = int(Output['text'])
    Output['text'] = ''
def Log():
    global Output, Operation, Var1
    Operation = 9
    Var1 = int(Output['text'])
    Output['text'] = ''
def Sin():
    global Output, Operation, Var1
    Operation = 10
    Var1 = int(Output['text'])
    Output['text'] = 'sin(',Var1,')'
def Cos():
    global Output, Operation, Var1
    Operation = 10
    Var1 = int(Output['text'])
    Output['text'] = 'cos(',Var1,')'
def Tg():
    global Output, Operation, Var1
    Operation = 10
    Var1 = int(Output['text'])
    Output['text'] = 'tg(',Var1,')'
def equally():
    global Output, Var1, Var2, Operation,eq
    Var2 = Output['text']
    Output['text'] = ''
    if Operation == 1:
        eq = Var1 + int(Var2)
    elif Operation == 2:
        eq = Var1 - int(Var2)
    elif Operation == 3:
        eq = Var1 * int(Var2)
    elif Operation == 4:
        eq = Var1 / int(Var2)
    elif Operation == 5:
        eq=Var1**int(Var2)
    elif Operation == 6:
        eq=Var1**(1/int(Var2))
    elif Operation == 7:
        eq=Var1//int(Var2)
    elif Operation == 8:
        eq=Var1%int(Var2)
    elif Operation == 9:
        eq=log(Var1,int(Var2))
    elif Operation == 10:
        eq=sin(Var1)
    elif Operation == 11:
        eq=cos(Var1)
    elif Operation == 12:
        eq=tan(Var1)
    Output['text'] = eq
def clear():
    global Output
    Output['text'] = ''
Output = Label(root, font = 'Arial 20', height = 2, width = 25)
btn1 = Button(root, text = '1', font = 'Arial 18', height = 2, width = 5, command = f1)
btn2 = Button(root, text = '2', font = 'Arial 18', height = 2, width = 5, command = f2)
btn3 = Button(root, text = '3', font = 'Arial 18', height = 2, width = 5, command = f3)
btn4 = Button(root, text = '4', font = 'Arial 18', height = 2, width = 5, command = f4)
btn5 = Button(root, text = '5', font = 'Arial 18', height = 2, width = 5, command = f5)
btn6 = Button(root, text = '6', font = 'Arial 18', height = 2, width = 5, command = f6)
btn7 = Button(root, text = '7', font = 'Arial 18', height = 2, width = 5, command = f7)
btn8 = Button(root, text = '8', font = 'Arial 18', height = 2, width = 5, command = f8)
btn9 = Button(root, text = '9', font = 'Arial 18', height = 2, width = 5, command = f9)
btn0 = Button(root, text = '0', font = 'Arial 18', height = 2, width = 5, command = f0)
btnAddition = Button(root, text = '+',font = 'Arial 18', height = 2, width = 5, command = addition)
btnSubtraction = Button(root, text = '-', font = 'Arial 18', height = 2, width = 5, command = subtraction)
btnMultiplication = Button(root, text = '*', font = 'Arial 18', height = 2, width = 5, command = multiplication)
btnDivision = Button(root, text = '/', font = 'Arial 18', height = 2, width = 5, command = division)
btnEqually = Button(root, text = '=', font = 'Arial 25', height = 2, width = 5, command = equally)
btnClear = Button(root, text = 'C', font = 'Arial 18',height = 2,width = 5, command = clear)
btnPow = Button(root, text = 'k^x', font = 'Arial 18',height = 2,width = 5, command = power)
btnRadical = Button(root, text = 'n√', font = 'Arial 18',height = 2,width = 5, command = radical)
btnDiv = Button(root, text = 'div', font = 'Arial 17',height = 2,width = 5, command = div)
btnMod = Button(root, text = 'mod', font = 'Arial 17',height = 2,width = 5, command = mod)
btnLog = Button(root, text = 'log', font = 'Arial 17',height = 2,width = 5, command = Log)
btnSin = Button(root, text = 'sin', font = 'Arial 17',height = 2,width = 5, command = Sin)
btnCos = Button(root, text = 'cos', font = 'Arial 17',height = 2,width = 5, command = Cos)
btnTg = Button(root, text = 'tg', font = 'Arial 17',height = 2,width = 5, command = Tg)
btn1.place(x=5,y=174,height=50,width=50)
btn2.place(x=57,y=174,height=50,width=50)
btn3.place(x=109,y=174,height=50,width=50)
btn4.place(x=5,y=122,height=50,width=50)
btn5.place(x=57,y=122,height=50,width=50)
btn6.place(x=109,y=122,height=50,width=50)
btn7.place(x=5,y=70,height=50,width=50)
btn8.place(x=57,y=70,height=50,width=50)
btn9.place(x=109,y=70,height=50,width=50)
btn0.place(x=5,y=226,height=50,width=102)
btnAddition.place(x=161,y=70,height=50,width=50)
btnSubtraction.place(x=161,y=122,height=50,width=50)
btnMultiplication.place(x=161,y=174,height=50,width=50)
btnDivision.place(x=161,y=226,height=50,width=50)
btnClear.place(x=109,y=226,height=50,width=50)
btnPow.place(x=213,y=70,height=50,width=50)
btnEqually.place(x=265,y=174,height=102,width=102)
btnRadical.place(x=213,y=122,height=50,width=50)
btnDiv.place(x=213,y=174,height=50,width=50)
btnMod.place(x=213,y=226,height=50,width=50)
btnLog.place(x=265,y=70,height=50,width=50)
btnSin.place(x=317,y=70,height=50,width=50)
btnCos.place(x=265,y=122,height=50,width=50)
btnTg.place(x=317,y=122,height=50,width=50)
Output.pack(side='top')
root.mainloop()
