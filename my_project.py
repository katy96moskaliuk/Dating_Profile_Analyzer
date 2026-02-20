import re
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet') 

def load_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return{line.strip() for line in f if line.strip()}


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
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

        self.ROMANTIC_WORDS = load_words("romantic_words.txt")
        self.PARTY_WORDS = load_words("party_words.txt")
        self.CAREER_WORDS = load_words("career_words.txt")
        
        self.ROMANTIC_LEMMAS = set(self.lemmatizer.lemmatize(word, pos='v') for word in self.ROMANTIC_WORDS)
        self.PARTY_LEMMAS = set(self.lemmatizer.lemmatize(word, pos='v') for word in self.PARTY_WORDS)
        self.CAREER_LEMMAS = set(self.lemmatizer.lemmatize(word, pos='v') for word in self.CAREER_WORDS)

    def analyze(self, text: str) -> str:
        words = re.findall(r"\b\w+\b", text.lower())
    
        lemmas = [self.lemmatizer.lemmatize(word, pos='v') for word in words]

        romantic_count = sum(1 for word in lemmas if word in self.ROMANTIC_LEMMAS)
        party_count = sum(1 for word in lemmas if word in self.PARTY_LEMMAS)
        career_count = sum(1 for word in lemmas if word in self.CAREER_LEMMAS)

        total = romantic_count + party_count + career_count

        if total == 0:
            return {"Neutral": 100}

        return {
            "Romantic": round(romantic_count / total * 100),
            "Party Lover": round(party_count / total * 100),
            "Career-Oriented": round(career_count / total * 100)
        }

class RedFlagDetector:
    def __init__(self):
       self.RED_FLAGS = load_words("red_flags.txt")

    def analyze(self, text: str) -> list:
        found = []
        lowered = text.lower()

        for flag in self.RED_FLAGS:
            pattern = r'\b' + re.escape(flag) + r'\b'
            if re.search(pattern, lowered):
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
