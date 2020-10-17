from tkinter import *
from turtle import *
from tkmacosx import Button
from abc import ABC
import statistics
def inputtolist(str1,list1):
        str1+=" ,"
        str2=""
        j=0
        i=0
        k=0
        for i in range (len(str1)):
            if str1[i]!=",": str2+=str1[i]
            else:
                list1.append(eval(str2))
                str2=""
        return list1
    
class LCM(object):
        def __init__(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Least Common Multiple")
                self.window.configure(background='black')
                self.inputenv=StringVar()
                inputleb = Label(self.window,text="Enter the numbers",font=("Times", "17")).place(height = 35, width=350,x=75, y=0)
                inputen = Entry(self.window,textvariable=self.inputenv).place(height = 35, width=350,x=75, y=40)
                buttonenter = Button(self.window,text="Enter",command=self.showans).place(x=212, y=80)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=212, y=105)
        def lcmoperation(self,list1):
                num=1
                while(1):
                    check=0
                    for i in range (len(list1)):
                        if num%list1[i]!=0: check+=1
                    if check!=0:
                        num+=1
                    else: return num
        def showans(self):
                self.str1=""
                self.list1=[]
                self.str1= str(self.inputenv.get())
                inputtolist(self.str1,self.list1)
                self.num=self.lcmoperation(self.list1)
                Label(self.window,text="The LCM is %d"%self.num,font=("Times", "17")).place(height = 35, width=350,x=75, y=145)
        def back(self):
                self.window.destroy()
                main()
                return
class GCD(object):
        def __init__(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Greatest Common Divisor")
                self.window.configure(background='black')
                self.inputenv=StringVar()
                inputleb = Label(self.window,text="Enter the numbers",font=("Times", "17")).place(height = 35, width=350,x=75, y=0)
                inputen = Entry(self.window,textvariable=self.inputenv).place(height = 35, width=350,x=75, y=40)
                buttonenter = Button(self.window,text="Enter",command=self.showans).place(x=212, y=80)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=212, y=105)
        def gcdoperation(self,list1):
                num=max(list1)
                while(num>0):
                    check=0
                    for i in range (len(list1)):
                        if list1[i]%num!=0: check+=1
                    if check!=0:
                        num-=1
                    else: return num
        def showans(self):
                self.str1=""
                self.list1=[]
                self.str1= str(self.inputenv.get())
                inputtolist(self.str1,self.list1)
                self.num=self.gcdoperation(self.list1)
                Label(self.window,text="The GCD is %d"%self.num,font=("Times", "17")).place(height = 35, width=350,x=75, y=145)
        def back(self):
                self.window.destroy()
                main()
                return

class Baseconversion(object):
        def __init__(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Base Conversion")
                self.window.configure(background='black')
                self.inputenv = IntVar()
                self.v = IntVar()
                inputleb = Label(self.window,text="Enter the number",font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=0)
                inputen = Entry(self.window,textvariable=self.inputenv).place(height = 35, width=350,x=75, y=40)
                bina = Radiobutton(self.window, text="Binary",padx = 20, variable=self.v,value=2).place(height = 25, width=150,x=250, y=80)
                octal = Radiobutton(self.window, text="Octal",padx = 20, variable=self.v,value=6).place(height = 25, width=150,x=250, y=110)
                hexa = Radiobutton(self.window, text="Hexadecimal",padx = 20, variable=self.v,value=16).place(height = 25, width=150,x=250, y=140)
                buttonenter = Button(self.window,text="Enter",command=self.getnum).place(height = 25, width=150,x=75, y=95)
                buttonexit = Button(self.window,text="Back",command=self.back).place(height = 25, width=150,x=75, y=125)
        def getnum(self):
                dec= int(self.inputenv.get())
                base = int(self.v.get())
                mod=0
                string = ""
                while dec:
                        mod = dec % base
                        dec = dec// base
                        string= chr(48 + mod + 7*(mod > 10)) + string
                ansleb = Label(self.window,text="%d in base %d is "%(self.inputenv.get(),base)+string,font=("Times", "17")).place(height = 35, width=350,x=75, y=175)
        def back(self):
                self.window.destroy()
                main()
                return
        
class Calculatormenu(ABC):
    def backtomenu(self):
        pass
class calculator(Calculatormenu):
        def showcal(self):
            self.calculator = Tk()
            self.dis=""
            self.equation = self.dis
            self.calculator.geometry("525x275+500+475")
            self.calculator.title("Calculator")
            self.calculator.configure(background='black')
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
            clear= Button(self.calculator,text = "CLEAR",width=235,height=35,activebackground="Gray",background="lightsalmon",fg="black",font=("Times", "16"),command=self.clear).place(x=25, y=45)
            neg =Button(self.calculator,text = "+/-",width=115,height=35,activebackground="Gray",background="lightsalmon",foreground="black",font=("Times", "16"),command=self.pressneg).place(x=265, y=45)
            divide =Button(self.calculator,text = "÷",width=115,height=35,activebackground="Gray",background="orange",foreground="black",font=("Times", "16"),command=self.pressdiv).place(x=385, y=45)
            one = Button(self.calculator,text = "1",width=115,height=35,activebackground="Gray",background="turquoise1",foreground="black",font=("Times", "16"),command=self.press1).place(x=25, y=85)
            two = Button(self.calculator,text = "2",width=115,height=35,activebackground="Gray",background="turquoise1",foreground="black",font=("Times", "16"),command=self.press2).place(x=145, y=85)
            three = Button(self.calculator,text = "3",width=115,height=35,activebackground="Gray",background="turquoise1",foreground="black",font=("Times", "16"),command=self.press3).place(x=265, y=85)
            mul = Button(self.calculator,text = "x",width=115,height=35,activebackground="Gray",background="darkorange",foreground="black",font=("Times", "16"),command=self.pressmul).place(x=385, y=85)
            four = Button(self.calculator,text = "4",width=115,height=35,activebackground="Gray",background="turquoise2",foreground="black",font=("Times", "16"),command=self.press4).place(x=25, y=125)
            five = Button(self.calculator,text = "5",width=115,height=35,activebackground="Gray",background="turquoise2",foreground="black",font=("Times", "16"),command=self.press5).place(x=145, y=125)
            six = Button(self.calculator,text = "6",width=115,height=35,activebackground="Gray",background="turquoise2",foreground="black",font=("Times", "16"),command=self.press6).place(x=265, y=125)
            minus = Button(self.calculator,text = "-",width=115,height=35,activebackground="Gray",background="coral",foreground="black",font=("Times", "16"),command=self.pressmin).place(x=385, y=125)
            seven = Button(self.calculator,text = "7",width=115,height=35,activebackground="Gray",background="turquoise3",foreground="black",font=("Times", "16"),command=self.press7).place(x=25, y=165)
            eight = Button(self.calculator,text = "8",width=115,height=35,activebackground="Gray",background="turquoise3",foreground="black",font=("Times", "16"),command=self.press8).place(x=145, y=165)
            nine = Button(self.calculator,text = "9",width=115,height=35,activebackground="Gray",background="turquoise3",foreground="black",font=("Times", "16"),command=self.press9).place(x=265, y=165)
            plus=Button(self.calculator,text = "+",width=115,height=35,activebackground="Gray",background="tomato",foreground="black",font=("Times", "16"),command=self.pressplus).place(x=385, y=165)
            zero= Button(self.calculator,text = "0",width=235,height=35,activebackground="Gray",background="salmon",foreground="black",font=("Times", "16"),command=self.press0).place(x=25, y=205)
            dec= Button(self.calculator,text = ".",width=115,height=35,activebackground="Gray",background="salmon",foreground="black",font=("Times", "16"),command=self.pressdec).place(x=265, y=205)
            equal =Button(self.calculator,text = "=",width=115,height=35,activebackground="Gray",background="orangered",foreground="black",font=("Times", "16"),command=self.equalpress).place(x=385, y=205)
            self.calculator.mainloop()
        def pressneg(self): 
            self.dis = self.dis + "-" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def press1(self): 
            self.dis = self.dis + "1" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def press2(self): 
            self.dis = self.dis + "2" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def press3(self): 
            self.dis = self.dis + "3" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def press4(self): 
            self.dis = self.dis + "4" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def press5(self): 
            self.dis = self.dis + "5" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def press6(self): 
            self.dis = self.dis + "6" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def press7(self): 
            self.dis = self.dis + "7" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def press8(self): 
            self.dis = self.dis + "8" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def press9(self): 
            self.dis = self.dis + "9" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def press0(self): 
            self.dis = self.dis + "0" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def pressdiv(self): 
            self.dis = self.dis + "/" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def pressmul(self): 
            self.dis = self.dis + "*" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def pressplus(self): 
            self.dis = self.dis + "+" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def pressmin(self): 
            self.dis = self.dis + "-" 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def pressdec(self): 
            self.dis = self.dis + "." 
            self.equation = self.dis
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)
        def equalpress(self): 
            try:  
                total = str(eval(self.dis)) 
                self.equation = total
                self.dis = ""
                self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
                self.display.place(height =25, width=475,x=25, y=10)
            except: 
                self.equation=" error "
                self.dis = ""
                self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
                self.display.place(height =25, width=475,x=25, y=10)
        def clear(self): 
            self.dis = "" 
            self.equation=""
            self.display = Label(self.calculator,text=self.equation,font=("Times", "17"),justify=LEFT)
            self.display.place(height =25, width=475,x=25, y=10)

