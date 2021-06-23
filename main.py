from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import serial
import threading
from datetime import datetime
from  datetime import timedelta
from Golovna import Stolic,Fon,Stolic_time,Stolic_Text,ResetButton,Timer_Menu,Drop
from Zakaz import  NameZakaz,OthderTextZakaz,ButtonZakaz,NumTable,HourZakaz
from menu import M_Text
import mysql.connector
from mysql.connector import connect, Error,cursor
from time import sleep
import webbrowser
#Серійний порт
ser = serial.Serial('COM3', 9600)
#БАЗА ДАНИХ
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="billiard_room_statistics "
)
mycursor = mydb.cursor()
billiard_room_statistics = """
INSERT INTO main_info 
( ordertime,	tablenumber)
VALUES ( %s ,%s)
"""

#Налоштування головного вікна
window = Tk()
window.title('Billiards manager V1')
window.geometry('700x780')
window.configure(bg='#f7fffd')
#Налаштування вкладок
nb = ttk.Notebook(window,height=800)
nb.pack(pady=5,fill='both')
Vkladki =['Golovna','Zakaz','Bronik','Menu','Quest']
i= 0
while i<=4:
    Vkladki[i] = ttk.Frame(window)
    i +=1

nb.add(Vkladki[0],text='Головна')
nb.add(Vkladki[1],text='Новий заказ')
nb.add(Vkladki[3],text='Меню')

#Імпорт картинок
table_img_one ="image/table.png"
img = ImageTk.PhotoImage(Image.open(table_img_one))
panel = tk.Label(Vkladki[0], image=img)

stan_null_img="image/Gray.png"
gray = ImageTk.PhotoImage(Image.open(stan_null_img))
stan_gray =tk.Label(Vkladki[0], image= gray)

reset_img = "image/reset.png"
reset = ImageTk.PhotoImage(Image.open(reset_img))
resetI =tk.Label(Vkladki[0], image= reset)

red_img = "image/red.png"
red = ImageTk.PhotoImage(Image.open(red_img))
redI = tk.Label(Vkladki[0],image = red)

forTime_img = "image/forTime.png"
forTime = ImageTk.PhotoImage(Image.open(forTime_img))
forTimeI = tk.Label(Vkladki[0],image = forTime)

order_img = "image/order.png"
order = ImageTk.PhotoImage(Image.open(order_img))
orderI = tk.Label(Vkladki[1],image = order)

admin_img = "image/admin.png"
admin = ImageTk.PhotoImage(Image.open(admin_img))
adminI = tk.Label(Vkladki[2],image = admin)


#Налаштування  стилю фону вкладок
fon = [1,2,3,4,5]
Fon(0,fon,Vkladki)

#Годинник
Timer = [1,2,3]
Timer_Menu(0,Timer,Vkladki,forTime)

clock = (datetime.now()).strftime('%H:%M:%S')
Clocks = tk.Label(
    Vkladki[0],
    text=clock,
    font=('Arial Black', 28),
    bg='#086e02',
    )
def clock_update():
    while True:

        Clocks['text'] = (datetime.now()).strftime('%H:%M:%S')
        sleep(1)

process = threading.Thread(target=clock_update)
process.start()
#Налаштування стилю столів
table = [1, 2, 3, 4, 5, 6]
Stolic(0,table,Vkladki,img)
Stolic(1,table,Vkladki,img)
Stolic(2,table,Vkladki,img)
Stolic(3,table,Vkladki,img)
Stolic(4,table,Vkladki,img)
Stolic(5,table,Vkladki,img)
#Налаштування стилю номера стола
text = [1, 2, 3, 4, 5, 6]
Stolic_Text(0,text,Vkladki)

#Налаштування стилю стану стола
stan = [1, 2, 3, 4, 5, 6]
Stolic(0,stan,Vkladki,gray)
Stolic(1,stan,Vkladki,gray)
Stolic(2,stan,Vkladki,gray)
Stolic(3,stan,Vkladki,gray)
Stolic(4,stan,Vkladki,gray)
Stolic(5,stan,Vkladki,gray)
#Налаштування стилю часу стола
times = [1, 2, 3, 4, 5, 6]
Stolic_time(0,times,Vkladki)
Stolic_time(1,times,Vkladki)
Stolic_time(2,times,Vkladki)
Stolic_time(3,times,Vkladki)
Stolic_time(4,times,Vkladki)
Stolic_time(5,times,Vkladki)
#Налаштування кнопки скидання

