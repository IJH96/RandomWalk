import numpy as np
import math
import matplotlib.pyplot as plt 
x,y,z,r = np.loadtxt("photonDistances2 (3).dat",unpack=True)

r_avg = np.average(r)
sigma_r = np.std(r)

x_avg = np.average(x)
sigma_x = np.std(x)
y_avg = np.average(y)
sigma_y = np.std(y)
z_avg = np.average(z)
sigma_z = np.std(z)
def gaussian(x,mu,sigma):
    return (1/(np.sqrt(2*np.pi)*sigma))*np.exp((-((x-mu)**2))/(2*sigma**2))
#xHist
xhist, xbinEdges = np.histogram(x,bins = "auto" ,density=True)
#get points
u =np.linspace(xbinEdges[0], xbinEdges[len(xbinEdges)-1], 1000)
v = gaussian(u, np.average(x), np.std(x))
#create a plot
plt.hist(x, bins = xbinEdges , density =True)
plt.plot(u,v) #plot the Gaussian pdf
plt.savefig("xHistSun.pdf")
plt.clf()
#yHist
yhist, ybinEdges = np.histogram(y,bins = "auto" ,density=True)
#get points
u =np.linspace(ybinEdges[0], ybinEdges[len(ybinEdges)-1], 1000)
v = gaussian(u, np.average(y), np.std(y))
#create a plot
plt.hist(y, bins = ybinEdges , density =True)
plt.plot(u,v) #plot the Gaussian pdf
plt.savefig("yHistSun.pdf")
plt.clf()
#zHist
zhist, zbinEdges = np.histogram(z,bins = "auto" ,density=True)
#get points
u =np.linspace(zbinEdges[0], zbinEdges[len(zbinEdges)-1], 1000)
v = gaussian(u, np.average(z), np.std(z))
#create a plot
plt.hist(z, bins = zbinEdges , density =True)
plt.plot(u,v) #plot the Gaussian pdf
plt.savefig("zHistSun.pdf")
plt.clf()
#rHist
rhist, rbinEdges = np.histogram(r,bins = "auto" ,density=True)
#get points
u =np.linspace(rbinEdges[0], rbinEdges[len(rbinEdges)-1], 1000)
v = gaussian(u, np.average(r), np.std(r))
#create a plot
plt.hist(r, bins = rbinEdges , density =True)
plt.plot(u,v) #plot the Gaussian pdf
plt.savefig("rHistSun.pdf")
plt.clf()

print("average distance:", x_avg, "+/-", sigma_x)
print("average distance:", y_avg, "+/-", sigma_y)
print("average distance:", z_avg, "+/-", sigma_z)
print("average distance:", r_avg, "+/-", sigma_r)
print("Expected:       ", math.sqrt)

# the r distance standard deviation does not agree. the x,y, and z ones do though.