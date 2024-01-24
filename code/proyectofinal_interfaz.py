# Truzz Blogg | Python + Tkinter | How to create a GUI
# How to create a registration form using Python + Tkinter

# Let's import tkinter 
from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
#import tkinter as tk
 
# Manipulate data from registration fields 
def usar_data():
  gre_info = float(gre.get())
  toefl_info = float(toefl.get())
  cgpa_info = float(cgpa.get())
 
  #cargamos el dataset jamboree
  ruta = r'C:/Users/matia/OneDrive/Escritorio/Curso_The_Corner/jamboree/jamboree_dataset.csv'
  df = pd.read_csv(ruta) 

  #cambiamos el nombre de las columnas
  df = df.rename(columns={'Serial No.':'SERIALNUMBER', 'GRE Score':'GRE', 'TOEFL Score':'TOEFL', 'University Rating': 'UNIVERSITYRATING', 'Research':'RESEARCH', 'Chance of Admit ':'CHANCEOFADMIT'})

  #asignar las variables x e y:
  y = df['CHANCEOFADMIT']
  x = df.drop(['CHANCEOFADMIT', 'SERIALNUMBER'], axis=1)

  # dividir en conjunto de entrenamiento y prueba:
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1, shuffle=True)

  regresion_lineal = LinearRegression()
  regresion_lineal.fit(x_train, y_train)

  y_pred = regresion_lineal.predict(x_test)

  gre_valor = gre_info
  toefl_valor = toefl_info
  cgpa_valor = cgpa_info

  prueba = ({'GRE': [gre_valor], 'TOEFL': [toefl_valor], 'UNIVERSITYRATING': [universidadrating_entry.get()], 'SOP': [sop_entry.get()], 'LOR ': [lor_entry.get()], 'CGPA': [cgpa_valor], 'RESEARCH': [research_entry.get()]})
  df_prueba = pd.DataFrame(prueba, index=[0])

  predicted_values = regresion_lineal.predict(df_prueba)
  #print("\nposibilidad de ingresar a la universidad solicitada: ",predicted_values)
  if (gre_valor.is_integer() == True) and (toefl_valor.is_integer() == True) and (0<=cgpa_valor<=10): 
    resultado.set(round(predicted_values[0], 2))
  else:
    resultado.set("Error, revise los datos ingresados")
 
#creamos la etiqueta que arroja el valor predict

# Create new instance - Class Tk()  
mywindow = Tk()
mywindow.geometry("650x650")
mywindow.title("Simulador acceso a la universidad")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "Simulador accesso a la universidad", font = ("Cambria", 14), fg = "black", width = "500", height = "2")
main_title.pack()

# Define Label Fields 
gre_label = Label(text = "Puntaje obtenido GRE", bg = "#213141", foreground='white')
gre_label.place(x = 22, y = 70)
toefl_label = Label(text = "Puntaje obtenido TOEFL", bg = "#213141", foreground='white')
toefl_label.place(x = 22, y = 130)
universidadrating_label = Label(text = "Puntuación universidad solicitada (1 - 4)", bg = "#213141", foreground='white')
universidadrating_label.place(x = 22, y = 190)
sop_label = Label(text = "Puntaje obtenido SOP", bg = "#213141", foreground='white')
sop_label.place(x = 22, y = 250)
lor_label = Label(text = "Puntaje obtenido LOR", bg = "#213141", foreground='white')
lor_label.place(x = 22, y = 310)
cgpa_label = Label(text = "Puntaje obtenido CGPA", bg = "#213141", foreground='white')
cgpa_label.place(x = 22, y = 370)
research_label = Label(text = "Research (SI = 1/NO = 0)", bg = "#213141", foreground='white')
research_label.place(x = 22, y = 430)
resultado_label = Label(text = "Probabilidad de ingresar: ", bg = "#213141", foreground='white')
resultado_label.place(x = 22, y = 560)

# Get and store data from users 
gre = StringVar()
toefl = StringVar()
cgpa = StringVar()
resultado = StringVar()
 
gre_entry = Entry(textvariable = gre, width = "40")
toefl_entry = Entry(textvariable = toefl, width = "40")
universidadrating_entry = ttk.Combobox(state="readonly", values=[1, 2, 3, 4], width="40")
sop_entry = ttk.Combobox(state="readonly", values=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5], width="40")
lor_entry = ttk.Combobox(state="readonly", values=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5], width="40")
cgpa_entry = Entry(textvariable = cgpa, width = "40")
research_entry = ttk.Combobox(state="readonly", values=[0, 1], width="40")
resultado_entry = Entry(textvariable = resultado, width = "40")
 
gre_entry.place(x = 22, y = 100)
toefl_entry.place(x = 22, y = 160)
universidadrating_entry.place(x = 22, y = 220)
sop_entry.place(x = 22, y = 280)
lor_entry.place(x = 22, y = 340)
cgpa_entry.place(x = 22, y = 400)
research_entry.place(x = 22, y = 460)
resultado_entry.place(x = 22, y = 590)
 
# Submit Button
submit_btn = Button(mywindow,text = "Calcular probabilidad de ingresar a la universidad solicitada", width = "60", height = "2", command = usar_data, bg = "white")
submit_btn.place(x = 22, y = 500)

mywindow.mainloop()


