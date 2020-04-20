x=123
y=12.23
z=5**3

k = 2
j = 2.0
print("k=", k, "j=", j)
print("k==j", k == j)
print("k is j",k is j)
print(x, y, z)

print("=============================================================================")
print("Math")
print()
import math

x = 2
y = 3
z = 9
print ("x=",x,"y=",y,"z=",z)
print("pov yINx", y**x, pow(y,x))
print("sqrt z", z**0.5, math.sqrt(z), pow(z,0.5))

from fractions import Fraction
import decimal
decimal.getcontext().prec = 6 # set count fix symbol after point

x=2
y=3.75
z = Fraction(4,6)
d = decimal.Decimal('5.00')/decimal.Decimal('3.00')

print ("int", x)
print ("float", y)
print ("Fraction4/6",z)
print ("Decimal" , d)
print ("convert bin:1101 to int", int("1101",2))
print ("convert int:12 to bin", bin(12))

f = 5/3
print ("f", f)
print ("f round",round(f,4)) # round to 4 symbol after point
print ("-f round",round(-f,4))
print ("f floor",math.floor(f) )   #round to int to down
print ("-f floor",math.floor(-f) ) #round to int to down
print ("f trunc",math.trunc(f) )	# to nearly int
print ("-f trunc",math.trunc(-f) )	#to nearly int