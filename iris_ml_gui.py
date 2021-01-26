from tkinter import *
import numpy as np
import pickle
from PIL import ImageTk, Image
model = pickle.load(open('IRIS.pkl', 'rb'))

root=Tk()
root.geometry("700x500")
root.title("Iris Species Predictor")
root_color="gray50"
root.configure(bg=root_color)
fg_color="white"
heading=Label(root, text="Iris Species Predictor",bg=root_color,fg="lawn green",font="calibri 25 bold").place(x=220,y=10)
sepal_lenght=Label(root, text="Sepal length", bg=root_color,fg=fg_color,font="calibri 12 bold").place(x=40,y=97)
sepal_lenght_entry=Entry(root)
sepal_lenght_entry.place(x=140, y=100)
sepal_width=Label(root, text="Sepal width", bg=root_color,fg=fg_color,font="calibri 12 bold").place(x=40,y=177)
sepal_width_entry=Entry(root)
sepal_width_entry.place(x=140, y=180)

petal_lenght=Label(root, text="Petal length", bg=root_color,fg=fg_color,font="calibri 12 bold").place(x=340,y=97)
petal_lenght_entry=Entry(root)
petal_lenght_entry.place(x=440, y=100)
petal_width=Label(root, text="Petal width", bg=root_color,fg=fg_color,font="calibri 12 bold").place(x=340,y=177)
petal_width_entry=Entry(root)
petal_width_entry.place(x=440, y=180)
def spec():
    species=Label(root, text="Species:" ,bg=root_color,fg=fg_color,font="calibri 25 bold").place(x=150, y=330)
    sl=float(sepal_lenght_entry.get())
    sw=float(sepal_width_entry.get())
    pl=float(petal_lenght_entry.get())
    pw=float(petal_width_entry.get())
    arr=np.array([[sl,sw,pl,pw]])
    prediction=model.predict(arr)
    print(prediction)

    if prediction==0:
        print("Iris-setosa")
        pred = Label(root, text="Iris-setosa       ", bg=root_color, fg=fg_color, font="calibri 25 bold").place(x=270, y=330)
    if prediction==1:
        print("Iris-versicolor")
        pred = Label(root, text="Iris-versicolor  ", bg=root_color, fg=fg_color, font="calibri 25 bold").place(x=270, y=330)
    if prediction==2:
        print("Iris-virginica")
        pred = Label(root, text="Iris-virginica    ", bg=root_color, fg=fg_color, font="calibri 25 bold").place(x=270, y=330)

submit_btn=Button(root, text="Submit", width=15, command=lambda : spec()).place(x=290, y=250)
mainloop()
