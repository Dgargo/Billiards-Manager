
import tkinter as tk

#Налаштування  стилю фону вкладок
def Fon(i,fon,Vkladki):
    while i <= 4:
        fon[i] = tk.Label(
            Vkladki[i],
            bg='#086e02',
            height=1000,
            width=800,
        )
        i += 1

#функція для імпортування картинки стола і стану стола
def Stolic(i,table,Vkladki,img):
        table[i] = tk.Label(
            Vkladki[0],
            bg = '#086e02',
            image=img
        )

#Налаштування стилю номера стола
def Stolic_Text(i,text,Vkladki):
    while i <= 5:
        text[i] = tk.Label(
            Vkladki[0],
            text=f'№{text[i]}',
            font=('Arial Black', 16),
            fg='black',
            bg='#086e02',
        )
        i += 1

#Налаштування стилю часу стола
def Stolic_time(i,time,Vkladki):
    time[i] = tk.Label(
        Vkladki[0],
        text='00:00:00',
        font=('Arial Black', 12),
        bg='#086e02',
            )

#Налаштування стилю кнопки скидання
def ResetButton(i,res,Vkladki,img,func):
        res[i]=tk.Button(
            Vkladki[0],
            bg = '#e82528',
            image=img,
            command = func

        )


#Налаштування годинника
def Timer_Menu(i,Name,Vkladki,img):
    Name[i] = tk.Label(
        Vkladki[0],
        bg='#086e02',
        image=img,
         )

#Налаштування кнопки скидання
def Drop(i,stan,gray,ser,Vkladki):
    SurePanal = tk.Toplevel(Vkladki[0], bg='#086e02')
    SurePanal.geometry('400x150')
    SurePanal.resizable(False, False)
    num = i +1
    def YesSure():
        stan[i].configure(image=gray)
        ser.write(str((i + 1) * 10).encode())
        SurePanal.destroy()
    def NoSure():
        SurePanal.destroy()
    SureText = tk.Label(SurePanal,
                        text=f"Відключити стіл №{num} ?",
                        font=('Arial Black', 20),
                        bg='#086e02')
    SureYes = tk.Button(SurePanal,
                        text='ТАК',
                        font=('Arial Black', 20),
                        width=5,
                        height=1,
                        bg='#8cffa7',
                        command=YesSure
                        )
    SureNo = tk.Button(SurePanal,
                        text='НІ',
                        font=('Arial Black', 20),
                        width=5,
                        height=1,
                        bg='#fa2525',
                        command=NoSure
                        )
    SureText.place(x=35,y=10)
    SureYes.place(x=75,y=60)
    SureNo.place(x=225,y=60)



