from tkinter import *
from PIL import ImageTk, Image

class win:
    
    def __init__(self,root) :
        self.url = ImageTk.PhotoImage(Image.open(r"C:\Users\gugan\Desktop\CODSOFT PROGRAMS\calculator\albertbro.png"))
        self.l1 = Label(root, image=self.url)
        self.l1.place(x=0, y=0)

        #describing labels
        self.lbl1 = Label(root,width=11, text='First number',bg='green',fg='white',font=('times new roman',18,'bold'))
        self.lbl2 = Label(root, text='Second number',bg='green',fg='white',font=('times new roman',18,'bold'))
        self.lbl3 = Label(root,width=11, text='Result',bg='green',fg='white',font=('times new roman',18,'bold'))

        
        self.lbl1.place(x=100, y=100)
        self.lbl2.place(x=100, y=200)
        self.lbl3.place(x=100, y=300)

        
        #describing entries
        self.e1 = Entry(root,width=20,relief=SUNKEN, bd=5)
        self.e2 = Entry(root,width=20,relief=SUNKEN, bd=5)
        self.e3 = Entry(root,width=20,relief=SUNKEN, bd=5)
        
        self.e1.place(x=300, y=100)
        self.e2.place(x=300, y=200)
        self.e3.place(x=300, y=300)

        #describing buttons
        self.b1 = Button(root, text='ADD', command=self.addition, bg='yellow')
        self.b2 = Button(root, text='SUBTRACT', command=self.subtraction, bg='yellow')
        self.b3 = Button(root, text='MULTIPLY', command=self.multiply, bg='yellow')
        self.b4 = Button(root, text='DIVIDE', command=self.divide, bg='yellow')

        self.b1.place(x=100,y=250)
        self.b2.place(x=200,y=250)
        self.b3.place(x=300,y=250)
        self.b4.place(x=400,y=250)

    #arithmatic operations
    def addition(self):

        self.e3.delete(0, 'end')
        num1=int(self.e1.get())
        num2=int(self.e2.get())
        result=num1+num2
        self.e3.insert(END, str(result))

    def subtraction(self):
        self.e3.delete(0,'end')
        num1=int(self.e1.get())
        num2=int(self.e2.get())
        result=num1-num2
        self.e3.insert(END, str(result))

    def multiply(self):
        self.e3.delete(0,'end')
        num1=int(self.e1.get())
        num2=int(self.e2.get())
        result= num1*num2
        self.e3.insert(END, str(result))

    def divide(self):
        self.e3.delete(0, 'end')
        num1=int(self.e1.get())
        num2=int(self.e2.get())
        result=num1/num2
        self.e3.insert(END, str(result))



#using the tkinter module creating the root rootdow

root=Tk()
mywin= win(root)
root.title('CALCULATOR')
root.geometry('10000x10000')

root.mainloop()






        
        
