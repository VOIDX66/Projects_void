import numpy as np
import matplotlib.pylab as plt

a=b=1

t = np.arange(0,4*np.pi,0.01)
xt = a*np.sin(t)+b*np.sin(2*t)

plt.plot(t,xt)
plt.show()