class equationsolver(object):
        def __init__(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Equation Solver")
                self.window.configure(background='black')
                Label(self.window,text="This program can only solve 3 format of equation",font=("Times", "17")).place(height = 35, width=360,x=75, y=0)
                Label(self.window,text="1. ax + b = c",font=("Times", "17"),justify=LEFT).place(height = 35, width=300,x=75, y=40)
                Button(self.window,text="Choose",command=self.choose1).place(height = 35, width=60,x=375, y=40)
                Label(self.window,text="2. ax + by + c = 0 and dx + ey + f = 0",font=("Times", "17"),justify=LEFT).place(height = 35, width=300,x=75, y=80)
                Button(self.window,text="Choose",command=self.choose2).place(height = 35, width=60,x=375, y=80)
                Label(self.window,text="3. ax^2 + bx + c  = 0",font=("Times", "17"),justify=LEFT).place(height = 35, width=300,x=75, y=120)
                Button(self.window,text="Choose",command=self.choose3).place(height = 35, width=60,x=375, y=120)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def back(self):
                self.window.destroy()
                main()
                return
        def choose1(self):
                self.window.destroy()
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Equation Solver")
                self.window.configure(background='black')
                self.a = IntVar()
                self.b = IntVar()
                self.c = IntVar()
                Entry(self.window,textvariable=self.a).place(height = 35, width=50,x=122, y=20)
                Label(self.window,text="x + ",font=("Times", "17"),justify=LEFT).place(height = 35, width=50,x=172, y=20)
                Entry(self.window,textvariable=self.b).place(height = 35, width=50,x=222, y=20)
                Label(self.window,text=" = ",font=("Times", "17"),justify=LEFT).place(height = 35, width=50,x=272, y=20)
                Entry(self.window,textvariable=self.c).place(height = 35, width=50,x=322, y=20)
                buttonenter = Button(self.window,text="Enter",command=self.getans1).place(height = 25, width=50,x=222, y=60)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0, y=200)
        def getans1(self):
                ans = (self.c.get()-self.b.get())/self.a.get()
                leb = Label(self.window,text="x = %.2f"%ans,font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=90)
        def choose2(self):
                self.window.destroy()
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Equation Solver")
                self.window.configure(background='black')
                self.a = IntVar()
                self.b = IntVar()
                self.c = IntVar()
                self.d = IntVar()
                self.e = IntVar()
                self.f = IntVar()
                Entry(self.window,textvariable=self.a).place(height = 35, width=50,x=112, y=20)
                Label(self.window,text="x + ",font=("Times", "17"),justify=LEFT).place(height = 35, width=50,x=132, y=20)
                Entry(self.window,textvariable=self.b).place(height = 35, width=50,x=182, y=20)
                Label(self.window,text="y + ",font=("Times", "17"),justify=LEFT).place(height = 35, width=50,x=232, y=20)
                Entry(self.window,textvariable=self.c).place(height = 35, width=50,x=282, y=20)
                Label(self.window,text=" =  0",font=("Times", "17"),justify=LEFT).place(height = 35, width=50,x=332, y=20)
                Label(self.window,text=" AND ",font=("Times", "17"),justify=LEFT).place(height = 25, width=50,x=222, y=60)
                Entry(self.window,textvariable=self.d).place(height = 35, width=50,x=112, y=90)
                Label(self.window,text="x + ",font=("Times", "17"),justify=LEFT).place(height = 35, width=50,x=132, y=90)
                Entry(self.window,textvariable=self.e).place(height = 35, width=50,x=182, y=90)
                Label(self.window,text="y + ",font=("Times", "17"),justify=LEFT).place(height = 35, width=50,x=232, y=90)
                Entry(self.window,textvariable=self.f).place(height = 35, width=50,x=282, y=90)
                Label(self.window,text=" =  0",font=("Times", "17"),justify=LEFT).place(height = 35, width=50,x=332, y=90)
                buttonenter = Button(self.window,text="Enter",command=self.getans2).place(height = 25, width=50,x=222, y=130)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0, y=200)
        def isSolvable(self):
                if (self.a.get()*self.d.get()) - (self.d.get()*self.c.get()) != 0:
                    return True
                return False
        def getans2(self):
                if self.isSolvable() == True:
                        ans1 = (self.f.get()*self.b.get()-self.c.get()*self.e.get())/(self.a.get()*self.e.get()-self.d.get()*self.b.get());
                        ans2 = (self.c.get()*self.d.get() -self.f.get()*self.a.get())/(self.a.get()*self.e.get()-self.d.get()*self.b.get());
                        leb = Label(self.window,text="x = %.2f and y = %.2f"%(ans1,ans2),font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=160)
                else :
                        leb = Label(self.window,text="Unsolvable",font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=90)
        def choose3(self):
                self.window.destroy()
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Equation Solver")
                self.window.configure(background='black')
                self.a = IntVar()
                self.b = IntVar()
                self.c = IntVar()
                Entry(self.window,textvariable=self.a).place(height = 35, width=50,x=112, y=20)
                Label(self.window,text="x^2 + ",font=("Times", "17"),justify=LEFT).place(height = 35, width=50,x=132, y=20)
                Entry(self.window,textvariable=self.b).place(height = 35, width=50,x=182, y=20)
                Label(self.window,text="x + ",font=("Times", "17"),justify=LEFT).place(height = 35, width=50,x=232, y=20)
                Entry(self.window,textvariable=self.c).place(height = 35, width=50,x=282, y=20)
                Label(self.window,text=" =  0",font=("Times", "17"),justify=LEFT).place(height = 35, width=50,x=332, y=20)
                buttonenter = Button(self.window,text="Enter",command=self.getans3).place(height = 25, width=50,x=222, y=60)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0, y=200)
        def getans3(self):
                ans1 = (-self.b.get() + pow(pow(self.b.get(),2) - 4*self.a.get()*self.c.get(),0.5))/2*self.a.get();
                ans2 = (-self.b.get() - pow(pow(self.b.get(),2) - 4*self.a.get()*self.c.get(),0.5))/2*self.a.get();
                leb = Label(self.window,text="x = %.2f and %.2f"%(ans1,ans2),font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=90)