res = [1, 2, 3, 4, 5, 6]
ResetButton(0,res,Vkladki,reset,lambda i=0,stan=stan,gray=gray,ser=ser,Vkladki=Vkladki : Drop(i,stan,gray,ser,Vkladki))
ResetButton(1,res,Vkladki,reset,lambda i=1,stan=stan,gray=gray,ser=ser ,Vkladki=Vkladki: Drop(i,stan,gray,ser,Vkladki))
ResetButton(2,res,Vkladki,reset,lambda i=2,stan=stan,gray=gray,ser=ser ,Vkladki=Vkladki : Drop(i,stan,gray,ser,Vkladki))
ResetButton(3,res,Vkladki,reset,lambda i=3,stan=stan,gray=gray,ser=ser ,Vkladki=Vkladki : Drop(i,stan,gray,ser,Vkladki))
ResetButton(4,res,Vkladki,reset,lambda i=4,stan=stan,gray=gray,ser=ser ,Vkladki=Vkladki: Drop(i,stan,gray,ser,Vkladki))
ResetButton(5,res,Vkladki,reset,lambda i=5,stan=stan,gray=gray,ser=ser ,Vkladki=Vkladki: Drop(i,stan,gray,ser,Vkladki))
PortsOff = [1,2,3,4,5,6]
#Налаштування вкладки Заказ
Zakaz_Name = [1,2]
NameZakaz(0,Zakaz_Name,Vkladki,'Забронювати стіл :')
NameZakaz(1,Zakaz_Name,Vkladki,'Новий заказ:')

Zakaz_Other_Text = [1,2,3,4]
OthderTextZakaz(0,Zakaz_Other_Text,Vkladki,'Номер стола :')
OthderTextZakaz(1,Zakaz_Other_Text,Vkladki,'З :          по :        годину ')
OthderTextZakaz(2,Zakaz_Other_Text,Vkladki,'Номер стола :')
OthderTextZakaz(3,Zakaz_Other_Text,Vkladki,'Кількість годин : ')


#Змінні для  обробки заказу
Seconds = [1,2,3,4,5,6]
ports =[1,2,3,4,5,6]
PortsON = [1,2,3,4,5,6]
PortsOff = [1,2,3,4,5,6]
Time_off = [1,2,3,4,5,6]
delay = [1,2,3,4,5,6]
Price = 100
cost = 0
#Функція обробки заказу
def ChabgeStan():
    n = Zakaz_Num[1].get()
    n = int(n) - 1
    h = Zakaz_Hour[2].get()
    h = int(h)
    x = datetime.now()
    Time_off[n] = timedelta(hours=x.hour, minutes=x.minute, seconds=x.second) + timedelta(hours=h)
    timer = timedelta(hours=h, minutes=0, seconds=0)
    riv  = int(x.hour)+h
    if riv > 24 :
        ErrorZakaz = tk.Toplevel(Vkladki[1], bg='#086e02')
        ErrorZakaz.geometry('400x100')
        ErrorZakaz.resizable(False, False)
        def ErrorExit():
            ErrorZakaz.destroy()
        ErrorText = tk.Label(ErrorZakaz,
                            text="Виберіть меншу кількість годин!!!",
                            font=('Arial Black', 14),
                            bg='#086e02')
        ErrorOk = tk.Button(ErrorZakaz,
                            text='OK',
                            font=('Arial Black', 14),
                            width=20,
                            height=1,
                            bg='#fa2525',
                            command=ErrorExit
                            )
        ErrorText.place(x=15,y=10)
        ErrorOk.place(x=60,y=45)
    else:
        cost = Price*h
        stan[n].configure(image=red)
        times[n].configure(text=timer)
        Seconds[n] = h *60*60
        ports[n] = (n+1) * 10
        PortsON[n] = ports[n] +1
        PortsOff[n] = ports[n]
        ser.write(str(PortsON[n]).encode())
        delay =(timer).total_seconds()
        SumaZakaz = tk.Toplevel(Vkladki[1], bg='#086e02')
        SumaZakaz.geometry('300x200')
        SumaZakaz.resizable(False, False)

        SumaText = tk.Label(SumaZakaz,
                            text="Заказ сформовано!",
                            font=('Arial Black', 16),
                            bg='#086e02')
        SumaNum = tk.Label(SumaZakaz,
                            text=f"Номер стола : {n+1}",
                            font=('Arial Black', 14),
                            bg='#086e02')
        SumaTime = tk.Label(SumaZakaz,
                           text=f"До : {Time_off[n]}",
                           font=('Arial Black', 14),
                           bg='#086e02')
        SumaPrice = tk.Label(SumaZakaz,
                            text=f"Ціна : {cost} грн.",
                            font=('Arial Black', 14),
                            bg='#086e02')
        def SumaExit():
            SumaZakaz.destroy()
        SumaOk = tk.Button(SumaZakaz,
                            text='OK',
                            font=('Arial Black', 14),
                            width=4,
                            height=1,
                            bg='#8cffa7',
                            command= SumaExit
                            )

        SumaText.place(x=30,y=10)
        SumaNum.place(x=10,y=50)
        SumaTime.place(x=10,y=85)
        SumaPrice.place(x=10,y=120)
        SumaOk.place(x=230,y=145)
        mycursor = mydb.cursor()
        billiard_room_statistics = """
        INSERT INTO main_info 
        (id,orderdate,ordertime,countHours,numberTable,revenue)
        VALUES ( %s,%s,%s ,%s,%s,%s)
        """

        main_infos = [('', f'{x.year}/{x.month}/{x.day}', f'{x.hour}:{x.minute}:{x.second}', f'{h}', f'{n+1}', f'{cost}' )]
        mycursor.executemany(billiard_room_statistics, main_infos)
        mydb.commit()

        def Virupai():
                ser.write(str(PortsOff[n]).encode())
                stan[n].configure(image=gray)
        threading.Timer(delay, Virupai).start()

