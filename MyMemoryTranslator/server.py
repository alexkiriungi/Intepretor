
from deep_translator import MyMemoryTranslator
from flask import Flask,render_template
app = Flask("Translator application")
@app.route('/englishToFrench', methods=['GET'])
def english_to_french(text):
    '''function translates English to French'''
    translated = MyMemoryTranslator(source="english", target="french").translate(text)
    return render_template("englishtoFrench.html", translated)

@app.route('/frenchToEnglish')
def french_to_english(text1):
    '''function translates French to English'''
    translated1 = MyMemoryTranslator(source="french", traget="english").translate(text1)
    return render_template("frenchtoEnglish.html", translated1)

text = "Hello World, This is a translation program that will help English and French speakers communicate better.Thank you"
if __name__ == '__main__':
    app.run(debug=True)
    
    