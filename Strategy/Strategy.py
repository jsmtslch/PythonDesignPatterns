class Duck:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

class LoudDuck(Duck):
	def quack(self):
		print("QUACK QUACK")

class GentleDuck(Duck):
	def quack(self):
		print("quack")
		
class ToyDuck(GentleDuck):
	def lights_on(self):
		print("Lights on for 10 sec")
		
class VillageDuck(LoudDuck):
	def go_home(self):
		print("Going to village")
		
class CityDuck(GentleDuck):
	def go_home(self):
		print("Going to City")
		
