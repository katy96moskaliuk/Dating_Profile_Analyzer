import re
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
        words = re.findall(r"\b\w+\b", text.lower())

        romantic_count = sum(1 for word in words if word in self.ROMANTIC_WORDS)
        party_count = sum(1 for word in words if word in self.PARTY_WORDS)
        career_count = sum(1 for word in words if word in self.CAREER_WORDS)

        max_count = max(romantic_count, party_count, career_count)

        if max_count == 0:
            return "Neutral"

        if romantic_count == max_count:
            return "Romantic"
        elif party_count == max_count:
            return "Party Lover"
        else:
            return "Career-Oriented"


class RedFlagDetector:
    RED_FLAGS = {
    "no drama",
    "don't waste my time",
    "must be rich",
    "prove me wrong",
    "looking for trophy partner",
    "only for fun",
    "must be attractive",
    "no commitment",
    "players welcome",
    "only here for hookups",
    "drama free only",
    "must have money",
    "don't contact me if...",
    "serious inquiries only",
    "hit me up if..."
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

        base_score = 1.0
        penalty = 0.15 * len(red_flags)

        if len(profile.text) < 30:
            penalty += 0.1

        score = max(base_score - penalty, 0.0)

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
