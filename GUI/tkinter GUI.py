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
TITLE = ("Times New Roman",28,'italic')
HD1 = ("Times New Roman",20)
HD2 = ("Times New Roman",16,)
NORMAL = ("TImes New Roman", 16)

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
########## VARIABLE ##########
v_catalog = StringVar()
v_location_arcmin = StringVar()
v_location_arcsec = StringVar()
v_location_miliarcsec = StringVar()
v_dd =StringVar()
v_mm = StringVar()
v_yyyy = StringVar()


Title1 = Label(T1, text = 'Satellite Data', font=TITLE).grid(row=0,column=0)
blank1 = Label(T1).grid(row=1,column=0)
HD1 = Label(T1, text = 'Catalog number : ',font = HD2).grid(row=2,column=0,sticky = 'E')
E1_1 = Entry(T1, textvariable = v_catalog, width = 50).grid(row=2,column=1)
B1_1 = Button(T1, text = 'search').grid(row=2, column = 2, sticky ='E')

L1_1 = Label(T1, text = 'Name :', font = NORMAL).grid(row=3,column = 0,sticky = 'E')
L1_2 = Label(T1, text = 'Designator :', font = NORMAL).grid(row=4,column = 0,sticky = 'E')
blank2 = Label(T1).grid(row=5,column=0)

Title2 = Label(T1, text = 'Observer Data', font=TITLE).grid(row=6,column=0)

L1_3 = Label(T1, text = 'Location :', font = NORMAL).grid(row=7,column = 0,sticky = 'E')
E1_2 = Entry(T1, textvariable = v_location_arcmin, width = 5).place(x=250,y=235)
L1_4 = Label(T1, text = chr(176),font=NORMAL).place(x=280,y=230)
E1_3 = Entry(T1, textvariable = v_location_arcsec, width = 5).place(x=300,y=235)
L1_5 = Label(T1, text = '\'',font=NORMAL).place(x=330,y=230)
E1_4 = Entry(T1, textvariable = v_location_miliarcsec, width = 5).place(x=350,y=235)
L1_6 = Label(T1, text = '\'\'',font=NORMAL).place(x=380,y=230)

L1_7 = Label(T1, text = 'Date :', font = NORMAL).grid(row=8,column = 0,sticky = 'E')
E1_5 = Entry(T1, textvariable = v_dd, width = 5).place(x=250,y=265)
L1_8 = Label(T1, text = '--',font=NORMAL).place(x=280,y=260)
E1_6 = Entry(T1, textvariable = v_mm, width = 5).place(x=300,y=265)
L1_9 = Label(T1, text = '--',font=NORMAL).place(x=330,y=260)
E1_7= Entry(T1, textvariable = v_yyyy, width = 10).place(x=350,y=265)
blank3 = Label(T1).grid(row=9,column=0)

B1_2 = Button(T1, text = 'Calculate', font = NORMAL).grid(row=11,column=2,sticky='E')
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
