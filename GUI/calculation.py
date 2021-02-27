import numpy as np
import sympy as sy
import math

def toRad(theta):
    return theta * math.pi / 180

def toDeg(theta):
    return theta *180 / math.pi

def solveE(M,e):
    E = sy.symbols('E')
    M = toRad(M)
    F = E-e*sy.sin(E)-M
    Fderivative = F.diff(E)
    En = M
    for i in range(10):
        En = En-np.float(F.evalf(subs = {E:En}))/np.float(Fderivative.evalf(subs = {E:En}))
        #print(f'The {i+1} iteration xn is {En:.10} and f(xn) is {np.float(F.evalf(subs= {E:En})):.2}')
    En = toDeg(En)
    return En

def isLeapyear(yyyy):
    if yyyy%4 == 0 and yyyy%100 != 0 and yyyy%400 != 0:
        return True
    elif yyyy%4 != 0:
        return False
    elif yyyy%4 == 0 and yyyy%100 == 0 and yyyy%400 != 0:
        return False
    elif yyyy%4 == 0 and yyyy%100 == 0 and yyyy%400 == 0:
        return True

def toEpoch(yyyy, mm, dd, time_sec):
    Epoch = ''
    day = 0
    for i in range(1,13):
        if i == mm:
            break
        if i in [1,3,5,7,8,10,12]:
            day = day + 31
        elif i in [6,9,11]:
            day = day + 30
        elif i in [2]: 
            if isLeapyear(yyyy):
                day = day + 29
            else:
                day = day +28
    day = day + dd
    if day < 100:
        day = '0' + str(day)
    if yyyy > 2000:
        yyyy = yyyy - 2000
    time_frac = time_sec
    Epoch = str(yyyy)+str(day)+str(time_frac)[1:]
    return Epoch

def fracTime(hr,minute,sec):
    time = 0
    time = time + float(hr) * 60 *60 
    time = time + float(minute) * 60
    time = time + float(sec)
    time = time/(24*60*60)
    return float(time)

def calMean(last_Epoch, next_Epoch, motion, anomaly):
    t = float(next_Epoch) - float(last_Epoch)
    anomaly = (float(anomaly) + float(motion) * t * 360) % 360
    return anomaly

def calTrue(E,e):
    E = toRad(E)
    tan_v_2 = math.sqrt((1+e)/(1-e)) * math.tan(E/2)
    v = 2 * math.atan(tan_v_2)
    v = toDeg(v)
    return v


def toRA(i, alpha, RAAN):
    i = toRad(i)
    alpha = toRad(alpha)
    sin_delta = math.sin(i) * math.sin(alpha)
    delta = math.asin(sin_delta)
    
    cos_RA = math.cos(alpha)/math.cos(delta)
    tan_RA = (math.cos(delta)**2 - math.cos(alpha)**2)/(math.cos(alpha)*math.sin(alpha)*math.cos(i))

    #cos_RA = 1/2
    #tan_RA = -math.sqrt(3)
    if cos_RA > 0 and tan_RA > 0:
        RA = math.acos(cos_RA)
    elif cos_RA < 0 and tan_RA < 0:
        RA = math.acos(cos_RA)
    elif cos_RA < 0 and tan_RA > 0:
        RA = 2*math.pi - math.acos(cos_RA) 
    elif cos_RA > 0 and tan_RA < 0:
        RA = 2*math.pi - math.acos(cos_RA)
    
    dec = (toDeg(delta))%360
    RA = (toDeg(RA) + RAAN)%360
    return [dec, RA]

def to_Lat_Long(RA,dec,UTC):
    latitute = dec

def timeZone(longt):
    for i in range(0,181,15):
        if float(longt) > i - 7.5 and float(longt) < i +7.5:
            zone = int(i/15)
            return zone
        
def calUTC(hr,minute,sec,timezone):
    UTC_hr = int(hr) - int(timeZone)
    return [UTC_hr, minute, sec]



