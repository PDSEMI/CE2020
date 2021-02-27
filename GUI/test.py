from datetime import datetime
UTC = datetime.utcnow()
import calculation as cal
print(UTC)

last_Epoch = 1288.95265372

T= 0.68147327814859
rev = 1.00684
i = 9.8219
last_RAAN = 19.7599
new_RAAN  = 252.6057
e = 0.000422
perigee = 26.002
anomaly = 82.6845

M = 43.15752713743473

E = cal.solveE(M,e)

v = cal.calTrue(E,e)

alpha = perigee + v

position = cal.toRA(i ,alpha, last_RAAN)
declination = (position[0])
last_RA = (position[1])

#print('last_RAAN : ', last_RAAN)
#print('new_RAAN : ', new_RAAN)
#print('Delta RA: ', deltaRA)

#print('new_RA : ', (deltaRA + new_RAAN)%360)
#print('Real RA :', 333.572)

print('M = ', M)
print('E = ', E)
print('v = ', v)
print('alpha = ', alpha)
print('Dec : ', declination)
print('last_RA : ', last_RA)


