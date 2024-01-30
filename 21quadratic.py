# Quadratic equation 

import math

# variables 
a = -3
b = 8
c = 2

q = ( b**2 ) - ( 4*a*c )    # calculate the discriminant

# Solving for both intercepts 
Intercept1 = (-b - math.sqrt(q)) / (2*a)
Intercept2 = (-b + math.sqrt(q)) / (2*a)

print(Intercept1,Intercept2)