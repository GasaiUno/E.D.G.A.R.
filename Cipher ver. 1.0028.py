from tkinter import *
root=Tk()
s2=0
def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)
def Cipher():
    global s2
    s2=list(ent.get().lower())
    for i in range(0,len(s2)):
            for j in range(97,123):
               if s2[i]==' ':
                   s2[i]='_'
                   break
               if s2[i]=='z':
                   s2[i]=chr(97+fib(i+1)-1)
                   break
               if chr(j)==s2[i]:
                    s2[i]=chr(j+fib(i+1))
                    break
    ext2['text']='Ответ:',s2
def Decipher():
    global s2
    s2=list(ent.get().lower())
    for i in range(0,len(s2)):
          for j in range(97,123):
               if s2[i]==' ':
                   s2[i]='_'
                   break
               if s2[i]=='a':
                   s2[i]=chr(123-fib(i+1))
                   break
               if chr(j)==s2[i]:
                    s2[i]=chr(j-fib(i+1))
                    break                         
    ext2['text']='Ответ:',s2
ext=Label(text="Введите слово для шифрования/дешифрования")
ent=Entry()
ext2=Label(text=s2)
btn1=Button(text='Зашифровать!',command=Cipher)
btn2=Button(text='Расшифровать!',command=Decipher)
ext.pack()
ent.pack()
ext2.pack()
btn1.pack()
btn2.pack()
root.mainloop()

