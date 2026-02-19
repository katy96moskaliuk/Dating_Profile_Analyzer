class Profile:
    def __init__(self, text: str):
        self.text = text.strip()

    def __repr__(self):
        return f"Profile(text_length={len(self.text)})"


class AnalysisResult:
    def __init__(self, style: str, red_flags: list, score: float):
        self.style = style
        self.red_flags = red_flags
        self.score = score

    def __repr__(self):
        return f"AnalysisResult(style={self.style}, red_flags={self.red_flags}, score={self.score})"


class StyleAnalyzer:
    ROMANTIC_WORDS = {"love", "loving", "romantic", "romance",
    "soul", "soulmate", "deep", "connection",
    "passion", "passionate", "heart", "feelings",
    "affection", "intimacy", "chemistry",
    "loyal", "loyalty", "caring", "sweet",
    "honest", "trust", "together", "forever"}
    PARTY_WORDS = { "fun", "club", "party", "drink", "drinks",
    "nightlife", "dance", "dancing", "dj",
    "music", "festival", "bar", "shots",
    "weekend", "crazy", "wild", "adventure",
    "social", "friends", "hangout",
    "travel", "spontaneous", "energy"}
    CAREER_WORDS = {"ambitious", "career", "success", "goal",
    "goals", "driven", "focused", "growth",
    "business", "entrepreneur", "startup",
    "leader", "leadership", "professional",
    "motivated", "discipline", "hardworking",
    "achievement", "results", "strategy",
    "development", "future", "independent"}

    def analyze(self, text: str) -> str:
        words = set(text.lower().split())

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

    def analyze(self, text: str) -> list:
        found = []
        lowered = text.lower()

        for flag in self.RED_FLAGS:
            if flag in lowered:
                found.append(flag)

        return found


class ProfileAnalyzer:
    def __init__(self):
        self.style_analyzer = StyleAnalyzer()
        self.red_flag_detector = RedFlagDetector()

    def analyze(self, profile: Profile) -> AnalysisResult:
        style = self.style_analyzer.analyze(profile.text)
        red_flags = self.red_flag_detector.analyze(profile.text)
        score = 1.0 - (0.1 * len(red_flags))

        return AnalysisResult(style, red_flags, max(score, 0.0))


if __name__ == "__main__":
    print("Dating Profile Analyzer")
    text = input("Enter dating profile text: ")

    profile = Profile(text)
    analyzer = ProfileAnalyzer()
    result = analyzer.analyze(profile)

    print("\nAnalysis Result")
    print(f"Style: {result.style}")
    print(f"Red Flags: {result.red_flags}")
    print(f"Score: {result.score}")
