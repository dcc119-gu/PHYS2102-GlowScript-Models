Web VPython 3.2

# Constants
e = 1.6e-19 # C, charge of a proton
ke = 9e9 # N*m**2/C**2, 1/(4*pi*epsilon0)
A2m = 1e-10 # conversion factor from Angstroms to meters

scalefactor = 3E-18 # for E-field arrows

s = 4*A2m # distance between + and - charge in the dipole

R = 4*s # radius of circle for observation points
N = 3 # number of observation points

# Objects
xaxis = cylinder(pos=vector(-30,0,0)*A2m,axis=vector(60,0,0)*A2m,radius=0.2*A2m,color=color.red)
yaxis = cylinder(pos=vector(0,-30,0)*A2m,axis=vector(0,60,0)*A2m,radius=0.2*A2m,color=color.green)
zaxis = cylinder(pos=vector(0,0,-30)*A2m,axis=vector(0,0,60)*A2m,radius=0.2*A2m,color=color.blue)

rplus = vector(s/2,0,0)
rminus = vector(-s/2,0,0)
plus = sphere(pos=rplus,radius=s*0.2,color=color.red)
minus = sphere(pos=rminus,radius=s*0.2,color=color.blue)
plus.q = e
minus.q = -e

# Initial Values
loop = 0
loc = 16

# Calculations
while (loop < N): 

    robs = vector(0,loc*A2m,0) 

    # electric field due to each charge
    r1 = robs-rplus
    r2 = robs-rminus
    Efield1 = ke*plus.q*r1.hat/(r1.mag**2) # calculate electric field with given equation
    Efield2 = ke*minus.q*r2.hat/(r2.mag**2) # calculate electric field with given equation
    
    # applying superposition
    Efield = Efield1 + Efield2
    print(Efield.mag)
    
    Edipole = (ke)*2*e*s*(1/robs.mag**3) # do simply robs since dipole centered at origin
    print(Edipole)
    
    # arrow representing electric field at observation point
    Earrow = arrow(pos=robs,axis=Efield*scalefactor,color=color.orange)
    
    loop = loop+1
    loc = loc+8
