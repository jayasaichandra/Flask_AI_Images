from flask import Flask, render_template, Blueprint
from flask import request
import openai
import requests 
from PIL import Image
from io import BytesIO
import webbrowser

openai.api_key = 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

app = Flask(__name__)

@app.route("/")
def index():
    AI_text = request.args.get("AI_text", "")
    if AI_text:
        url1 = image_gen(AI_text) 
        # using requests library to get the image in bytes 
        response = requests.get(url1)
        webbrowser.open(url1)
    else:
        fahrenheit = ""
    return (
        """<form action="" method="get">
                Enter the text to generate AI Image: <input type="text" name="AI_text">
                <input type="submit" value="Generate AI Image">
            </form>"""
        + "New Browser will pop up with AI Image: "
        + "next tab"
    )

@app.route('/text.html')
def text_temp():
    AI_text = request.args.get("color1", "")
    if AI_text:
        url1 = image_gen(AI_text) 
        # using requests library to get the image in bytes 
        response = requests.get(url1)
        webbrowser.open(url1)
    return render_template('text.html')


def image_gen(AI_test):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        res = openai.Image.create(
            prompt=AI_test,
            n=1,
            size='1024x1024',
        )
        return res["data"][0]["url"] 
    
    except ValueError:
        return "invalid input"
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
