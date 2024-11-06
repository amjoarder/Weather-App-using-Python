from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=65af65c603d3b47af69c56b20436f1ef").json()

    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pre_label1.config(text=data["main"]["pressure"])








win=Tk()
win.title("Joarder")
win.config(bg="blue")
win.geometry("500x570")



name_label = Label( win,text="Weather App", font=("Time New Roman", 30, "bold") )

name_label.place(x=25, y=50, height=50,width=450)



list_name = ["Dhaka", "Khulna", "Rajshahi", "Chittagong", "Sylhet"]
city_name=StringVar()
com=ttk.Combobox(win,text="Weather App", values=list_name, font=("Time New Roman", 20, "bold"), textvariable=city_name )

com.place(x=25, y=120, height=50, width=450)




w_label = Label( win,text="Weather Climate", font=("Time New Roman", 20) )
w_label.place(x=25, y=260, height=50,width=210)
w_label1 = Label( win,text="t", font=("Time New Roman", 20) )
w_label1.place(x=250, y=260, height=50,width=210)


wb_label = Label( win,text="Weather Description", font=("Time New Roman", 17) )
wb_label.place(x=25, y=330, height=50,width=210)
wb_label1 = Label( win,text="t", font=("Time New Roman", 17) )
wb_label1.place(x=250, y=330, height=50,width=210)



temp_label = Label( win,text="Temperature", font=("Time New Roman", 17) )
temp_label.place(x=25, y=400, height=50,width=210)
temp_label1 = Label( win,text="T", font=("Time New Roman", 17) )
temp_label1.place(x=250, y=400, height=50,width=210)


pre_label = Label( win,text="Pressure", font=("Time New Roman", 17) )
pre_label.place(x=25, y=470, height=50,width=210)
pre_label1 = Label( win,text="P", font=("Time New Roman", 17) )
pre_label1.place(x=250, y=470, height=50,width=210)



done_button = Button( win,text="Done", font=("Time New Roman", 30, "bold"), command=data_get )

done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()