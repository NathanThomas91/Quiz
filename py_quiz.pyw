from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Quiz')
root.geometry("1000x700")
a = Frame(root)
a.pack(side="top", expand=True, fill="both")



sports = {"Question":["Q1. What is Usain Bolt's 100m world record time",
                 "Q2. A penalty in football is taken how many yards away from the goal?",
                 "Q3. Who has scored the most Premier League hat-tricks?",
                 "Q4. Who did England beat in the 2019 cricket World Cup final?",
                 "Q5. World's highest polo ground, is located in Pakistan.",
                 "Q6. Who won BBC's Sports Personality of the Year prize 2020?",
                 "Q7.  Katarina Johnson-Thompson is world champion in which sport??"],
     "Answer":[2,1,4,3,3,1,1],
     "Options":[['15.3', '9.58', '19.58','5.10'],
                ['12 yards', '6 yards', '15 yards', '10 yards'],
                ['Alan Shearer','Cristiano Ronaldo','Lionel Messi','Sergio Aguero'],
                ['England','Bangladesh','New Zealand','India'],
                ['Kasur','Attock','Shandur','Okara'],
                ['Lewis Hamilton','Michael Schumacher','Jordan Henderson','Hollie Doyle'],
                ['Athletics','Swimming','Football','Cricket']]}


technology = {"Question":["Q1. What technology is used to make telephone calls over the Internet possible?",
                 "Q2. Which computer language is the most widely used?",
                 "Q3. What technology is used to record cryptocurrency transactions?",
                 "Q4. What does the Internet prefix WWW stand for?",
                 "Q5. A network designed to allow communication within an organization is called?",
                 "Q6. What operating system did Google develop?",
                 "Q7. What does the acronym FTP stand for?"],
     "Answer":[4,2,3,2,4,1,2],
     "Options":[['Bluetooth', 'Ethernet', 'NFC', 'VoIP'],
                ['C#', 'Java', 'Swift', 'PHP'],
                ['Digital wallet', 'Mining', 'Blockchain', 'Token'],
                ['Western Washington World', 'World Wide Web', 'Wide Width Wickets', 'Worldwide Weather'],
                ['The Internet', 'The World Wide Web', 'A browser', 'An intranet'],
                ['Android', 'iOS', 'Windows', 'BlackBerry OS'],
                ['Free transistor protocol', 'File transfer protocol', 'File tripling power', 'Fast total processing']]}



geography = {"Question":["Q1. Which country has the longest coastline in the world?",
                 "Q2. What is the capital of the Philippines?",
                 "Q3. What is the World's Smallest Country?",
                 "Q4. In which country is the world's highest waterfall?",
                 "Q5. What country has the greatest number of active volcanoes?",
                 "Q6. Where was the hottest temperature ever recorded?",
                 "Q7. Which of these countries has three national capitals?"],
     "Answer":[3,2,1,4,1,3,2],
     "Options":[['Russia', 'Indonesia', 'Canada', 'Australia'],
                ['Jakarta', 'Manila', 'Dili', 'Marawi'],
                ['Vatican City', 'Monaco', 'Lichtenstein', 'Luxembourg'],
                ['Brazil', 'USA', 'South Africa', 'Venezuela'],
                ['Indonesia', 'Italy', 'Japan', 'Philippines'],
                ['Mexico', 'India', 'Libya', 'Peru'],
                ['Bolivia', 'South Africa', 'Nepal', 'Morroco']]}

python = {"Question":["Q1. What is the correct file extension for Python files?",
                 "Q2. Which operator is used to multiply numbers?",
                 "Q3. Which statement is used to stop a loop?",
                 "Q4. What is the method inside the class in python language?",
                 "Q5. Which character is used in Python to make a single line comment?",
                 "Q6. In which year was the Python language developed?",
                 "Q7. Who developed the Python language?"],
     "Answer":[4,3,1,4,2,1,2],
     "Options":[['.pyt', '.pyth', '.pt', '.py'],
                ['#', 'X', '*', '%'],
                ['break', 'exit', 'return', 'stop'],
                ["Object", "Argument", "Attribute", "Function"],
                ['/', '#', '//', '!'],
                ['1989', '1981', '1972', '1995'],
                ['Zim Den', 'Guido van Rossum', 'Niene Stom', 'Wick van Rossum']]}




que1 = (sports['Question'])
ans1 = (sports['Answer'])
opt1 = (sports['Options'])

que2 = (technology['Question'])
ans2 = (technology['Answer'])
opt2 = (technology['Options'])

que3 = (geography['Question'])
ans3 = (geography['Answer'])
opt3 = (geography['Options'])

que4 = (python['Question'])
ans4 = (python['Answer'])
opt4 = (python['Options'])

xyz = que1
yxz = ans1
zyx = opt1


