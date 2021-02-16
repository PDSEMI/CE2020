import xlsxwriter

######### EXCEL #########
workbook = xlsxwriter.Workbook("SatelliteData.xlsx")
worksheet = workbook.add_worksheet()

Header = ['ID', 'NAME', 'CATALOG', 'ELSET CLASSIFICATION', 'INTERNATIONAL DESIGNATOR', 'EPOCH', 'INCLINATION', 'RA OF ASC_NODE','ECCENTRICITY', 'ARG OF PERIGEE', 'ANOMALY', 'MOTION']
i = 0
for column_name in Header:
    worksheet.write(0,i, column_name)
    i = i+1


######### END OF DATABASE INITIALIZE #########
class Satellite:
    def __init__(self):
        self.Name = None
        self.CatNum = None
        self.Class = None
        self.Desig = None
        self.Epoch = None
        self.Incl = None
        self.RA = None
        self.E = None
        self.Perigee = None
        self.Anomaly = None
        self.Motion = None

def to_sat_data(sat):
    sat_data =  [sat.Name,sat.CatNum,sat.Class,sat.Desig,sat.Epoch,sat.Incl,sat.RA,sat.E,sat.Perigee,sat.Anomaly,sat.Motion]
    return sat_data
   
######### INSERT DATA ##########
data_file = r"E:\FORUM\Project\CE2020\Scrap\3LE.txt"
data = open(data_file,"r")
i = 0
sat = Satellite()
row = 1
for line in data:
    column = 1
    i = i+1
    if i%3 == 1:
        name = line[1:24]
        sat.Name = name
    elif i%3 == 2:
        sat.CatNum = line[2:7]
        sat.Class = line[7]
        sat.Desig = line[9:17]
        sat.Epoch = line[17:32]
    elif i%3 == 0:
        sat.Incl = line[8:17]
        sat.RA = line[17:25]
        sat.E = line[26:33]
        sat.Perigee = line[34:42]
        sat.Anomaly = line[43:51]
        sat.Motion = line[52:63]
        sat_data = to_sat_data(sat)
        worksheet.write(row, 0, row)
        for data in sat_data:
            worksheet.write(row, column, data)
            column = column + 1 
        row = row +1
        #insert_data(conn, (sat.Name, sat.CatNum, sat.Class, sat.Desig, sat.Epoch, sat.Incl, sat.RA, sat.E, sat.Perigee, sat.Anomaly, sat.Motion ))


#insert_data(conn, )

print("END SECTION")
workbook.close()
