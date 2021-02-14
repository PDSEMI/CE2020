from tkinter import *
from tkinter import ttk, messagebox
import json

########## MAIN GUI ##########
H = "500"
W = "700"
title = "Celestial Equation 2020"
GUI = Tk()
GUI.geometry("{}x{}".format(W,H))
GUI.title(title)

FONT1 = ('Ansana New', 25)
FONT2 = ('Ansana New', 18)

########## Notebook(TAB) ##########
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T1_title = "Satellite Calculation"
T2 = Frame(Tab)
T2_title = "Satellite data"
T3 = Frame(Tab)
T3_title = "Alt-Alz visualization"

Tab.pack(fill=BOTH, expand = 1)

Tab.add(T1,text=T1_title)
Tab.add(T2,text=T2_title)
Tab.add(T3,text=T3_title)

########## T1 (Satellite Calculation) ##########

########## T2 (Satellite Data) ##########
header = ['CATALOG NUMBER', 'INTERNATIONAL DESIGNATOR', 'SATELLITE NAME']
hdsize = [200,200,200]

DataTable = ttk.Treeview(T2, column = header, show='headings', height=15)
DataTable.place(x=50,y=20)

for h,s in zip(header,hdsize):
    DataTable.heading(h,text=h)
    DataTable.column(h,width=s)

########## T3 (Alt-Alz visualization) ##########
L1 = ttk.Label(T3, text = "Visualization test", font=FONT1)
L1.grid(row=0,column=0)

v_alz = StringVar()
v_alt = StringVar()

########## Function Definintion ##########
def writeToJOSON(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

def Visualize():
    alt = v_alt.get()
    alz = v_alz.get()
    data = {}
    path = './'
    fileName = 'data'
    if len(alt) > 0 and len(alz) > 0:
        data['Altitude'] = alt
        data['Alzimuth'] = alz
        writeToJOSON(path, fileName, data)
        v_alt.set('')
        v_alz.set('')
        E1.focus()
    else:
        messagebox.showinfo('No data is inserted', 'vocab and meaning must be valid')



L2 = ttk.Label(T3, text = "Alzimuth", font = FONT2,anchor = 'w')
L2.grid(sticky = "W",row=1,column=0)
E1 = ttk.Entry(T3, textvariable = v_alz, width = 30)
E1.grid(row=1,column=1)
L3 = ttk.Label(T3, text = "Altitude", font =FONT2, anchor='w')
L3.grid(sticky = "W", row=2,column=0)
E2 = ttk.Entry(T3, textvariable = v_alt, width = 30)
E2.grid(row=2,column=1)

B1 = ttk.Button(T3, text = "Visualize", command = Visualize)
B1.grid(sticky = "E",row=3,column = 1)

GUI.mainloop()
