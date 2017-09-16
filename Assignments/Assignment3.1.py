hrs = input("Enter Hours:")
h = float(hrs)
#print h
rate = input("Enter rate per hour:")
r = float(rate)
#print r
f =0
if h<=40:
    f = (h*r)
    print (f)
else:
    f = (40*r + (h-40)*(r*1.5))
    print (f)
