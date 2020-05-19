class Item:
	def __init__(self, name, description):
			self.name = name
			self.description = description

	def on_take(self):
			print(f"You pick up a {self.name}")

	def on_drop(self):
			print(f"You drop a {self.name}")

class LightSource(Item):
	def __init__(self, name, description):
			self.name = name
			self.description = description
    
	def on_drop(self):
	    	print(f"Why did you drop your {self.name}? It's still on the floor. Pick it up!")
