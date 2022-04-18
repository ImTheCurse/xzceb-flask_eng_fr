import translation
from translation import Onlytranslator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/eng_To_French")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.eng_to_french(textToTranslate)

@app.route("/fr_To_eng")
def fr_To_eng():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.fr_To_eng(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
