import pickle 
import numpy as np
t=np.arange(0,1,0.01)
f=3
x=np.sin(2*np.pi*f*t)
with open("picklee.pkl","wb")as k:
	pickle.dump(x,k)