class Poly(object):
    def __init__(self,x):
        self.__x = x
    def print(self):
        x = self.__x
        y = ""
        for i in range (len(x)):
            if i==0 and x[i]!=0:
                y += ("%d"%x[i])
            elif i==1:
                if x[i]<0:
                    y += " - "+"%d"%abs(x[i])+"x"
                elif x[i]==0:
                    continue
                elif x[i]==1:
                    y += " + "+"x^%d"%i
                else :
                    y += " + "+"%d"%int(x[i])+"x"
            else:
                if x[i]<0:
                    y += " - "+"%d"%abs(x[i])+"x^%d"%i
                elif x[i]==0:
                    continue
                elif x[i]==1:
                    y += " + "+"x^%d"%i
                else :
                    y += " + "+"%d"%int(x[i])+"x^%d"%i
        return y
    def add(self,p):
        x = self.__x
        y = p.__x
        more = max(len(x),len(y))
        less = min(len(x),len(y))
        new = []
        for i in range (more):
            if i >= less:
                if len(x)>len(y):
                    new.append(x[i])
                elif len(y)>len(x):
                    new.append(y[i])
            else :
                new.append(x[i]+y[i])
        return Poly(tuple(new))
    def multiply(self,p):
        x = self.__x
        y = p.__x
        new = []
        for i in range (len(x)):
            for j in range (len(y)):
                new.append(0)
                new[i+j]+=x[i]*y[j]
        return Poly(tuple(new))
    def power(self,n):
        x = self.__x
        p = Poly(x)
        if n<0:
            return "Invalid"
        if n==0:
            return Poly((1))
        for i in range (n-1):
            p = p.multiply(self)
        return p
    def diff(self):
        x = self.__x
        new=[]
        for i in range (1,len(x)):
            new.append(x[i]*i)
        return Poly(tuple(new))
    def integrate(self):
        x = self.__x
        new=[0]
        for i in range (len(x)):
            new.append(x[i]/(i+1))
        return Poly(tuple(new))
    def eval(self,n):
        x = self.__x
        y = 0
        for i in range (len(x)):
            y += x[i]*pow(n,i)
        return y

