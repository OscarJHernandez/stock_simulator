import numpy as np


class stock_simulator:
	
	
	def __init__(self, mu,sigma):
		self.mu = mu
		self.sigma = sigma		
		
		return None
		
	def simulate_stock(self,steps):
		
		self.S = [1.0]
		
		for tk in range(1,steps+1):
			
			# The ratio S(t+1)/S(t) is log normal
			s_ratio = np.exp(np.random.normal(loc=self.mu,scale=self.sigma))
			r = s_ratio
			
			skp1 = r*self.S[tk-1]
			self.S.append(skp1)
			
		self.S = np.asarray(self.S)
		
		return self.S
	
	def simulate_GBM(self,steps,mu=None):
		
		self.S=[1.0]
		
		for tk in range(1,steps+1):
			sigma =  self.sigma
			s_ratio = np.exp(np.random.normal(loc=self.mu-0.5*sigma**2,scale=sigma))
			r = s_ratio
			
			skp1= r*self.S[tk-1]
			self.S.append(skp1)
		
		self.S = np.asarray(self.S)
		
		return self.S
		
	def stock_returns(self,N):
		Sr = []
		
		for i in range(1,len(self.S)):
			
			if(i%N==0):
				r = (self.S[i]-self.S[i-1])/self.S[i-1]
				Sr.append(r)
				
		Sr = np.asarray(Sr)
		
		return Sr	
