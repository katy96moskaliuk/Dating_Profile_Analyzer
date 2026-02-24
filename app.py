from flask import Flask, render_template
from my_project import Profile, ProfileAnalyzer   

app = Flask(__name__)
analyzer = ProfileAnalyzer()  

@app.route("/")
def home():
    test_text = "I love romantic dinners and building my career."
    
    profile = Profile(test_text)
    result = analyzer.analyze(profile)

    return render_template("index.html", text=test_text, result=result)

if __name__ == "__main__":
    app.run(debug=True)