class equationsoperation(object):
        def __init__(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Equations Operation")
                self.window.configure(background='black')
                Label(self.window,text="Equations Operation",font=("Times", "17")).place(height = 35, width=360,x=75, y=0)
                Label(self.window,text="Addition",font=("Times", "17"),justify=LEFT).place(height = 35, width=300,x=75, y=40)
                Button(self.window,text="Choose",command=self.choose1).place(height = 35, width=60,x=375, y=40)
                Label(self.window,text="Multiply",font=("Times", "17"),justify=LEFT).place(height = 35, width=300,x=75, y=80)
                Button(self.window,text="Choose",command=self.choose2).place(height = 35, width=60,x=375, y=80)
                Label(self.window,text="Power",font=("Times", "17"),justify=LEFT).place(height = 35, width=300,x=75, y=120)
                Button(self.window,text="Choose",command=self.choose3).place(height = 35, width=60,x=375, y=120)
                Label(self.window,text="Value",font=("Times", "17"),justify=LEFT).place(height = 35, width=300,x=75, y=160)
                Button(self.window,text="Choose",command=self.choose4).place(height = 35, width=60,x=375, y=160)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def choose1(self):
                self.window.destroy()
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Equations Operation")
                self.window.configure(background='black')
                self.a = StringVar()
                self.b = StringVar()
                Label(self.window,text="Enter equation #1",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=20)
                Entry(self.window,textvariable=self.a).place(height = 25, width=150,x=275, y=20)
                Label(self.window,text="Enter equation #2",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=50)
                Entry(self.window,textvariable=self.b).place(height = 25, width=150,x=275, y=50)
                buttonenter = Button(self.window,text="Enter",command=self.getans1).place(height = 25, width=50,x=222, y=80)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def back(self):
                self.window.destroy()
                main()
                return
        def getans1(self):
                list1 =[]
                list2=[]
                inputtolist(self.a.get(),list1)
                inputtolist(self.b.get(),list2)
                a = Poly(list1)
                b = Poly(list2)
                ans  = a.add(b)
                leb = Label(self.window,text=ans.print(),font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=110)
        def choose2(self):
                self.window.destroy()
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Equations Operation")
                self.window.configure(background='black')
                self.a = StringVar()
                self.b = StringVar()
                Label(self.window,text="Enter equation #1",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=20)
                Entry(self.window,textvariable=self.a).place(height = 25, width=150,x=275, y=20)
                Label(self.window,text="Enter equation #2",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=50)
                Entry(self.window,textvariable=self.b).place(height = 25, width=150,x=275, y=50)
                buttonenter = Button(self.window,text="Enter",command=self.getans2).place(height = 25, width=50,x=222, y=80)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def getans2(self):
                list1 =[]
                list2=[]
                inputtolist(self.a.get(),list1)
                inputtolist(self.b.get(),list2)
                a = Poly(list1)
                b = Poly(list2)
                ans  = a.multiply(b)
                leb = Label(self.window,text=ans.print(),font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=110)
        def choose3(self):
                self.window.destroy()
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Equations Operation")
                self.window.configure(background='black')
                self.a = StringVar()
                self.b = StringVar()
                Label(self.window,text="Enter equation #1",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=20)
                Entry(self.window,textvariable=self.a).place(height = 25, width=150,x=275, y=20)
                Label(self.window,text="Enter equation #2",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=50)
                Entry(self.window,textvariable=self.b).place(height = 25, width=150,x=275, y=50)
                buttonenter = Button(self.window,text="Enter",command=self.getans3).place(height = 25, width=50,x=222, y=80)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def getans3(self):
                list1 =[]
                inputtolist(self.a.get(),list1)
                a = Poly(list1)
                ans  = a.power(self.b.get())
                leb = Label(self.window,text=ans.print(),font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=110)
        def choose4(self):
                self.window.destroy()
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Equations Operation")
                self.window.configure(background='black')
                self.a = StringVar()
                self.b = StringVar()
                Label(self.window,text="Enter equation #1",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=20)
                Entry(self.window,textvariable=self.a).place(height = 25, width=150,x=275, y=20)
                Label(self.window,text="Enter equation #2",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=50)
                Entry(self.window,textvariable=self.b).place(height = 25, width=150,x=275, y=50)
                buttonenter = Button(self.window,text="Enter",command=self.getans4).place(height = 25, width=50,x=222, y=80)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def getans4(self):
                list1 =[]
                inputtolist(self.a.get(),list1)
                a = Poly(list1)
                ans  = a.eval(self.b.get())
                leb = Label(self.window,text="%d"%ans,font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=110)
        
class numoperation(Calculatormenu):
    def shownumop(self):
        self.window=Tk()
        self.window.geometry("500x225+500+200")
        self.window.title("Number Operation")
        self.window.configure(background='black')
        menu = Frame(self.window,bg='black',width=500,height=275)
        menu.place(x=0,y=0)
        title = Label(menu,text = "Number Operation",bg="yellowgreen",font=("Times", "24") ).place(height =30, width=450,x=25, y=10)
        LCM = Button(menu,text = "Least Common Multiple",width=17,command=self.showlcm,activebackground="Gray",background="khaki",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=50)
        GCD = Button(menu,text = "Greatest Common Divisor",width=17,command=self.showgcd,activebackground="Gray",background="palegoldenrod",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=90)
        base = Button(menu,text = "Base Conversion",width=17,command=self.showbase,activebackground="Gray",background="lightgoldenrodyellow",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=130)
        back = Button(menu,text = "Back To Menu",width=17,command=self.backtomenu,activebackground="Gray",background="lightyellow",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=170)
        self.window.mainloop()
    def backtomenu(self):
        self.window.destroy()
        main().menuwindow
        return
    def showlcm(self):
        self.window.destroy()
        LCM()
        return
    def showgcd(self):
        self.window.destroy()
        GCD()
        return
    def showbase(self):
        self.window.destroy()
        Baseconversion()
        return
class algebra(Calculatormenu):
        def showalgebra(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Algebra")
                self.window.configure(background='black')
                menu = Frame(self.window,bg='black',width=500,height=275)
                menu.place(x=0,y=0)
                title = Label(menu,text = "Algebra",bg="yellowgreen",font=("Times", "24") ).place(height =30, width=450,x=25, y=10)
                es = Button(menu,text = "Equation Solver",width=17,command=self.showes,activebackground="Gray",background="palegoldenrod",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=50)
                value = Button(menu,text = "Equations Operation",width=17,command=self.showeo,activebackground="Gray",background="lightgoldenrodyellow",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=90)
                back = Button(menu,text = "Back To Menu",width=17,command=self.backtomenu,activebackground="Gray",background="lightyellow",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=130)
                self.window.mainloop()
        def backtomenu(self):
                self.window.destroy()
                main().menuwindow
                return
        def showes(self):
                self.window.destroy()
                equationsolver()
                return
        def showeo(self):
                self.window.destroy()
                equationsoperation()
                return

class diff(object):
        def __init__(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Calculus")
                self.window.configure(background='black')
                self.a = StringVar()
                Label(self.window,text="Enter equation",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=20)
                Entry(self.window,textvariable=self.a).place(height = 25, width=150,x=275, y=20)
                buttonenter = Button(self.window,text="Enter",command=self.getans).place(height = 25, width=50,x=222, y=50)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def back(self):
                self.window.destroy()
                main()
                return
        def getans(self):
                list1 =[]
                inputtolist(self.a.get(),list1)
                a = Poly(list1)
                ans  = a.diff()
                leb = Label(self.window,text=ans.print(),font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=90)

class integral(object):
        def __init__(self):
                self.window.destroy()
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Calculus")
                self.window.configure(background='black')
                self.a = StringVar()
                Label(self.window,text="Enter equation",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=20)
                Entry(self.window,textvariable=self.a).place(height = 25, width=150,x=275, y=20)
                buttonenter = Button(self.window,text="Enter",command=self.getans).place(height = 25, width=50,x=222, y=50)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def back(self):
                self.window.destroy()
                main()
                return
        def getans(self):
                list1 =[]
                inputtolist(self.a.get(),list1)
                a = Poly(list1)
                ans  = a.integrate()
                leb = Label(self.window,text=ans.print(),font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=90)
class tangentline(object):
        def __init__(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Calculus")
                self.window.configure(background='black')
                self.a = StringVar()
                self.b = IntVar()
                Label(self.window,text="Enter equation",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=20)
                Entry(self.window,textvariable=self.a).place(height = 25, width=150,x=275, y=20)
                Label(self.window,text="Value",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=50)
                Entry(self.window,textvariable=self.b).place(height = 25, width=150,x=275, y=50)
                buttonenter = Button(self.window,text="Enter",command=self.getans).place(height = 25, width=50,x=222, y=80)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def back(self):
                self.window.destroy()
                main()
                return
        def getans(self):
                list1 =[]
                inputtolist(self.a.get(),list1)
                eq = Poly(list1)
                deq  = eq.diff()
                m =deq.eval(self.b.get())
                y = eq.eval(self.b.get())
                c=y-(m*self.b.get())
                ans = Poly([c,m])
                leb = Label(self.window,text="y = "+ans.print(),font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=110)


class calculus(Calculatormenu):
        def showcalculus(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Calculus")
                self.window.configure(background='black')
                menu = Frame(self.window,bg='black',width=500,height=275)
                menu.place(x=0,y=0)
                title = Label(menu,text = "Calculus",bg="gold",font=("Times", "24") ).place(height =30, width=450,x=25, y=10)
                derivative = Button(menu,text = "Derivative",width=17,command=self.showdiff,activebackground="Gray",background="lightgoldenrod",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=50)
                integral = Button(menu,text = "Integral",width=17,command=self.showinte,activebackground="Gray",background="darkgoldenrod1",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=90)
                tangentline = Button(menu,text = "Tangent Line",width=17,command=self.showtan,activebackground="Gray",background="darkgoldenrod2",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=130)
                back = Button(menu,text = "Back To Menu",width=17,command=self.backtomenu,activebackground="Gray",background="darkgoldenrod3",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=170)
                self.window.mainloop()
        def backtomenu(self):
                self.window.destroy()
                main().menuwindow
                return
        def showdiff(self):
                self.window.destroy()
                diff()
                return
        def showinte(self):
                self.window.destroy()
                integral()
                return
        def showtan(self):
                self.window.destroy()
                tangentline()
                return

def fac(x):
        if x==0:return 1
        else :return x*fac(x-1) 

class factorial(object):
        def __init__(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Probability")
                self.window.configure(background='black')
                self.a = IntVar()
                Label(self.window,text="Enter a number",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=20)
                Entry(self.window,textvariable=self.a).place(height = 25, width=150,x=275, y=20)
                buttonenter = Button(self.window,text="Enter",command=self.getans).place(height = 25, width=50,x=222, y=50)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def back(self):
                self.window.destroy()
                main()
                return
        def getans(self):
                x = fac(self.a.get())
                leb = Label(self.window,text="%d! = %d"%(self.a.get(),x),font=("Times", "17"),justify=LEFT).place(height = 35, width=350,x=75, y=90)

class permutation(object):
        def __init__(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Probability")
                self.window.configure(background='black')
                self.a = StringVar()
                self.ans = []
                Label(self.window,text="Enter numbers",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=20)
                Entry(self.window,textvariable=self.a).place(height = 25, width=150,x=275, y=20)
                buttonenter = Button(self.window,text="Enter",command=self.getans).place(height = 25, width=50,x=222, y=50)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def back(self):
                self.window.destroy()
                main()
                return
        def permutation(self,lst): 
            if len(lst) == 0: 
                return [] 
            if len(lst) == 1: 
                return [lst] 
            l = []
            for i in range(len(lst)): 
               m = lst[i] 
               remLst = lst[:i] + lst[i+1:] 
               for p in self.permutation(remLst): 
                   l.append([m] + p) 
            return l 
        def getans(self):
                list1=[]
                self.ans = []
                inputtolist(self.a.get(),list1)
                for p in self.permutation(list1):
                        self.ans.append(p)
                x=190
                y=80
                index=0
                for i in range(int(len(self.a.get())/2)):
                        x=190
                        for j in range(int(len(self.a.get())/2)):
                                Label(self.window,text=self.ans[index],font=("Times", "17"),justify=LEFT).place(height = 25, width=50,x=x, y=y)
                                index+=1
                                x+=60
                        y+=30

                
class combination(object):
        def __init__(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Probability")
                self.window.configure(background='black')
                self.a = StringVar()
                self.ans = []
                Label(self.window,text="Enter numbers",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=20)
                Entry(self.window,textvariable=self.a).place(height = 25, width=150,x=275, y=20)
                buttonenter = Button(self.window,text="Enter",command=self.getans).place(height = 25, width=50,x=222, y=50)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def back(self):
                self.window.destroy()
                main()
                return
        def powerSet(self,items):
                list1=[]
                N = len(items)
                for i in range(2**N):
                        combo = []
                        for j in range(N):
                            if (i >> j) % 2 == 1:
                                combo.append(items[j])
                        list1.append(combo)
                return list1
        def getans(self):
                list1=[]
                self.ans = []
                inputtolist(self.a.get(),list1)
                self.ans = self.powerSet(list1)
                x=190
                y=80
                index=0
                try:
                        for i in range(int(len(self.ans)/2)):
                                x=190
                                for j in range(int(len(self.ans)/2)):
                                        Label(self.window,text=self.ans[index],font=("Times", "17"),justify=LEFT).place(height = 25, width=50,x=x, y=y)
                                        index+=1
                                        x+=60
                                y+=30
                except:return
         

class probability(Calculatormenu):
        def showprobability(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Probability")
                self.window.configure(background='black')
                menu = Frame(self.window,bg='black',width=500,height=275)
                menu.place(x=0,y=0)
                title = Label(menu,text = "Probability",bg="gold",font=("Times", "24") ).place(height =30, width=450,x=25, y=10)
                factorial = Button(menu,text = "Factorial",width=17,command=self.showfac,activebackground="Gray",background="lightgoldenrod",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=50)
                permutation = Button(menu,text = "Permutation",width=17,command=self.showperm,activebackground="Gray",background="darkgoldenrod1",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=90)
                combination = Button(menu,text = "Combination",width=17,command=self.showcom,activebackground="Gray",background="darkgoldenrod2",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=130)
                back = Button(menu,text = "Back To Menu",width=17,command=self.backtomenu,activebackground="Gray",background="darkgoldenrod3",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=170)
                self.window.mainloop()
        def backtomenu(self):
                self.window.destroy()
                main().menuwindow
                return
        def showfac(self):
                self.window.destroy()
                factorial()
                return
        def showperm(self):
                self.window.destroy()
                permutation()
                return
        def showcom(self):
                self.window.destroy()
                combination()
                return


class stat(Calculatormenu):
        def showstat(self):
                self.window=Tk()
                self.window.geometry("500x325+500+200")
                self.window.title("Statistics")
                self.window.configure(background='black')
                menu = Frame(self.window,bg='black',width=500,height=325)
                menu.place(x=0,y=0)
                title = Label(menu,text = "Statistics",bg="darkorange",font=("Times", "24") ).place(height =30, width=450,x=25, y=10)
                self.a = StringVar()
                self.ans = []
                Label(self.window,text="Enter numbers",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=50)
                Entry(self.window,textvariable=self.a).place(height = 25, width=150,x=275, y=50)
                buttonenter = Button(self.window,text="Enter",command=self.getans).place(height = 25, width=50,x=222, y=80)
                back = Button(menu,text = "Back To Menu",width=17,command=self.backtomenu,activebackground="Gray",background="coral",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=270)
                self.window.mainloop()
        def backtomenu(self):
                self.window.destroy()
                main().menuwindow
                return
        def getans(self):
                inputtolist(self.a.get(),self.ans)
                m = statistics.mean(self.ans)
                me = statistics.median(self.ans)
                mo = statistics.mode(self.ans)
                std = statistics.stdev(self.ans)
                var = statistics.variance(self.ans)
                Label(self.window,text="Mean of the list is "+str(m),font=("Times", "17"),justify=LEFT).place(height = 25, width=375,x=62, y=105)
                Label(self.window,text="Median of the list is "+str(me),font=("Times", "17"),justify=LEFT).place(height = 25, width=375,x=62, y=130)
                Label(self.window,text="Mode of the list is "+str(mo),font=("Times", "17"),justify=LEFT).place(height = 25, width=375,x=62, y=155)
                Label(self.window,text="Standard Deviation of the list is "+str(std),font=("Times", "17"),justify=LEFT).place(height = 25, width=375,x=62, y=180)
                Label(self.window,text="Variance of the list is "+str(var),font=("Times", "17"),justify=LEFT).place(height = 25, width=375,x=62, y=205)

class Inputmatrix(object):
        def show(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Matrix Operation")
                self.window.configure(background='black')
                self.row = StringVar()
                self.col = StringVar()
                self.row="0"
                self.col="0"
                Label(self.window,text="Row",font=("Times", "17"),justify=LEFT).place(height = 25, width=70,x=125, y=50)
                self.lebrow = Label(self.window,text=self.row,font=("Times", "17"),justify=LEFT).place(height = 25, width=100,x=195, y=50)
                plusr = Button(self.window,text = "+",command = self.plusr)
                plusr.place(height = 15, width=50,x=295, y=48)
                minusr = Button(self.window,text = "-",command = self.minusr)
                minusr.place(height = 15, width=50,x=295, y=62)
                Label(self.window,text="Column",font=("Times", "17"),justify=LEFT).place(height = 25, width=70,x=125, y=100)
                self.lebcol = Label(self.window,text=self.col,font=("Times", "17"),justify=LEFT).place(height = 25, width=100,x=195, y=100)
                plusc = Button(self.window,text = "+",command = self.plusc)
                plusc.place(height = 15, width=50,x=295, y=98)
                minusc = Button(self.window,text = "-",command = self.minusc)
                minusc.place(height = 15, width=50,x=295, y=112)
                buttonenter = Button(self.window,text="Enter",command=self.get).place(height = 25, width=50,x=222, y=130)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)  
        def back(self):
                self.window.destroy()
                main()
                return

        def plusr(self):
                n =  int(self.row)+1
                self.row = n
                self.lebrow = Label(self.window,text = self.row)
                self.lebrow.place(height = 25, width=100,x=195, y=50)
        def minusr(self):
                n =  int(self.row)-1
                if n<0:return
                self.row = n
                self.lebrow = Label(self.window,text = self.row)
                self.lebrow.place(height = 25, width=100,x=195, y=50)
        def plusc(self):
                n =  int(self.col)+1
                self.col = n
                self.lebcol = Label(self.window,text = self.col)
                self.lebcol.place(height = 25, width=100,x=195, y=100)
        def minusc(self):
                n =  int(self.col)-1
                if n<0:return
                self.col = n
                self.lebcol = Label(self.window,text = self.col)
                self.lebcol.place(height = 25, width=100,x=195, y=100)
        def get(self):
                self.window.destroy()
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Matrix Operation")
                self.window.configure(background='black')
                x=1
                for k in range (len(self.entry)):
                        Label(self.window,text ="Matrix %d"%(k+1)).grid(row=x, column=0,rowspan=self.row, sticky=NSEW)
                        for i in range(self.row):
                                col = []
                                for j in range(self.col):
                                        e = Entry(relief=RIDGE,width="5")
                                        e.grid(row=i+x, column=j+1, sticky=NSEW)
                                        col.append(e)
                                self.entry[k].append(col)
                        Label(self.window,text ="").grid(row=i+x+1, column=0,columnspan=self.col, sticky=NSEW)
                        x+=self.row+1
                buttonenter = Button(self.window,text="Enter",command=self.Press).place(x=202,y=180)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def Press(self):
                for k in range (len(self.entry)):
                        for i in range (len(self.entry[k])):
                                self.matrix[k].append([])
                                for j in range (len(self.entry[k][i])):
                                        self.matrix[k][i].append(0)
                                        self.matrix[k][i][j]=int(self.entry[k][i][j].get())
                self.window.destroy()
                self.op()


class matrixoperation(Inputmatrix):
        def __init__(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Matrix Operation")
                self.window.configure(background='black')
                Label(self.window,text="Matrix Operation",font=("Times", "17")).place(height = 35, width=360,x=75, y=0)
                Label(self.window,text="Addition",font=("Times", "17"),justify=LEFT).place(height = 35, width=300,x=75, y=40)
                Button(self.window,text="Choose",command=self.choose1).place(height = 35, width=60,x=375, y=40)
                Label(self.window,text="Subtraction",font=("Times", "17"),justify=LEFT).place(height = 35, width=300,x=75, y=80)
                Button(self.window,text="Choose",command=self.choose2).place(height = 35, width=60,x=375, y=80)
                Label(self.window,text="Multiplication",font=("Times", "17"),justify=LEFT).place(height = 35, width=300,x=75, y=120)
                Button(self.window,text="Choose",command=self.choose3).place(height = 35, width=60,x=375, y=120)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def back(self):
                self.window.destroy()
                main()
                return

        def choose1(self):
                self.choice=1
                self.window.destroy()
                self.entry=[[],[]]
                self.matrix=[[],[]]
                self.show()


        def choose2(self):
                self.choice=2
                self.window.destroy()
                self.entry=[[],[]]
                self.matrix=[[],[]]
                self.show()


        def choose3(self):
                self.choice=3
                self.window.destroy()
                self.entry=[[],[]]
                self.matrix=[[],[]]
                self.show()

        def op(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Matrix Operation")
                self.window.configure(background='black')
                matrix1=self.matrix[0]
                matrix2=self.matrix[1]

                for i in range (self.row):
                        for j in range (self.col):
                                Label(self.window,text=str(matrix1[i][j]),font=("Times", "17")).place(x=j*25+200,y=50+i*25)
                                Label(self.window,text=str(matrix2[i][j]),font=("Times", "17")).place(x=self.col*25+j*25+225,y=50+i*25)
                if self.choice==1:
                        suma=[]
                        Label(self.window,text="Addition",font=("Times", "17"),justify=LEFT).place(x=222,y=0)
                        Label(self.window,text="+",font=("Times", "17")).place(x=self.col*25+200,y=self.row*25+12)
                        Label(self.window,text="=",font=("Times", "17")).place(x=self.col*50+225,y=self.row*25+12)
                        for i in range (self.row):
                                suma.append([])
                                for j in range (self.col):
                                        suma[i].append(0)
                                        suma[i][j] = matrix1[i][j] + matrix2[i][j]
                                        Label(self.window,text=str(suma[i][j]),font=("Times", "17")).place(x=self.col*50+j*25+250,y=50+i*25)
                if self.choice==2:
                        sub=[]
                        Label(self.window,text="Subtraction",font=("Times", "17"),justify=LEFT).place(x=222,y=0)
                        Label(self.window,text="-",font=("Times", "17")).place(x=self.col*25+200,y=self.row*25+12)
                        Label(self.window,text="=",font=("Times", "17")).place(x=self.col*50+225,y=self.row*25+12)
                        for i in range (self.row):
                                sub.append([])
                                for j in range (self.col):
                                        sub[i].append(0)
                                        sub[i][j] = matrix1[i][j] - matrix2[i][j]
                                        Label(self.window,text=str(sub[i][j]),font=("Times", "17")).place(x=self.col*50+j*25+250,y=50+i*25)
                
                if self.choice==3:
                        mul=[]
                        Label(self.window,text="Multiplication",font=("Times", "17"),justify=LEFT).place(x=222,y=0)
                        Label(self.window,text="x",font=("Times", "17")).place(x=self.col*25+200,y=self.row*25+12)
                        Label(self.window,text="=",font=("Times", "17")).place(x=self.col*50+225,y=self.row*25+12)
                        for i in range (self.row):
                                mul.append([])
                                for j in range (self.col):
                                        mul[i].append(0)
                                        for k in range(self.col):
                                                mul[i][j] += matrix1[i][k] * matrix2[k][j]
                                        Label(self.window,text=str(mul[i][j]),font=("Times", "17")).place(x=self.col*50+j*25+250,y=50+i*25)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
class transpose(Inputmatrix):
        def __init__(self):
                self.entry=[[]]
                self.matrix=[[]]
                self.show()
        def op(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Matrix Transpose")
                self.window.configure(background='black')
                matrix=self.matrix[0]
                tran=[]
                Label(self.window,text="Transpose",font=("Times", "17"),justify=LEFT).place(x=222,y=0)
                for i in range (self.row):
                        for j in range (self.col):
                                Label(self.window,text=str(matrix[i][j]),font=("Times", "17")).place(x=j*25+200,y=50+i*25)
                Label(self.window,text="TO",font=("Times", "17")).place(x=self.col*25+195,y=self.row*25)
                for i in range (self.col):
                        tran.append([])
                        for j in range (self.row):
                                tran[i].append(0)
                                tran[i][j] = matrix[j][i]
                                Label(self.window,text=str(tran[i][j]),font=("Times", "17")).place(x=self.col*25+j*25+225,y=50+i*25)
                buttonexit = Button(self.window,text="Back",command=self.back).place(x=0,y=200)
        def back(self):
                self.window.destroy()
                main()
                return

class matrix(Calculatormenu):
        def showmatrix(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Matrix")
                self.window.configure(background='black')
                menu = Frame(self.window,bg='black',width=500,height=275)
                menu.place(x=0,y=0)
                title = Label(menu,text = "Matrix",bg="darkorange",font=("Times", "24") ).place(height =30, width=450,x=25, y=10)
                operation = Button(menu,text = "Matrix Operations",width=17,command=self.showmo,activebackground="Gray",background="coral",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=50)
                transpose = Button(menu,text = "Matrix Transpose",width=17,command=self.showtp,activebackground="Gray",background="orangered",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=90)
                back = Button(menu,text = "Back To Menu",width=17,command=self.backtomenu,activebackground="Gray",background="red",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=130)
                self.window.mainloop()
        def backtomenu(self):
                self.window.destroy()
                main().menuwindow
                return
        def showmo(self):
                self.window.destroy()
                matrixoperation()
                return
        def showtp(self):
                self.window.destroy()
                transpose()
                return

class graphs(Calculatormenu):
        def showgraphs(self):
                self.window=Tk()
                self.window.geometry("500x225+500+200")
                self.window.title("Graphs")
                self.window.configure(background='black')
                menu = Frame(self.window,bg='black',width=500,height=275)
                menu.place(x=0,y=0)
                title = Label(menu,text = "Graphs",bg="coral",font=("Times", "24") ).place(height =30, width=450,x=25, y=10)
                self.a = StringVar()
                Label(self.window,text="Enter your equation :",font=("Times", "17"),justify=LEFT).place(height = 25, width=200,x=75, y=50)
                Entry(self.window,textvariable=self.a).place(height = 25, width=150,x=275, y=50)
                buttonenter = Button(self.window,text="Enter",command=self.enter).place(height = 25, width=50,x=222, y=80)
                back = Button(menu,text = "Back To Menu",width=17,command=self.backtomenu,activebackground="Gray",background="coral",foreground="black",font=("Times", "16")).place(height = 35, width=350,x=75, y=180)
                self.window.mainloop()
        def backtomenu(self):
                self.window.destroy()
                main().menuwindow
                return
        def enter(self):
                list1=[]
                inputtolist(self.a.get(),list1)
                eq = Poly(list1)
                graph=[]
                Label(self.window,text="Your equation : "+eq.print(),font=("Times", "17"),justify=LEFT).place(height = 25, width=375,x=75, y=120)
                for i in range(-50,50):
                        graph.append((i,eq.eval(i)))
                speed(0)
                penup()
                goto(-5000,0)
                pendown()
                forward(100000)
                penup()
                goto(0,-50000)
                setheading(90)
                pendown()
                forward(100000)
                penup()
                goto(graph[0][0],graph[0][1])
                pendown()
                pencolor("red")
                for i in range (len(graph)):
                        goto(graph[i][0]*10,graph[i][1])
                        write("%d,%d"%(graph[i][0],graph[i][1]))
    
class main(calculator,numoperation,algebra,calculus,probability,stat,matrix,graphs):
    def __init__(self):
        self.menuwindow()
    def menuwindow(self):
        self.window=Tk()
        self.window.geometry("500x225+500+200")
        self.window.title("Advanced Mathematics Calculator")
        self.window.configure(background='black')
        menu = Frame(self.window,bg='black',width=500,height=275)
        menu.place(x=0,y=0)
        title = Label(menu,text = "Advanced Mathematics Calculator",bg="orchid",font=("Times", "24", "bold") )
        choose = Label(menu,text = "Menu",bg="deepskyblue",fg="black",font=("Times", "17", "bold"))
        calculator = Button(menu,text = "Calculator",width=17,command=self.showcal,activebackground="Gray",background="turquoise",foreground="black",font=("Times", "16"))
        num = Button(menu,text = "Number Operations",width=17,activebackground="Gray",font=("Times", "16"),background="greenyellow",foreground="black",command=self.numop)
        al = Button(menu,text = "Algebra",width=17,activebackground="Gray",font=("Times", "16"),background="greenyellow",foreground="black",command=self.algebra)
        cal = Button(menu,text = "Calculus",width=17,activebackground="Gray",font=("Times", "16"),background="gold",foreground="black",command=self.calculus)
        pro =  Button(menu,text = "Probability",width=17,activebackground="Gray",font=("Times", "16"),background="gold",foreground="black",command=self.probability)
        sta = Button(menu,text = "Statistic",width=17,activebackground="Gray",font=("Times", "16"),background="darkorange",foreground="black",command=self.statistics)
        ma = Button(menu,text = "Matrix",width=17,activebackground="Gray",font=("Times", "16"),background="darkorange",foreground="black",command =self.matrix)
        gra = Button(menu,text = "Graphs",width=17,activebackground="Gray",font=("Times", "16"),background="salmon",foreground="black",command=self.graphs)
        title.place(height =25, width=450,x=25, y=10)
        choose.place(height = 25, width=150,x=175, y=40 )
        calculator.place(height = 25, width=150,x=175, y=70)
        num.place(height = 25, width=150,x=75, y=100 )
        al.place(height = 25, width=150,x=275, y=100 )
        cal.place(height = 25, width=150,x=75, y=130 )
        pro.place(height = 25, width=150,x=275, y=130 )
        sta.place(height = 25, width=150,x=75, y=160 )
        ma.place(height = 25, width=150,x=275, y=160 )
        gra.place(height = 25, width=150,x=175, y=190 )
        self.window.mainloop()
        return
    def  numop(self):
        self.window.destroy()
        self.shownumop()
        return
    def algebra(self):
        self.window.destroy()
        self.showalgebra()
        return
    def calculus(self):
        self.window.destroy()
        self.showcalculus()
        return
    def probability(self):
        self.window.destroy()
        self.showprobability()
        return
    def statistics(self):
        self.window.destroy()
        self.showstat()
        return
    def matrix(self):
        self.window.destroy()
        self.showmatrix()
        return
    def graphs(self):
        self.window.destroy()
        self.showgraphs()
        return
        
main()
