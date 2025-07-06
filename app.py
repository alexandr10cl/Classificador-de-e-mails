from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv
from google import genai
from PyPDF2 import PdfReader
import json

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/classify', methods=['POST'])
def classify_email():
    final_text  = ""

    # Pegar texto do textarea do formulário
    email_content = request.form.get('email_content')

    if email_content:
        final_text = email_content
    else:
        # Se não houver texto, ler o pdf ou txt enviado
        form_file = request.files.get('file_upload')

        if form_file and form_file.filename:
            filename = form_file.filename.lower()

            if filename.endswith('.txt'):
                final_text = form_file.read().decode('utf-8', errors='ignore')

            elif filename.endswith('.pdf'):
                try:
                    # Usar PyPDF2 para ler PDF
                    reader = PdfReader(form_file)
                    for page in reader.pages:
                        final_text += page.extract_text()
                except Exception as e:
                    return render_template('index.html', tipo=None, resposta="Erro ao ler o PDF.")
        else:
            return render_template('index.html', tipo=None, resposta="Nenhum conteúdo fornecido.")


    client = genai.Client()

    gemini_question = (
    "Classifique o texto abaixo como 'produtivo' ou 'improdutivo' e gere uma resposta automática adequada ao conteúdo. "
    "Responda SOMENTE com um objeto JSON válido, exatamente neste formato:\n\n"
    "{\n"
    '  "tipo": "produtivo" ou "improdutivo",\n'
    '  "resposta": "texto da resposta automática"\n'
    "}\n\n"
    "Texto:\n" + final_text
    )


    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=gemini_question
    )

    print("Resposta do modelo:", response.text)

    # Formatar resposta do modelo
    if response.text:
        resposta_formatada = extrair_json(response.text)
        resposta_formatada = resposta_formatada.replace("'", '"')
    else:
        resposta_formatada = "Sem resposta do modelo."
    
    dados = json.loads(resposta_formatada)

    return render_template('index.html', tipo=dados['tipo'], resposta=dados['resposta'])

# Corrigir o JSON recebido pela IA
def extrair_json(texto):
    inicio = texto.find('{')
    fim = texto.find('}', inicio)

    if inicio != -1 and fim != -1:
        return texto[inicio:fim+1]
    return None

if __name__ == "__main__":
    app.run(debug=True)
