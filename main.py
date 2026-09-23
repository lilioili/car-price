import tkinter as tk
from PIL import Image,ImageTk
import pandas as pd
import numpy as np
import openpyxl
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

######################################################

def price():
  accident_count=int(E_accident_count.get())
  engine_l=float(E_engine_l.get())
  mileage_km=int(E_mileage_km.get())
  technical_score=float(E_technical_score.get())
  year=int(E_year.get())

  answer=model.predict(np.array([[year,mileage_km,engine_l,accident_count,technical_score]]))[0][0]
  l_answer = tk.Label(screen,text=f"{round(answer,2)}$+-1340",bg="#89CCFF",font=("Arial",12))
  l_answer.place(x=250,y=510,anchor="center")

###############################################################

data = pd.read_excel("project1_used_car_data.xlsx")

f = data[['Year', 'Mileage_km', 'Engine_L', 'Accident_Count', 'Technical_Score']]
l = data[['Price_USD']]

f_train,f_test,l_train,l_test = train_test_split(f,l,test_size=0.25)

model = LinearRegression()
model.fit(X=f_train,y=l_train)

#################################################################

screen = tk.Tk()
screen.geometry("500x650")
screen.title("Used car dataset")
screen.config(bg="#89CCFF")
screen.iconbitmap("cars.ico")

#################################################################

l1 = tk.Label(screen,text="                 Used cars dataset                ",bg="#030784",fg="#FFFFFF",font=("Arial",22))
l1.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("car_image.png").resize((150,100)))
l2 = tk.Label(screen,image=img,bg="#89CCFF")
l2.place(x=250,y=230,anchor="center")

L_year = tk.Label(screen,text="write cars year",bg="#89CCFF",font=("Arial",12))
L_year.place(x=60,y=135)

L_mileage_km = tk.Label(screen,text="write cars mileage km",bg="#89CCFF",font=("Arial",12))
L_mileage_km.place(x=310,y=135)

L_engine_l = tk.Label(screen,text="write cars engine litr",bg="#89CCFF",font=("Arial",12))
L_engine_l.place(x=40,y=345)

L_accident_count = tk.Label(screen,text="write cars accident",bg="#89CCFF",font=("Arial",12))
L_accident_count.place(x=320,y=345)

L_technical_score = tk.Label(screen,text="write cars technical score",bg="#89CCFF",font=("Arial",12))
L_technical_score.place(x=250,y=445,anchor="center")

L_MAE = tk.Label(screen,text="MAE=1082+-",font=("Arial",12),bg="#89CCFF")
L_MAE.place(x=20,y=550)

L_MSE = tk.Label(screen,text="MSE=179675+-",font=("Arial",12),bg="#89CCFF")
L_MSE.place(x=350,y=550)

L_RMSE = tk.Label(screen,text="RMSE=1340+-",font=("Arial",12),bg="#89CCFF")
L_RMSE.place(x=250,y=550,anchor="center")
###################################################################

E_year = tk.Entry(screen)
E_year.place(x=50,y=110,width=125,height=25)

E_mileage_km = tk.Entry(screen)
E_mileage_km.place(x=320,y=110,width=125,height=25)

E_engine_l = tk.Entry(screen)
E_engine_l.place(x=50,y=320,width=125,height=25)

E_accident_count = tk.Entry(screen)
E_accident_count.place(x=320,y=320,width=125,height=25)

E_technical_score = tk.Entry(screen)
E_technical_score.place(x=250,y=420,anchor="center",width=125,height=25)

###################################################################

B_price_USD = tk.Button(screen,text="price",bg="#00A500",font=("Arial",12),command=price)
B_price_USD.place(x=250,y=600,anchor="center",width=100)











screen.mainloop()