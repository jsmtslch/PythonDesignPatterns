from StrategyClass import LoudQuackStrategy
from StrategyClass import GentleQuackStrategy
from StrategyClass import LightOnStrategy

loud_quack = LoudQuackStrategy()
gentle_quack = GentleQuackStrategy()
ten_seconds = LightOnStrategy()

class Duck(object):
	def __init__(self, quack_strategy, light_strategy):
		self._quack_strategy = quack_strategy
		self._light_strategy = light_strategy
	def quack(self):
		self._quack_strategy.quack()
	def light_on(self):
		self._light_strategy.light_on()

class VillageDuck(Duck):
	def __init__(self):
		super().__init__(loud_quack, None)
	def go_home(self):
		print("Going to Village")
		
class ToyDuck(Duck):
	def __init__(self):
		super().__init__(gentle_quack, ten_seconds)

class CityDuck(Duck):
	def __init__(self):
		super().__init__(gentle_quack, None)
	
	def go_home(self):
		print("Going to City")

class RoboDuck(Duck):
	def __init__(self):
		super().__init__(loud_quack, ten_seconds)

robo = RoboDuck()
robo.quack()
robo.light_on()