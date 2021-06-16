
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import serial
from datetime import datetime, timedelta
from Golovna import Stolic,Fon,Stolic_time,Stolic_Text,Reset
from Zakaz import  NameZakaz ,Number_Tap_text
from menu import M_Text
import mysql.connector
from mysql.connector import connect, Error,cursor
from threading import Thread
from time import sleep
'''
ser = serial.Serial('COM4', 9600)
'''
clockHot = [1,2,3,4,5,6]
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
#Налаштування  стилю фону вкладок
fon = [1,2,3,4,5]
Fon(0,fon,Vkladki)

#Налаштування стилю столів
table = [1, 2, 3, 4, 5, 6]
Stolic(0,table,Vkladki,img)

#Налаштування стилю номера стола
text = [1, 2, 3, 4, 5, 6]
Stolic_Text(0,text,Vkladki)

#Налаштування стилю стану стола
stan = [1, 2, 3, 4, 5, 6]
Stolic(0,stan,Vkladki,gray)


#Налаштування стилю часу стола
time = [1, 2, 3, 4, 5, 6]
Stolic_time(0,time,Vkladki)

#
res = [1, 2, 3, 4, 5, 6]
Reset(0,res,Vkladki,reset)

#Налаштування вкладки Заказ
Zakaz_Text = ['1','2']
NameZakaz(0,Zakaz_Text,Vkladki,"Забронювати стіл :")
NameZakaz(1,Zakaz_Text,Vkladki,'Експресс заказ:')
Zakaz_Num_Tap =['1','2']
Number_Tap_text(0,Zakaz_Num_Tap,Vkladki)
NumZ = IntVar()
NumHotZ = IntVar()
FHourZ = IntVar()
THourZ = IntVar()
#Вибір номеру стола
Zakaz_NumB_Check = ttk.Combobox(
    Vkladki[1],
    font=('Arial Black', 12),
    width=1,
    textvariable=NumZ
)

Zakaz_NumB_Check['values'] =tuple(range(1,7))

#Налаштування тексту
Zakaz_Time =tk.Label(
        Vkladki[1],
        text='Час, з:             до:     ',
        font=('Arial Black', 12),
        fg='black',
        bg='#086e02',
)

Zakaz_Time_fHour = ttk.Combobox(
    Vkladki[1],
    font=('Arial Black', 12),
    width=2,
    textvariable=FHourZ
    )
Zakaz_Time_fHour['values'] = tuple(range(10,24))

Zakaz_Time_tHour = ttk.Combobox(
    Vkladki[1],
    font=('Arial Black', 12),
    width =2,
    textvariable=THourZ
)
Zakaz_Time_tHour['values'] = tuple(range(11,25))
def Button_Z(i,Zakaz_B,Vkladki):
    Zakaz_B[i] = tk.Button(
        Vkladki[1],
        text='Відправити',
        font=('Arial Black', 14),
        width=15,
        height=1,
        bg='#8cffa7',
        relief =RIDGE)


Zakaz_Button = ['1','2']
Button_Z(0,Zakaz_Button,Vkladki)
Button_Z(1,Zakaz_Button,Vkladki)
'''
def sendZakaz():
    count =  1
    main_infos = [count,NumZ.get]
    mycursor.executemany(billiard_room_statistics, main_infos)
    mydb.commit()
'''


Zakaz_NumH_Check = ttk.Combobox(
    Vkladki[1],
    font=('Arial Black', 12),
    width=1,
    values = list(range(1,7))
)
Zakaz_NumH_Check.set(10)
Zakaz_TextH = tk.Label(
    Vkladki[1],
    text='Кількість:           год.',
    font=('Arial Black', 12),
    bg='#086e02',
)

Zakaz_TimeH_Hour = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 12),
    width=2,
    values = list(range(0,13))

    )
Zakaz_TimeH_Hour.set(0)
def HourHot(i):
     if clockHot[i] < datetime.now():
         sleep(60)
         stan[i].configure(image=red)
         print('work')

     else :
         '''ser.write(int((NumOff), 'UTF-8'))'''
         stan[i].configure(image=gray)



def sendHot():
    h = float(Zakaz_TimeH_Hour.get())
    h = int(h)
    i = float(Zakaz_NumH_Check.get())
    i = int(i)
    '''
    clockHot[i] = datetime.now() + timedelta(hours = h)
    Num = (NumHotZ.get() *10 )
    NumOnn = int(Num + 1)
    NumOff = int(Num - 1)
    ser.write(bytes(NumOnn, 'UTF-8'))
    '''
    stan[i].configure(image=red)



