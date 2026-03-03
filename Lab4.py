Web VPython 3.2

eps0 = 8.85E-12 # F/m
Q = 10E-3 # C Coulombs, charge on the plates 
R = 5E-2 # m, radius of the disks
d = 2*R #m, distance between disks
sigma = Q/(pi*(R**2)) # C/m^2, surface charge density

N = 100 # number of divisions from z = 0 to z = d
deltaz = d/N

# initializations
i = 0
z = 0
deltaV = 0

while i < N : # computationally integrating from the positive plate at z = 0 to the negative plate at z = d
 
    Ez_pos = (sigma/(2*eps0)) * (1 - z/sqrt(R**2 + z**2))
    Ez_neg = (sigma/(2*eps0)) * (1 - (d-z)/sqrt(R**2 + (d-z)**2))
    
    Ez = Ez_pos + Ez_neg # Total field
    deltaV = deltaV + Ez * deltaz
    z = z - deltaz
    i = i + 1

C = Q/deltaV


# multiply each by 1E9 to get nF
print('calculated capacitance (nF): ', C*1E9)
print('approximate capacitance (nF): ', (eps0*pi*R**2/d)*1E9 )
