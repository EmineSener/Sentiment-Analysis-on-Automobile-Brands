from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_all_posts():
   return render_template("index.html")

@app.route('/hey')
def hey():
   return render_template("graphic.html")

@app.route('/e')
def e():
   return render_template("deneme.html")

@app.route("/sentiment_graphic")
def movies_page():
    return render_template("sentiment_graphic.html")

if __name__ == "__main__":
    app.run(debug=True)

