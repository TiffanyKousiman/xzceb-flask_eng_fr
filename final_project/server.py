"""
import the package machinetranslation into server.py and create flask end points
"""

from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """
    this method uses the implemented translation function through imported package 
    and module, and take the english text as input through the request parameter 
    and return a string.
    """
    text_to_translate = request.args.get('textToTranslate')
    french_text = translator.english_to_french(text_to_translate)

    return french_text

@app.route("/frenchToEnglish")
def french_to_english():
    """
    this method uses the implemented translation function through imported package 
    and module, and take the french text as input through the request parameter 
    and return a string.
    """
    text_to_translate = request.args.get('textToTranslate')
    english_text = translator.french_to_english(text_to_translate)

    return english_text

@app.route("/")
def render_index_page():
    """
    renders index.html using render_template function
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
