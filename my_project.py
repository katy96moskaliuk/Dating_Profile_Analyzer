class Profile:
	def __init__(self, text: str):
		self.text = text.strip()

	def __repr__(self):
		return f"Profile (text_lenght = ({len(self.text)})"
	
p = Profile(" Kate 25 fine")
print(p.text)
print(p)