Zakaz_Button = [1,2]
ButtonZakaz(0,Zakaz_Button,Vkladki,ChabgeStan)
ButtonZakaz(1,Zakaz_Button,Vkladki,ChabgeStan)
Zakaz_Num = [1,2]
NumTable(0,Zakaz_Num,Vkladki)
NumTable(1,Zakaz_Num,Vkladki)

Zakaz_Hour = [1,2,3]
HourZakaz(0,Zakaz_Hour,Vkladki,10,24)
HourZakaz(1,Zakaz_Hour,Vkladki,11,25)
HourZakaz(2,Zakaz_Hour,Vkladki,1,15)

#налаштування вкладки меню
Menu_Text = ['1','2','3']
M_Text(0,Menu_Text,Vkladki,16,'Вхід до панелі адміна')
M_Text(1,Menu_Text,Vkladki,12,'Логін:')
M_Text(2,Menu_Text,Vkladki,12,'Пароль:')
login = StringVar()
parol = StringVar()

M_Login = tk.Entry(
            Vkladki[3],
            width=15,
            font=('Arial Black', 12),
            textvariable=login

)
M_Parol = tk.Entry(
            Vkladki[3],
            width=15,
            font=('Arial Black', 12),
            show='*',
            textvariable=parol
)
fonLogin = ' '
fonParol = '  '
#Функція налаштування адмін панелі
def panel():
    if login.get() =='admin':
        if parol.get() == 'admin':
            AdminPanel = tk.Toplevel(Vkladki[3],bg='#086e02')
            AdminPanel.geometry('600x300')
            AdminPanel.resizable(False, False)
            AdminText = tk.Label(AdminPanel,
                                 text="Адмін панель",
                                 font=('Arial Black', 18),
                                 bg='#086e02'
                                 )
            Price_Text = tk.Label(AdminPanel,
                                  text=f"Вартість оренди за 1 год: {Price} грн.",
                                  font=('Arial Black', 14),
                                  bg='#086e02'
                                  )

            def Exit():
                AdminPanel.destroy()
                M_Login.insert('0',fonLogin)
                M_Parol.insert('0',fonParol)
            def Baze():
                webbrowser.open_new(r"http://localhost/phpmyadmin/index.php?route=/database/structure&server=1&db=billiard_room_statistics")
                print('work')
            Save = tk.Button(AdminPanel,
                             text="Вихід",
                             font=('Arial Black', 14),
                             bg='#fa2525',
                             command = Exit
                             )
            BazeData = tk.Button(AdminPanel,
                             text="Зайти в базу данних",
                             font=('Arial Black', 14),
                             bg='#8cffa7',
                             relief=RIDGE,
                             command = Baze
                             )
            Timer = [1, 2, 3]
            Timer[0] = tk.Label(
                AdminPanel,
                bg='#086e02',
                image=forTime,
            )

            clock = (datetime.now()).strftime('%H:%M:%S')
            Clocks = tk.Label(
                AdminPanel,
                text=clock,
                font=('Arial Black', 27),
                bg='#086e02',
            )

            def clock_update():
                while True:
                    Clocks['text'] = (datetime.now()).strftime('%H:%M:%S')
                    sleep(1)

            process = threading.Thread(target=clock_update)
            process.start()
            Timer[0].place(x=380, y=5)
            Clocks.place(x=397, y=25)
            AdminText.place(x=100, y=10)
            Price_Text.place(x=5,y=70)
            BazeData.place(x=50,y=150)
            Save.place(x=515, y=245)
        else :
            wronk = tk.Label(
                Vkladki[3],
                font=('Arial Black', 14),
                fg='red',
                text='Неправильний пароль!!!',
                bg='#f0ffff',
            )
            wronk.place(x=35,y=200)

