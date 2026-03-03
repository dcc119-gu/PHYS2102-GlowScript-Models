Web VPython 3.2

# Setting up 3D View
scene.range = 3E-10 # m, the half-width of the view
scene.autoscale = 0

### Constants
d = 8E-11 # meters
mu = 1E-7 # N/A^2
q = 1.6E-19 # Coulombs

### Objects
proton = sphere(pos=vector(0,0,0),radius=1E-11,color=color.red)
barrowlist = [] # empty list of vectors

num_obs = 6 # number of observation points/arrows
i = 0
while i < num_obs:
    angle = (2 * pi * i) / num_obs  # evenly space arrows around the circle 
    pos = vector(0, d * cos(angle), d * sin(angle))  # observation point in yz-plane
    barrowlist.append(arrow(pos=pos, color=color.cyan))  # create arrow and add to list
    i = i + 1


### Initial Values
proton.pos = vector(-4E-10,0,0) # m, the proton's initial position
velocity = 2E4 # m/s, the proton's initial velocity

### Computation
t = 0 # seconds, initial time
tfinal = 1 # seconds, final time
deltat = 1.0E-19 # seconds
v = vector(velocity,0,0)

rfinal = 4E-10

while proton.pos.x < rfinal : 
    rate(100000)
    
    i = 0
    while (i < num_obs):
        # For each observation location, calculate:
        # 1. relative position vector r 
        r = barrowlist[i].pos - proton.pos
        
        # 2. magnetic field vector
        Bfield = (mu*q*cross(v, r.hat)/r.mag**2)
    
        # 3. new axis for the arrow (to scale)
        barrowlist[i].axis = Bfield * 5E-9
        i = i + 1
        
    # move proton along x axis
    proton.pos.x = proton.pos.x+(velocity*deltat)

    t=t+deltat
    
print("done")
