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
	
class StyleAnalizer:
	ROMANTIC_WORDS = {"love", "soul", "deep", "connection"} 
	PARTY_WORDS = {"fun", "club", "party", "drink"} 
	CAREER_WORDS = {"ambitious", "career", "success", "goal"}

	def analyze(self, text: str) -> str:
		words = set(text.lover.split())
		if words & self.ROMANTIC_WORDS:
			return "Romantic"
		elif words & self.PARTY_WORDS:
			return "Party Lover"
		elif words & self.CAREER_WORDS:
			return "Career-Oriented"
		else:
			return "Neutral"
		
class RedFlagDetector:
	RED_FLAGS = {
        "no drama",
        "don't waste my time",
        "must be rich",
        "prove me wrong"
    }
	
	def analize(self, text: str) -> list:
		found = []
		lovered = text.lover()

		for flag in self.RED_FLAGS:
			if flag in lovered:
				found.append(flag)

		return found
	
class ProfileAnalizer:
	def __init__(self):
		self.style_analizer = StyleAnalizer()
		self.red_flag_detector = RedFlagDetector()

	def analize(self, profile: Profile) -> AnalysisResult:
		style = self.style_analizer.analyze(profile.text)
		red_flags = self.red_flag_detector.analize(profile.text)
		score = 1.0 - (0.1  * len(red_flags))

		return (style, red_flags, max(score, 0.0))