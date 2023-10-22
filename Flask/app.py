from flask import Flask, render_template, jsonify
import json
import os 

def get_dataset_path(sub_directory,file_name):
    base_dir = os.getcwd()
    target_dir = os.path.dirname(base_dir)
    file_path = os.path.join(target_dir, sub_directory,file_name)
    return file_path

def get_data_from_json(file):
    file_path = get_dataset_path("project\\MachineLearning\\GraphicData",file)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

data = get_data_from_json("comment_number_graphic_source.json")

app = Flask(__name__)

@app.route('/')
def get_all_posts():
   return render_template("index.html")


@app.route("/sentiment_graphic")
def sentiment_garphic():
    sentiment_graphic_data = get_data_from_json("sentiment_graphic_source.json")
    return render_template("sentiment_graphic.html",sentiment_graphic_data =sentiment_graphic_data)

@app.route("/number_of_comments")
def number_of_comments():
    comment_numbers = get_data_from_json("comment_number_graphic_source.json")
    automobiles = get_data_from_json("automobiles.json")
    return render_template("number_of_comments.html",comment_numbers = comment_numbers,automobiles = automobiles)

@app.route("/brands")
def brands():
    return render_template("brands.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/<brand>')
def brand_page(brand):
   sentiments = get_data_from_json("sentiment_graphic_source.json")
   automobiles = get_data_from_json("automobiles.json")
   scores = get_data_from_json("average_score_source.json")
   idx = automobiles.index(brand)
   graphic = []
   graphic.append(sentiments[0])
   graphic.append(sentiments[idx+1])
   sentiment = scores[idx+1]/100
   return render_template('brand.html', brand=brand,sentiment = sentiment,graphic =graphic)



if __name__ == "__main__":
    app.run(debug=True)

