from person import Person

class kenyan(Person):
	corrupt = False

	def probe (self, corrupt):
		self.corrupt = corrupt

	def is_corrupt (self):
		if self.corrupt:
			return "Yes"
		return "No"



