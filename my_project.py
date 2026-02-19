class Profile:
	def __init__(self, text: str):
		self.text = text.strip()

	def __repr__(self):
		return f"Profile (text_lenght = ({len(self.text)})"
	
class AnalysisResult:
	def __init__(self, style: str, red_flags: list, score: float):
		self.style = style
		self.red_flags = red_flags
		self.score = score
	
	def __repr__(self):
		return f"AnalysisResult(style={self.style}, red_flags={self.red_flags}, score={self.score})"