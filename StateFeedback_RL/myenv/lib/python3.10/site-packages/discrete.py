# discrete.py: pure python implementation of discrete random generator.
# Ben Rosser <bjr@sas.upenn.edu>

"""Pure Python implementation of discrete random generator.


"""

import abc
import decimal
import math
import multiprocessing
import random

def seed(a=None):
	random.seed(a)

def _cdf(obj, k):
	return obj.cdf(k)

class Discrete(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self, mu, sigma):
		self.mu = mu
		self.sigma = sigma

		self.max = None

	@abc.abstractmethod
	def pdf(self):
		pass

	@abc.abstractmethod
	def cdf(self):
		pass

	def generate(self, n=1, cutoff=0.99995):
		cdfs = {-1:0}
		j = 0

		# We can't completely parallelize this calculation, but we can compute num_cpus
		# of these at a time.
		pool = multiprocessing.Pool()
		while cdfs[max(cdfs.keys())] <= cutoff:
			mp_results = []
			for k in range(j, j + multiprocessing.cpu_count()):
				mp_results.append(pool.apply_async(_cdf, (self, k,)))
				if self.max is not None and k >= self.max:
					break
			for result in mp_results:
				cdfs[j] = result.get()
				j += 1
			if self.max is not None and k >= self.max:
				break
		pool.close()
		pool.join()

		results = []
		for i in range(n):
			uniform = random.random()
			for j in range(len(cdfs) - 1):
				if cdfs[j - 1] <= uniform and uniform < cdfs[j]:
					results.append(j)
					break
		return results

class Poisson(Discrete):

	def __init__(self, mu):
		super(Poisson, self).__init__(mu, mu)

	def pdf(self, k):
#		pdf = (self.mu**k * math.exp(-self.mu)) / math.factorial(k)
		pdf = decimal.Decimal(self.mu)**decimal.Decimal(k)
		pdf *= decimal.Decimal(-self.mu).exp()
		pdf /= math.factorial(decimal.Decimal(k))
		return float(pdf)

	def cdf(self, k):
		result = 0
		for i in range(int(math.floor(k) + 1)):
			result += self.pdf(i)
		return result

class Binomial(Discrete):

	def __init__(self, n, p):
		super(Binomial, self).__init__(n*p, n*p*(1-p))
		self.n = n
		self.p = p
		self.max = n

	def pdf(self, k):
		choose = math.factorial(decimal.Decimal(self.n)) / (math.factorial(decimal.Decimal(self.n-k)) * math.factorial(decimal.Decimal(k)))
		pdf = choose * self.p**k * (1 - self.p)**(self.n - k)
		return pdf

	def cdf(self, k):
		result = 0
		for i in range(int(math.floor(k) + 1)):
			result += self.pdf(i)
		return result
