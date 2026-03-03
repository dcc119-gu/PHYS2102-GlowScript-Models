Web VPython 3.2

# Constants
e = 1.6E-19 # C, fundamental unit of charge
ke = 9.0E9 # N*m**2/C**2
A2m = 1.0E-10 # meters per Angstrom
scalefactor = 3E-18

xaxis = cylinder(pos=vector(-50.,0.,0.)*A2m, axis=vector (100.,0.,0.)*A2m, radius=0.2*A2m)
yaxis = cylinder(pos=vector(0.,-50.,0.)*A2m, axis=vector (0.,100.,0.)*A2m, radius=0.2*A2m)
zaxis = cylinder(pos=vector(0.,0.,-50.)*A2m, axis=vector (0.,0.,100.)*A2m, radius=0.2*A2m)

rsource = vector(0.,0.,0.) # original position of the point charge (origin)
ion = sphere(pos=rsource,radius=1.*A2m,color=color.yellow)
ion.q = -e

# Visualizations
t = 0
theta = 0 

while(t < 12):
    # calculate and display Efield for the current observation point
    robs = 20*A2m*vector(0, cos(theta), sin(theta))
    r  = robs-rsource
    Efield = ke*ion.q*r.hat/(r.mag**2)
    Earrow = arrow(pos=robs, axis=Efield*scalefactor, color=color.orange) 
    
    # update observation location
    theta = theta + pi/6 

    t = t+1
    
