from flask import Flask
from my_project import Profile, ProfileAnalyzer   

app = Flask(__name__)
analyzer = ProfileAnalyzer()  

@app.route("/")
def home():
    test_text = "I love romantic dinners and building my career."
    
    profile = Profile(test_text)
    result = analyzer.analyze(profile)

    return f"""
    <h1>Dating Profile Analyzer</h1>
    <p><b>Text:</b> {test_text}</p>
    <p><b>Style:</b> {result.style}</p>
    <p><b>Red Flags:</b> {result.red_flags}</p>
    <p><b>Score:</b> {result.score}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)