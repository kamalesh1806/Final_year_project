import os
from flask import Flask, render_template
from modes.Image.image import image
from modes.Text.text import text


UPLOAD_IMAGE_FOLDER = 'modes\\Image\\static'
IMAGE_CACHE_FOLDER = 'modes\\Image\\__pycache__'
UPLOAD_TEXT_FOLDER = 'modes\\Text\\static'
TEXT_CACHE_FOLDER = 'modes\\Text\\__pycache__'


# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key = "hello"
app.config['UPLOAD_IMAGE_FOLDER'] = UPLOAD_IMAGE_FOLDER
app.config['IMAGE_CACHE_FOLDER'] = IMAGE_CACHE_FOLDER
app.config['UPLOAD_TEXT_FOLDER'] = UPLOAD_TEXT_FOLDER
app.config['TEXT_CACHE_FOLDER'] = TEXT_CACHE_FOLDER
app.register_blueprint(image, url_prefix="/image")
app.register_blueprint(text, url_prefix="/text")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)