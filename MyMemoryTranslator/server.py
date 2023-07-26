
from deep_translator import MyMemoryTranslator
from flask import Flask,render_template
app = Flask("Translator application")
@app.route('/englishToFrench/')
def english_to_french():
    '''function translates English to French'''
    translated = MyMemoryTranslator(source="english", target="french").translate(text)
    return render_template("englishtoFrench.html",translated=translated)

@app.route('/frenchToEnglish')
def french_to_english():
    '''function translates French to English'''
    translated1 = MyMemoryTranslator(source="french", target="english").translate(text)
    return render_template("frenchtoEnglish.html", translated1=translated1)

text = "Hello World, This is a translation program that will help English and French speakers communicate better.Thank you"

with app.app_context():
    english_to_french()
if __name__ == '__main__':
    app.run(debug=True)
    
    