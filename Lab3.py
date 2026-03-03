Web VPython 3.2

# Constants

e = 1.6e-19 # C, fundamental unit of charge
ke = 9e9 # N*m**2/C**2, 1/(4*pi*epsilon0)
scalefactor = 5E-5 # for electric field arrows

L = 1 # m, length of rod
Q = 2E-8 # C, total charge on rod
N = 500 # number of point charges used to model the rod

dist = 0.1 # m, magnitude of the observation location

deltax = L/N # length of each segment
deltaQ = Q/N # charge of each segment

# Objects
xaxis = cylinder(pos=vector(-0.75,0,0),axis=vector(1.5,0,0),radius=0.005)
yaxis = cylinder(pos=vector(0,-0.75,0),axis=vector(0,1.5,0),radius=0.005)
zaxis = cylinder(pos=vector(0,0,-0.75),axis=vector(0,0,1.5),radius=0.005)

robs = vector(dist*cos(pi/4),dist*sin(pi/4),0) # m, observation location

# Initial Values
Efield = vector(0, 0, 0) # initial value for the calculation
x = -0.5*L + 0.5*deltax # x position of first point charge


# Iterative Calculations
while (x < L/2):
    # calculate electric field due to the point charge representing the current segment
    r = robs - vector(x, 0, 0)
    Efield1 = ke*deltaQ*r.hat/(r.mag**2)
    Efield = Efield + Efield1

    sphere(pos=vector(x, 0, 0), radius=.02, color=color.cyan) # sphere representing point charge
   
    x = x + deltax

# visualize & display the electric field due to the rod
arrow(pos=vector(0,0,0),axis=Efield*scalefactor,color=color.orange)
theta = atan(Efield.y/Efield.x)*(180/pi)
print(Efield.mag, Efield.x, Efield.y, theta)
