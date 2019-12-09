class Singleton:
	__instance=None
	
	@staticmethod
	def getInstance():
		if Singleton.__instance == None:
			Singleton()
		return Singleton.__instance
	
	def __init__(self):
		if Singleton.__instance != None:
			raise Exception("Class is SIngleton")
		else:
			Singleton.__instance = self
			
s = Singleton()
print(s)

y = Singleton.getInstance()
print(y)