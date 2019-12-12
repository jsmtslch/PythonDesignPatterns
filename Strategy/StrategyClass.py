import abc

class QuackStrategyAbstract(object):
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractmethod
	def quack(self):
		"""Required Method"""

class LoudQuackStrategy(QuackStrategyAbstract):
	def quack(self):
		print("QUACK!!!")

class GentleQuackStrategy(QuackStrategyAbstract):
	def quack(self):
		print("quack")

class LightStrategyAbstract(object):
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractmethod
	def light_on(self):
		"""Required Method"""

class LightOnStrategy(LightStrategyAbstract):
	def light_on(self):
		print("Ligh on for 10 secods")