Zakaz_Button[1].configure(command = sendHot())

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
def static(i,stat,AdminPanel,suma,kilZam,KilHour):
    stat[i] = tk.Label(AdminPanel,
                           text=f'Сума за період: {suma}\n'
                                  f'Кількість замовлень: {kilZam}\n'
                                f'Кількість годин: {KilHour}\n',
                           font = ('Arial Black', 12),
                           bg = '#616c75',
                           fg = 'white',
                           width=22,
                           height=5,
                           justify=LEFT)

def stat_Text(i,statText,AdminPanel,text):
    statText[i] = tk.Label(AdminPanel,
                       text =f"{text}",
                       font=('Arial Black', 14),
                       bg='#616c75',
                       fg='white',
                       width=18,
                       height=1,
                           )
suma = 100
def panel():
    if login.get() =='admin':
        if parol.get() == 'admin':
            AdminPanel = tk.Toplevel(Vkladki[3],bg='#086e02')
            AdminPanel.geometry('820x500')
            AdminPanel.resizable(False, False)
            AdminText = tk.Label(AdminPanel,
                                 text="Адмін панель",
                                 font=('Arial Black', 18),
                                 bg='#086e02'
                                 )
            Price_Text = tk.Label(AdminPanel,
                                  text="Вартість оренди за 1 год:",
                                  font=('Arial Black', 12),
                                  bg='#086e02'
                                  )
            Price = tk.Entry(AdminPanel,
                             width =10,
                             font=('Arial Black', 12)
                                )
            Save = tk.Button(AdminPanel,
                             text="Зберегти",
                             font=('Arial Black', 12),
                             bg='#8cffa7'
                             )
            Suma_day = tk.Label(AdminPanel,
                                text =f'В касі мають бути: {suma} грн.',
                                font=('Arial Black', 12),
                                bg='#086e02'
                                )
            stat = ['1','7','30']
            static(0,stat,AdminPanel,100,2,3)
            static(1, stat, AdminPanel, 1000, 10, 50)
            static(2, stat, AdminPanel, 5000, 25, 150)
            stat_Period = ['1','7','30']
            stat_Text(0,stat_Period,AdminPanel,'Вчора')
            stat_Text(1, stat_Period, AdminPanel, '7 Днів')
            stat_Text(2, stat_Period, AdminPanel, '30 Днів')
            stat[0].place(x = 20 ,y=180)
            stat[1].place(x = 280,y=180)
            stat[2].place(x = 550,y=180)
            stat_Period[0].place(x=24 , y=142)
            stat_Period[1].place(x=284, y=142)
            stat_Period[2].place(x=554, y=142)
            AdminText.place(x=100, y=10)
            Price_Text.place(x=10,y=70)
            Price.place(x=270, y=70)
            Suma_day.place(x=10,y=450)
            Save.place(x=700, y=450)
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

table[0].place(x=20, y=50)
table[1].place(x=470, y=50)
table[2].place(x=20, y=300)
table[3].place(x=470, y=300)
table[4].place(x=20, y=550)
table[5].place(x=470, y=550)

text[0].place(x=100, y=19)
text[1].place(x=550, y=19)
text[2].place(x=100, y=269)
text[3].place(x=550, y=269)
text[4].place(x=100, y=519)
text[5].place(x=550, y=519)

stan[0].place(x=20, y=165)
stan[1].place(x=470, y=165)
stan[2].place(x=20, y=415)
stan[3].place(x=470, y=415)
stan[4].place(x=20, y=665)
stan[5].place(x=470, y=665)

time[0].place(x=80, y=180)
time[1].place(x=530, y=180)
time[2].place(x=80, y=430)
time[3].place(x=530, y=430)
time[4].place(x=80, y=680)
time[5].place(x=530, y=680)

res[0].place(x=172, y=175)
res[1].place(x=622, y=175)
res[2].place(x=172, y=425)
res[3].place(x=622, y=425)
res[4].place(x=172, y=675)
res[5].place(x=622, y=675)

Zakaz_Text[0].place(x=50,y=15)
Zakaz_Num_Tap[0].place(x=30, y=75)
Zakaz_NumB_Check.place(x=160, y=75)
Zakaz_Time.place(x=30, y=130)
Zakaz_Time_fHour.place(x=100, y=130)
Zakaz_Time_tHour.place(x=193, y=130)
Zakaz_Button[0].place(x=30, y=180)
Zakaz_Text[1].place(x=50, y=250)
Zakaz_Num_Tap[1].place(x=30, y=300)
Zakaz_NumH_Check.place(x=160, y=300)
Zakaz_TextH.place(x=30,y=355)
Zakaz_TimeH_Hour.place(x=125,y=355)
Zakaz_Button[1].place(x=30, y=415)


Menu_Text[0].place(x=50,y=10)
Menu_Text[1].place(x=15,y=65)
Menu_Text[2].place(x=15,y=100)
M_Login.place(x=95,y=65)
M_Parol.place(x=95,y=100)
M_Button.place(x=85,y=150)



window.mainloop()