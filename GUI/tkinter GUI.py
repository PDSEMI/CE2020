from tkinter import *
from tkinter import ttk, messagebox
import json
import search
import calculation as cal
########## MAIN GUI ##########
H = "800"
W = "800"
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
########## CONSTANT ##########



########## VARIABLE ##########
v_catalog = StringVar()
v_sat_name = StringVar()
v_sat_designator = StringVar()
v_latitude_arcmin = StringVar()
v_latitude_arcsec = StringVar()
v_latitude_miliarcsec = StringVar()
v_longitude_arcmin = StringVar()
v_longitude_arcsec = StringVar()
v_longitude_miliarcsec = StringVar()
v_dd =StringVar()
v_mm = StringVar()
v_yyyy = StringVar()
v_hr = StringVar()
v_min = StringVar()
v_sec = StringVar()
v_UTC_hr = StringVar()
v_UTC_min = StringVar()
v_UTC_sec = StringVar()
v_RA = StringVar()
v_dec = StringVar()
v_timezone = StringVar()
########## FUNCTION #########
def SearchSat():
    path = 'E:\FORUM\Project\CE2020\SatelliteData.xlsx'
    ID = v_catalog.get()
    result = search.satSearch(ID, path)
    v_sat_name.set(result.get('Name'))
    v_sat_designator.set(result.get('Designator'))
    Epoch = result.get('Epoch')
    Incl = result.get('Inclination')
    RAAN = result.get('RAAN')
    Eccentricity = result.get('Eccentricity')
    Perigee = result.get('Perigee')
    Anomaly = result.get('Anomaly')
    Motion = result.get('Motion')
    global Kepler_element 
    Kepler_element = [Epoch, Incl, RAAN, Eccentricity, Perigee, Anomaly, Motion]
    
def SetEpoch():
    yyyy = int(v_yyyy.get())
    mm = int(v_mm.get())
    dd = int(v_dd.get())
    hr = int(v_UTC_hr.get())
    minute = int(v_UTC_min.get())
    sec = int(v_UTC_sec.get())
    time = cal.fracTime(hr, minute, sec)
    Epoch = cal.toEpoch(yyyy, mm, dd, time)
    return Epoch

def calTimeZone():
    longtitude = v_longitude_arcmin.get()
    zone = cal.timeZone(longtitude)
    v_timezone.set(zone)
    return zone

def setUTC():
    hr = int(v_hr.get())
    v_UTC_min.set(v_min.get())
    v_UTC_sec.set(v_sec.get())
    zone = int(v_timezone.get())
    UTC_hr = hr -zone
    v_UTC_hr.set(str(UTC_hr))
    

def CalSat():
    calTimeZone()
    setUTC()

    next_Epoch = SetEpoch()
    last_Epoch = float(Kepler_element[0])
    Motion = float(Kepler_element[6])
    Anomaly = float(Kepler_element[5])
    RAAN = float(Kepler_element[2])
    Perigee = float(Kepler_element[4])
    i = float(Kepler_element[1])
    e = float(Kepler_element[3])
    M = cal.calMean(last_Epoch, next_Epoch, Motion, Anomaly)
    E = cal.solveE(M,e)
    v = cal.calTrue(E,e)
    alpha = v + Perigee
    position = cal.toRA(i,alpha,RAAN)
    Dec = position[0]
    RA = position[1]
    v_RA.set(RA)
    v_dec.set(Dec)
    print('FROM USER INTERFACE')
    print('i : ', i)
    print('alpha : ', alpha)
    print('RAAN : ', RAAN)
    print('perigee :', Perigee)
    print('e :', e)
    print('=========================')
    print('M : ', M)
    print('E : ', E)
    print('v : ', v)
    print('RA : ', RA)
    print('Dec : ', Dec)
    

    
    



Title1 = Label(T1, text = 'Satellite Data', font=TITLE).grid(row=0,column=0)
blank1 = Label(T1).grid(row=1,column=0)
HD1 = Label(T1, text = 'Catalog number : ',font = HD2).grid(row=2,column=0,sticky = 'E')
E1_1 = Entry(T1, textvariable = v_catalog, width = 30)
E1_1.grid(row=2,column=1)
E1_1.bind('<Return>', SearchSat)
B1_1 = Button(T1, text = 'search', command = SearchSat).grid(row=2, column = 2, sticky ='E')


L1_1_1 = Label(T1, text = 'Name :', font = NORMAL).grid(row=3,column = 0,sticky = 'E')
L1_1_2 = Label(T1, textvariable = v_sat_name, font =NORMAL).grid(row = 3, column = 1, sticky = 'W')
L1_2_1 = Label(T1, text = 'Designator :', font = NORMAL).grid(row=4,column = 0,sticky = 'E')
L1_2_2 = Label(T1, textvariable = v_sat_designator, font =NORMAL).grid(row = 4, column = 1, sticky = 'W')
blank2 = Label(T1).grid(row=5,column=0)

