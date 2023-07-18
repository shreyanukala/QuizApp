import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
global r1
global r2
global r3
global r4
global r5
global sum
root=tk.Tk()
root.geometry("1920x1080")
image=Image.open('C:\\Users\\Shreya\\OneDrive\\Desktop\\Project\\My-project.ppm')
img=image.resize((1920, 1080))
bgimg=ImageTk.PhotoImage(img)
limg=Label(root,image=bgimg).place(x=0,y=0)
root.title("Quiz Game")
label=tk.Label(root,text="Quiz",font=('Arial',80))
label.pack(padx=20, pady=20)
labe2=tk.Label(root,text="Login",font=('Arial',30))
labe2.pack(padx=20, pady=20)
labe3=tk.Label(root,text="e-mail",font=('Arial',20))
labe3.place(x=650, y=300)
myentry=tk.Entry(root)
myentry.place(x=650,y=350,height=40,width=300)
labe4=tk.Label(root,text="Username",font=('Arial',20))
labe4.place(x=650, y=400)
myentry1=tk.Entry(root)
myentry1.place(x=650,y=450,height=40,width=300)
labe4=tk.Label(root,text="password",font=('Arial',20))
labe4.place(x=650, y=500)
myentry2=tk.Entry(root)
myentry2.place(x=650,y=550,height=40,width=300)
#checkvar1=IntVar()
#C1=Checkbutton(root,text="I am ready for the quiz",variable=checkvar1,height=5,width=20)
#C1.place(x=500,y=600)