M_Button = tk.Button(
            Vkladki[3],
            text='Зайти',
            font=('Arial Black', 14),
            width=15,
            height=1,
            bg='#8cffa7',
            command=panel
)
#Налаштування розміщення  елементів
window.resizable(False,False)
i=0
while i<=4:
    fon[i].pack()
    i +=1
#Вкладка головна

Timer[0].place(x=240,y=20)
Clocks.place(x=257,y=40)
table[0].place(x=20, y=50)
table[1].place(x=470, y=50)
table[2].place(x=20, y=300)
table[3].place(x=470, y=300)
table[4].place(x=20, y=550)
table[5].place(x=470, y=550)

text[0].place(x=100, y=15)
text[1].place(x=550, y=15)
text[2].place(x=100, y=265)
text[3].place(x=550, y=265)
text[4].place(x=100, y=515)
text[5].place(x=550, y=515)

stan[0].place(x=20, y=165)
stan[1].place(x=470, y=165)
stan[2].place(x=20, y=415)
stan[3].place(x=470, y=415)
stan[4].place(x=20, y=665)
stan[5].place(x=470, y=665)
'''
times[0].place(x=80, y=180)
times[1].place(x=530, y=180)
times[2].place(x=80, y=430)
times[3].place(x=530, y=430)
times[4].place(x=80, y=680)
times[5].place(x=530, y=680)
'''
res[0].place(x=172, y=175)
res[1].place(x=622, y=175)
res[2].place(x=172, y=425)
res[3].place(x=622, y=425)
res[4].place(x=172, y=675)
res[5].place(x=622, y=675)
#Вкладка заказ
orderI.place(x=100,y=50)
#Zakaz_Name[0].place(x=200, y=30)
Zakaz_Name[1].place(x=220, y=30)
'''
Zakaz_Other_Text[0].place(x=160, y=100)
Zakaz_Other_Text[1].place(x=160, y=150)
'''
Zakaz_Other_Text[2].place(x=160, y=100)
Zakaz_Other_Text[3].place(x=160, y=150)

#Zakaz_Button[0].place(x=200, y=200)
Zakaz_Button[1].place(x=200, y=200)

#Zakaz_Num[0].place(x=320, y=100)
Zakaz_Num[1].place(x=322, y=100)

#Zakaz_Hour[0].place(x=193, y=150)
#Zakaz_Hour[1].place(x=280, y=150)
Zakaz_Hour[2].place(x=350, y=150)

#Вкладка меню
adminI.place(x=400,y=150)
Menu_Text[0].place(x=50,y=10)
Menu_Text[1].place(x=15,y=65)
Menu_Text[2].place(x=15,y=100)

M_Login.place(x=95,y=65)
M_Parol.place(x=95,y=100)
M_Button.place(x=85,y=150)
window.mainloop()