class quiz:
    def __init__(self):
        self.qno = 0
        self.cor = 0
        self.length = len(xyz)
        self.optselected = IntVar()
        self.menubar()
        self.displaytitle("ABC Quiz")
        self.welcome_screen()
    def welcome_screen(Self):
        l1 = Label(a, text = "Welcome in Quiz ", width = 50, bg = 'lightblue',fg = 'black', font = ('arial',30,'bold'))
        l1.place(x = 120, y = 100)
      
        #Setting it up
        img = ImageTk.PhotoImage(Image.open("quiz-time.jpg"))


        #Displaying it
        imglabel = Label(a, image=img, width = 700, height =500)
        imglabel.image = img
        imglabel.place(x=400, y = 200)
       

    def clear_frame(self):
        for widgets in a.winfo_children():
            widgets.destroy()
        self.qno = 0
        self.cor = 0

    def createradiobutton(self):
        v1 = []
        v2 = 150
        while len(v1) < 4:
            abc = Radiobutton(a, text = ' ', variable = self.optselected , fg = 'black', font = ('',18,''), value = len(v1) + 1)
            abc.place(x = 100, y = v2)
            v1.append(abc)
            v2 = v2 + 40
        return v1
    def dest(self):
        messagebox.showinfo("Bye Bye","Thank you for playing game...... \n have a Nice Day")
        root.destroy()
    def displayoptions(self):
        count = 0
        for v3 in zyx[self.qno]:
            self.radiobuttoncontrol[count]['text'] = v3
            count = count + 1
    def displaytitle(self, title):
        l1 = Label(a, text = title, width = 100, bg = 'darkblue',fg = 'black', font = ('arial',20,'bold'))
        l1.place(x = -150, y = 0)
    def displayquestion(self):
        l2 = Label(a, text = xyz[self.qno], width = 63, bg = 'darkblue', fg = 'white', font = ('arial',15,''))
        l2.place(x = 100, y = 70)
    def createbutton(self):
        b1 = Button(a, text = 'Next', command = self.nextbutton, width = 50, bg = 'darkblue', fg = 'white')
        b2 = Button(a, text = 'Exit', command = self.dest, width = 10, height= 2, bg = 'darkblue', fg = 'red',font = ('arial',20,'bold'))
        b1.place(x = 350, y = 350)
        b2.place(x = 1200, y = 600)
    def checkanswer(self, questiono):
        if self.optselected.get() == yxz[questiono]:
            return True
    def displayresult(self):
        wrong = self.length - self.cor
        wrong = f"Wrong: {wrong}"
        abc = f"correct: {self.cor}"
        percentage = self.cor / self.length * 100
        Result = f"percentage: {percentage}%"
        messagebox.showinfo("Result",f"{abc}\n{wrong}\n{Result}")
    def nextbutton(self):
        if self.checkanswer(self.qno):
            self.cor = self.cor + 1
        self.qno = self.qno + 1
        if self.qno == self.length:
            self.displayresult()
            self.clear_frame()
            self.displaytitle("ABC Quiz")
            self.welcome_screen()
        else:
            self.displayquestion()
            self.displayoptions()

    def sports1(self):

        global xyz
        global yxz
        global zyx
        global l1
        xyz = que1
        yxz = ans1
        zyx = opt1
        self.clear_frame()
        
        self.radiobuttoncontrol = self.createradiobutton()
        self.displaytitle("Sports Quiz")
        self.displayquestion()
        self.displayoptions()
        self.createbutton()
       
        
    def technology1(self):

        global xyz
        global yxz
        global zyx
        xyz = que2
        yxz = ans2
        zyx = opt2
        
        self.clear_frame()
        self.radiobuttoncontrol = self.createradiobutton()
        self.displaytitle("Technology Quiz")
        self.displayquestion()
        self.displayoptions()
        self.createbutton()
    
    def geography1(self):
        global xyz
        global yxz
        global zyx
        xyz = que3
        yxz = ans3
        zyx = opt3

        self.clear_frame()
        self.radiobuttoncontrol = self.createradiobutton()
        self.displaytitle("Geography Quiz")
        self.displayquestion()
        self.displayoptions()
        self.createbutton()
        
    def python1(self):
        self.clear_frame()
        global xyz
        global yxz
        global zyx
        xyz = que4
        yxz = ans4
        zyx = opt4
        
        
        self.radiobuttoncontrol = self.createradiobutton()
        self.displaytitle("Python Quiz")
        self.displayquestion()
        self.displayoptions()
        self.createbutton()
       
       
        
    def about(self):
        messagebox.showinfo("About Quiz","This is a Quiz program made using Python \n Instruction:\n Category menu is to change the topic \n Next button is to change the question \n Exit button is to leave ") 
    def menubar(self):
        MenuBar1 = Menu(root)
        SubMenu1 = Menu(MenuBar1, tearoff = 0)
        MenuBar1.add_cascade(label = 'Category', menu = SubMenu1)
        SubMenu1.add_command(label = 'Sports', command = self.sports1)
        SubMenu1.add_command(label = 'Technology', command = self.technology1)
        SubMenu1.add_command(label = 'Geography', command = self.geography1)
        SubMenu1.add_command(label = 'python', command = self.python1)

        SubMenu2 = Menu(MenuBar1, tearoff = 0)
        MenuBar1.add_cascade(label = 'Help', menu = SubMenu2)
        SubMenu2.add_command(label = 'About', command = self.about)

        root.config(menu = MenuBar1)
          
obj1 = quiz()
a.mainloop()
