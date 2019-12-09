class Button:
	def _get_blue_button(self):
		print("Blue Button")
		
	def _get_green_button(self):
		print("Green Button")
	
	def _get_button(self, button_type):
		if(button_type == "blue"):
			return self._get_blue_button
		if(button_type == "green"):
			return self._get_green_button
			

generic_button = Button();
mybluemethod = generic_button._get_button("blue")
mybluemethod()

mygreenmethod = generic_button._get_button("green")
mygreenmethod()