def onClick():
    global sum 
    global img1
    sum=0
    tk.messagebox.showinfo("Alert message","Are you sure?")
    root.destroy()
    new1=tk.Tk()
    new1.geometry("1920x1080")
    new1.title("Quiz Question 1")
    labels=tk.Label(new1,text="Question 1",font=('Arial',60))
    labels.pack(padx=20, pady=20)
    label=tk.Label(new1,text="",font=('Arial',60))
    l1=tk.Label(new1,text="Q1) Who is the President of India?",font=('Arial',30))
    l1.place(x=500, y=150)
    l=[]
    for i in range(4):
        option=IntVar()
        option.set(0)
        l.append(option)
    def display():
        global sum
        global r1
        r1=l[0].get()
        if(r1==1):
            sum+=1
        return     
    Checkbutton(new1,text="Droupadi Murmu",font=("Arial",25),variable=l[0],command=display).place(x=550,y=250)
    Checkbutton(new1,text="Ram Nath Kovind",font=("Arial",25),variable=l[1]).place(x=550,y=350)
    Checkbutton(new1,text="Indira Gandhi",font=("Arial",25),variable=l[2]).place(x=550,y=450)
    Checkbutton(new1,text="Prathibha Patil",font=("Arial",25),variable=l[3]).place(x=550,y=550)
    def countdown(count):
        label['text']=count
        label.place(x=1300,y=80)
        if(count>0):
            new1.after(1000,countdown,count-1)
        else:
            q1()
    countdown(15)
    def q1():
        new1.destroy()
        new2=tk.Tk()
        new2.geometry("2000x2000")
        new2.title("Quiz Question 2")
        labels=tk.Label(new2,text="Question 2",font=('Arial',60))
        labels.pack(padx=20, pady=20)
        label=tk.Label(new2,text="",font=('Arial',60))
        l1=tk.Label(new2,text="Q2) Who is the Prime Minister of India?",font=('Arial',30))
        l1.place(x=500, y=150)
        l=[]
        for i in range(4):
            option=IntVar()
            option.set(0)
            l.append(option)
        def display1():
            global sum
            global r2
            r2=l[0].get()
            if(r2==1):
                sum+=1
            return
        Checkbutton(new2,text="Narendra Modi",font=("Arial",25),variable=l[0],command=display1).place(x=550,y=250)
        Checkbutton(new2,text="Manmohan Singh",font=("Arial",25),variable=l[1]).place(x=550,y=350)
        Checkbutton(new2,text="Nirmala Sitaraman",font=("Arial",25),variable=l[2]).place(x=550,y=450)
        Checkbutton(new2,text="Amit Shah",font=("Arial",25),variable=l[3]).place(x=550,y=550)
        def countdown(count):
            label['text']=count
            label.place(x=1300,y=80)
            if(count>0):
                new2.after(1000,countdown,count-1)
            else:
                q2()
        countdown(15)
        def q2():
            new2.destroy() 
            new3=tk.Tk()
            new3.geometry("2000x2000")
            new3.title("Quiz Question 3")
            labels=tk.Label(new3,text="Question 3",font=('Arial',60))
            labels.pack(padx=20, pady=20)
            label=tk.Label(new3,text="",font=('Arial',60))
            l1=tk.Label(new3,text="Q3)What is the capital of India?",font=('Arial',30))
            l1.place(x=500, y=150)
            l=[]
            for i in range(4):
                option=IntVar()
                option.set(0)
                l.append(option)
            def display2():
                global sum
                global r3
                r3=l[1].get()
                if(r3==1):
                    sum+=1
                return
            Checkbutton(new3,text="Hyderabad",font=("Arial",25),variable=l[0]).place(x=550,y=250)
            Checkbutton(new3,text="New Delhi",font=("Arial",25),variable=l[1],command=display2).place(x=550,y=350)
            Checkbutton(new3,text="Bangalore",font=("Arial",25),variable=l[2]).place(x=550,y=450)
            Checkbutton(new3,text="Chennai",font=("Arial",25),variable=l[3]).place(x=550,y=550)
            def countdown(count):
                label['text']=count
                label.place(x=1300,y=80)
                if(count>0):
                    new3.after(1000,countdown,count-1)
                else:
                    q3()
            countdown(15)
            def q3():
                new3.destroy()
                new4=tk.Tk()
                new4.geometry("2000x2000")
                new4.title("Quiz Question 4")
                labels=tk.Label(new4,text="Question 4",font=('Arial',60))
                labels.pack(padx=20, pady=20)
                label=tk.Label(new4,text="",font=('Arial',60))
                l1=tk.Label(new4,text="Q4)What is the national animal of India?",font=('Arial',30))
                l1.place(x=500, y=150)
                l=[]
                for i in range(4):
                    option=IntVar()
                    option.set(0)
                    l.append(option)
                def display3():
                    global sum
                    global r4
                    r4=l[3].get()
                    if(r4==1):
                        sum+=1
                    return
                Checkbutton(new4,text="Lion",font=("Arial",25),variable=l[0]).place(x=550,y=250)
                Checkbutton(new4,text="Cheetah",font=("Arial",25),variable=l[1]).place(x=550,y=350)
                Checkbutton(new4,text="Cow",font=("Arial",25),variable=l[2]).place(x=550,y=450)
                Checkbutton(new4,text="Tiger",font=("Arial",25),variable=l[3],command=display3).place(x=550,y=550)
                def countdown(count):
                    label['text']=count
                    label.place(x=1300,y=80)
                    if(count>0):
                        new4.after(1000,countdown,count-1)
                    else:
                        q4()
                countdown(15)
                def q4():
                    new4.destroy()
                    new5=tk.Tk()
                    new5.geometry("2000x2000")
                    new5.title("Quiz Question 5")
                    labels=tk.Label(new5,text="Question 5",font=('Arial',60))
                    labels.pack(padx=20, pady=20)
                    label=tk.Label(new5,text="",font=('Arial',60))
                    l1=tk.Label(new5,text="Q5)How many states are there in India?",font=('Arial',30))
                    l1.place(x=500, y=150)
                    l=[]
                    for i in range(4):
                        option=IntVar()
                        option.set(0)
                        l.append(option)
                    def display4():
                        global sum
                        global r5
                        r5=l[3].get()
                        if(r5==1):
                            sum+=1
                        return
                    Checkbutton(new5,text="28",font=("Arial",25),variable=l[0]).place(x=550,y=250)
                    Checkbutton(new5,text="33",font=("Arial",25),variable=l[1]).place(x=550,y=350)
                    Checkbutton(new5,text="30",font=("Arial",25),variable=l[2]).place(x=550,y=450)
                    Checkbutton(new5,text="29",font=("Arial",25),variable=l[3],command=display4).place(x=550,y=550)
                    def countdown(count):
                        label['text']=count
                        label.place(x=1300,y=80)
                        if(count>0):
                            new5.after(1000,countdown,count-1)
                        else:
                            end()
                    countdown(15)
                    def end():
                        tk.messagebox.showinfo("Alert message","Are you sure you want to submit?")
                        new5.destroy()
                        score=tk.Tk()
                        score.geometry("2000x2000")
                        score.title("Score")
                        label=tk.Label(score,text="Score",font=('Arial',60))
                        label.pack(padx=20, pady=20)
                        label=tk.Label(score,text=f"{sum} is the FINAL SCORE",font=("Arial",60))
                        label.pack(padx=10,pady=10)
                        label=tk.Label(score,text=f"{r1}-score in Question 1",font=("Arial",30))
                        label.pack(padx=10,pady=10)
                        label=tk.Label(score,text=f"{r2}-score in Question 2",font=("Arial",30))
                        label.pack(padx=10,pady=10)
                        label=tk.Label(score,text=f"{r3}-score in Question 3",font=("Arial",30))
                        label.pack(padx=10,pady=10)
                        label=tk.Label(score,text=f"{r4}-score in Question 4",font=("Arial",30))
                        label.pack(padx=10,pady=10)
                        label=tk.Label(score,text=f"{r5}-score in Question 5",font=("Arial",30))
                        label.pack(padx=10,pady=10)
                        

                    b1=tk.Button(new5,text="Submit",font=("Arial",20),command=end)
                    b1.place(x=1000,y=600)
                b1=tk.Button(new4,text="Next",font=("Arial",20),command=q4)
                b1.place(x=1000,y=600)

            b1=tk.Button(new3,text="Next",font=("Arial",20),command=q3)
            b1.place(x=1000,y=600)
        b1=tk.Button(new2,text="Next",font=("Arial",20),command=q2)
        b1.place(x=1000,y=600)
    b1=tk.Button(new1,text="Next",font=("Arial",20),command=q1)
    b1.place(x=1000,y=600)
    
    

annother=tk.Button(root,text="Start Quiz",font=("Arial",20),activeforeground='red',command=onClick)
annother.place(x=1000,y=600)


root.mainloop()




