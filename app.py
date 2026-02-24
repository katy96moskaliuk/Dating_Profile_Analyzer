from flask import Flask, render_template, request   
from my_project import Profile, ProfileAnalyzer   

app = Flask(__name__)
analyzer = ProfileAnalyzer()  

@app.route("/", methods=["GET", "POST"])   
def home():
    text = ""        
    result = None    

    if request.method == "POST":
        text = request.form["profile_text"]   
        profile = Profile(text)
        result = analyzer.analyze(profile)
    
    return render_template("index.html", text=text, result=result)

if __name__ == "__main__":
    app.run(debug=True)