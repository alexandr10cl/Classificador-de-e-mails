from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv
from google import genai
import json

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/classify', methods=['POST'])
def classify_email():
    email_content = request.form.get('email_content')

    client = genai.Client()

    gemini_question = "Classifique o seguinte email como Produtivo ou Improdutivo e gere uma resposta automática, retornando em formato JSON com as chaves 'classificacao' e 'resposta':\n\n" + email_content


    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=gemini_question
    )


    return render_template('index.html', resposta=response.text,)


if __name__ == "__main__":
    app.run(debug=True)
