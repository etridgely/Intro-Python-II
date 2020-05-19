# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, name, current_room, inventory=[]):
		self.name = name
		self.current_room = current_room
		self.inventory = inventory

		for item in self.inventory:
			if item is isinstance('item', LightSource):
				# self.current_room.is_light=True
				print("True")
			else:
				print("False")

	def take(self, item):
		if item in self.current_room.items:
			item.on_take()
			self.current_room.items.remove(item)
			self.inventory.append(item)
		else:
			print('\nHmmm. I do not see that. Try again?\n')

	def drop(self, item):
		if item in self.inventory:
			item.on_drop()
			self.inventory.remove(item)
			self.current_room.items.append(item)
		else:
			print('\nNice try. You already have that. \n')

	def holding(self):
		print('\nIn your posession you have a:\n')
		for item in self.inventory:
			print(item.name)