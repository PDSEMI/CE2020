import sqlite3

#Initialize database

sql_create_3LE_table = """CREATE TABLE IF NOT EXISTS Data (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name text,
        CatalogNumber text,
        ElsetClassification text,
        InternationalDesignator text,
        Epoch text,
        Inclination text,
        RAAscending text,
        Eccentricity text,
        ArgOfPerigee text,
        MeanAnomaly text,
        MeanMotion text);
        """


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

database = r"E:\FORUM\Project\CE2020\Test"

conn = create_connection(database)
if conn is not None:
    create_table(conn, sql_create_3LE_table)
else:
    print("Error! cannot create database connection")

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


def insert_data(conn, data):
    sql_insert_satellite_data = """
    INSERT INTO Data( 
        Name, 
        CatalogNumber,
        ElsetClassification,
        InternationalDesignator,
        Epoch,
        Inclination,
        RAAscending,
        Eccentricity,
        ArgOfPerigee,
        MeanAnomaly,
        MeanMotion)
        VALUES(?,?,?,?,?,?,?,?,?,?,?);
    """
    sql_insert_satellite_name = """
    INSERT INTO Data( 
        Name)
        VALUES(?);
    """
    c = conn.cursor()
    c.execute(sql_insert_satellite_data, data)
    conn.commit()

def to_sat_data(sat):
    sat_data =   '\''+ sat.Name + '\',\'' + sat.CatNum + '\',\'' + sat.Class + '\',\'' + sat.Desig + '\',\'' + sat.Epoch + '\',\'' + sat.Incl + '\',\'' + sat.RA + '\',\'' + sat.E + '\',\'' + sat.Perigee + '\',\'' + sat.Anomaly + '\',\'' + sat.Motion  +'\''
    return sat_data
   
######### INSERT DATA ##########
data_file = r"E:\FORUM\Project\CE2020\Scrap\3LE.txt"
data = open(data_file,"r")
i = 0
sat = Satellite()
for line in data:
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
        print(sat_data)
        #insert_data(conn, (sat.Name, sat.CatNum, sat.Class, sat.Desig, sat.Epoch, sat.Incl, sat.RA, sat.E, sat.Perigee, sat.Anomaly, sat.Motion ))
        break

#insert_data(conn, )


conn.close()
data.close()
