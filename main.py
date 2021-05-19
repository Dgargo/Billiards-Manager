
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

from Golovna import Stolic,Fon,Stolic_time,Stolic_Text,Reset
from Bron import Bronik,BronTime,BronPlace,BronNum,BronNumPlace,BronMas,BronPlaceTime
from Zakaz import  Button_Z,NameZakaz ,Number_Tap_text
#Налоштування головного вікна
window = Tk()
window.title('Billiards manager V1')
window.geometry('800x800')
window.configure(bg='#f7fffd')
#Налаштування вкладок
nb = ttk.Notebook(window,height=800)
nb.pack(pady=10,fill='both')
Vkladki =['Golovna','Zakaz','Bronik','Menu','Quest']
i= 0
while i<=4:
    Vkladki[i] = ttk.Frame(window)
    i +=1

nb.add(Vkladki[0],text='Головна')
nb.add(Vkladki[1],text='Новий заказ')
nb.add(Vkladki[2],text='Заброньовані')
nb.add(Vkladki[3],text='Меню')
nb.add(Vkladki[4],text='?')

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
#Вибір номеру стола
Zakaz_NumB_Check = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width=1,
)
Zakaz_NumB_Check['values'] =tuple(range(1,7))

Zakaz_NumH_Check = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width=1,
)
Zakaz_NumH_Check['values'] =tuple(range(1,7))
#Налаштування тексту
Zakaz_Time =tk.Label(
        Vkladki[1],
        text='Час, з:          до:     ',
        font=('Consolas', 14),
        fg='black',
        bg='#f7fffd',
)
#
Zakaz_Time_fHour = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width=2,
    )
Zakaz_Time_fHour['values'] = tuple(range(10,24))
#
Zakaz_Time_fMin = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width =2,
)
Zakaz_Time_fMin['values'] = tuple(range(0, 60))
#
Zakaz_Time_tHour = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width =2,
)
Zakaz_Time_tHour['values'] = tuple(range(11,25))

Zakaz_Time_tMin = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width =2,
)
Zakaz_Time_tMin['values'] = tuple(range(0, 60))
Zakaz_Button = ['1','2']
Button_Z(0,Zakaz_Button,Vkladki)

Zakaz_TextH = tk.Label(
    Vkladki[1],
    text='Кількість     год      хв',
    font=('Consolas', 14),
    bg='#f7fffd',
)

Zakaz_TimeH_Hour = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width=2,
    )
Zakaz_TimeH_Hour['values'] = tuple(range(0,13))

Zakaz_TimeH_Min =ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width =2,
)
Zakaz_TimeH_Min['values']=  (0,15,30,45)
#Вкладка Заброньвані
Bron1 = []
BronMas(Bron1)
Bronik(0,Bron1,Vkladki)
Bron2 = []
BronMas(Bron2)
Bronik(0,Bron2,Vkladki)
Bron3 = []
BronMas(Bron3)
Bronik(0,Bron3,Vkladki)
Bron4 = []
BronMas(Bron4)
Bronik(0,Bron4,Vkladki)
Bron5 = []
BronMas(Bron5)
Bronik(0,Bron5,Vkladki)
Bron6 = []
BronMas(Bron6)
Bronik(0,Bron6,Vkladki)
Bron7 =[]
BronMas(Bron7)
BronTime(0,Bron7,Vkladki)
Number = [1,2,3,4,5,6]
BronNum(0,Number,Vkladki)

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

text[0].place(x=100, y=20)
text[1].place(x=550, y=20)
text[2].place(x=100, y=270)
text[3].place(x=550, y=270)
text[4].place(x=100, y=520)
text[5].place(x=550, y=520)

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
Zakaz_NumB_Check.place(x=155, y=75)
Zakaz_Time.place(x=30, y=130)
Zakaz_Time_fHour.place(x=105, y=130)
Zakaz_Time_fMin.place(x=151, y=130)
Zakaz_Time_tHour.place(x=233, y=130)
Zakaz_Time_tMin.place(x=280, y=130)
Zakaz_Button[0].place(x=30, y=180)

Zakaz_Text[1].place(x=50, y=250)
Zakaz_Num_Tap[1].place(x=30, y=300)
Zakaz_NumH_Check.place(x=155, y=300)
Zakaz_TextH.place(x=30,y=350)
Zakaz_TimeH_Hour.place(x=125,y=350)
Zakaz_TimeH_Min.place(x=210,y=350)
Zakaz_Button[1].place(x=30, y=415)

BronPlace(0,Bron1,60,55)
BronPlace(0,Bron2,60,100)
BronPlace(0,Bron3,60,145)
BronPlace(0,Bron4,60,190)
BronPlace(0,Bron5,60,235)
BronPlace(0,Bron6,60,280)
BronNumPlace(0,Number,10,53)
BronPlaceTime(0,Bron7,60,10)

window.mainloop()