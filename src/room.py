# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	def __init__(self, name, description, is_light=False, items=[]):
		self.name = name
		self.items = items
		self.is_light = is_light
		self.n_to = self
		self.e_to = self
		self.s_to = self
		self.w_to = self

		if is_light==False:
			self.description = "If only there was an item you could pick up to help you see better..."
		else: self.description = description

	def move(self, direction):
		new_room = self.__getattribute__(direction)
        
		if new_room == self:
			return("\nDanger Will Robinson! Danger! Don't go that way!\n")
		return new_room