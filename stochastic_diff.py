import numpy as np


class stochastic_diff:
	
	
	def __init__(self,v0,x0,sigma):
		self.v0 = v0
		self.x0 = x0
		self.sigma = sigma
		return None
		
	def sim_stoch_ho(self,T0,TF,steps,w0,gamma0):
		
		dt = (TF-T0)/float(steps)
		T = [T0,T0+dt]
		X = [self.x0]
		V = [0.0,self.v0]
		x1 = self.v0*dt+X[0]
		X.append(x1)
		
		for t in range(2,steps):
			dBT = np.random.normal(0.0,scale=self.sigma*np.sqrt(dt))
			fT = -w0**2*X[t-1]
			vT = V[t-1]+dt*fT-gamma0*V[t-1]+dBT
			xT = X[t-1]+vT*dt
			X.append(xT)
			V.append(vT)
			T.append(T0+t*dt)
		
		T = np.asarray(T)
		X = np.asarray(X)
		
		return T,X