Title2 = Label(T1, text = 'Observer Data', font=TITLE).grid(row=6,column=0)

L1_3 = Label(T1, text = 'Latitude :', font = NORMAL).grid(row=7,column = 0,sticky = 'E')
E1_2 = Entry(T1, textvariable = v_latitude_arcmin, width = 5).place(x=250,y=235)
L1_4 = Label(T1, text = chr(176),font=NORMAL).place(x=280,y=230)
E1_3 = Entry(T1, textvariable = v_latitude_arcsec, width = 5).place(x=300,y=235)
L1_5 = Label(T1, text = '\'',font=NORMAL).place(x=330,y=230)
E1_4 = Entry(T1, textvariable = v_latitude_miliarcsec, width = 5).place(x=350,y=235)
L1_6 = Label(T1, text = '\'\'',font=NORMAL).place(x=380,y=230)

L1_3 = Label(T1, text = 'Longitude :', font = NORMAL).grid(row=7,column = 2,sticky = 'E')
E1_2 = Entry(T1, textvariable = v_longitude_arcmin, width = 5).place(x=520,y=235)
L1_4 = Label(T1, text = chr(176),font=NORMAL).place(x=550,y=230)
E1_3 = Entry(T1, textvariable = v_longitude_arcsec, width = 5).place(x=570,y=235)
L1_5 = Label(T1, text = '\'',font=NORMAL).place(x=600,y=230)
E1_4 = Entry(T1, textvariable = v_longitude_miliarcsec, width = 5).place(x=620,y=235)
L1_6 = Label(T1, text = '\'\'',font=NORMAL).place(x=650,y=230)



L1_7 = Label(T1, text = 'Date :', font = NORMAL).grid(row=8,column = 0,sticky = 'E')
E1_5 = Entry(T1, textvariable = v_dd, width = 5).place(x=250,y=265)
L1_8 = Label(T1, text = '--',font=NORMAL).place(x=280,y=260)
E1_6 = Entry(T1, textvariable = v_mm, width = 5).place(x=300,y=265)
L1_9 = Label(T1, text = '--',font=NORMAL).place(x=330,y=260)
E1_7= Entry(T1, textvariable = v_yyyy, width = 10).place(x=350,y=265)

L1_10 = Label(T1, text = 'Time :', font = NORMAL).grid(row=9,column = 0,sticky = 'E')
E1_8 = Entry(T1, textvariable = v_hr, width = 5).place(x=250,y=295)
L1_11 = Label(T1, text = ':',font=NORMAL).place(x=280,y=290)
E1_9 = Entry(T1, textvariable = v_min, width = 5).place(x=300,y=295)
L1_12 = Label(T1, text = ':',font=NORMAL).place(x=330,y=290)
E1_10= Entry(T1, textvariable = v_sec, width = 5).place(x=350,y=295)
blank3 = Label(T1).grid(row=10,column=0)

B1_2 = Button(T1, text = 'Calculate', font = NORMAL, command = CalSat).place(x=500, y = 270)

L1_13_3 = Label(T1, text = 'Timezone :',font=NORMAL).grid(row=12,column = 0, sticky = 'E')
L1_13_4 = Label(T1, textvariable = v_timezone ,font=NORMAL).grid(row=12,column = 1, sticky = 'E')
L1_13_3 = Label(T1, text = 'UTC :',font=NORMAL).grid(row=13,column = 0, sticky = 'E')
L1_13_7 = Label(T1, textvariable = v_UTC_hr ,font=NORMAL).grid(row=13,column = 1, sticky = 'E')
L1_13_8 = Label(T1, textvariable = v_UTC_min ,font=NORMAL).grid(row=13,column = 2, sticky = 'E')
L1_13_9 = Label(T1, textvariable = v_UTC_sec ,font=NORMAL).grid(row=13,column = 3, sticky = 'E')
L1_13_1 = Label(T1, text = 'RA :',font=NORMAL).grid(row=14,column = 0, sticky = 'E')
L1_13_2 = Label(T1, textvariable = v_RA ,font=NORMAL).grid(row=14,column = 1, sticky = 'E')
L1_14_2 = Label(T1, textvariable = v_dec,font=NORMAL).grid(row=15,column = 1, sticky = 'E')
L1_14_1 = Label(T1, text = 'Declination :',font=NORMAL).grid(row=15,column = 0, sticky = 'E')
L1_15_1 = Label(T1, text = ' :',font=NORMAL).grid(row=14,column = 0, sticky = 'E')
L1_15_2 = Label(T1, textvariable = v_RA ,font=NORMAL).grid(row=14,column = 1, sticky = 'E')



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
