from flask import Flask, render_template
import requests
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

def get_random_quote():
    response = requests.get("https://api.quotable.io/random", verify=False)
    if response.status_code == 200:
        quote = response.json()
        translated_content = translator.translate(quote['content'], src='en', dest='ru').text
        translated_author = translator.translate(quote['author'], src='en', dest='ru').text
        return {"content": translated_content, "author": translated_author}
    return {"content": "Ошибка при получении цитаты.", "author": "Неизвестный"}

@app.route('/')
def index():
    quote = get_random_quote()
    return render_template("baden.html", quote=quote)

if __name__ == '__main__':
    app.run(debug=True)