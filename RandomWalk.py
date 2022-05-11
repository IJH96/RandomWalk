import numpy as np

def steps(mu, sigma, N):

    x = np.random.normal(mu, sigma, N)
    y = np.random.normal(mu, sigma, N)
    z = np.random.normal(mu, sigma, N)
    return x,y,z

#x,y,z = steps(0.0,0.00577,int(1E8))
#6 seconds for this code if above is used
x,y,z = steps(0.0,324333.0108,int(31557600))
#this is found by realizing that 1 second is 10^8 scattering and there are (31,557,600) s
#2 seconds
X = np.sum(x)
Y = np.sum(y)
Z = np.sum(z)

r = np.sqrt(X**2+Y**2+Z**2)

print("Final photon position", X, ",", Y, ",", Z)
print("Distance from the center", r)





np.savetxt("ExitingSun1.txt", np.column_stack((r,X,Y,Z)))