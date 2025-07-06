# Classificador de E-mails

Este projeto é um sistema web para **classificação automática de e-mails** utilizando IA (Google Gemini). Ele identifica se um e-mail é "produtivo" ou "improdutivo" e sugere uma resposta automática adequada ao conteúdo.

## Funcionalidades

- Classificação automática de e-mails como produtivo ou improdutivo.
- Sugestão de resposta automática baseada no conteúdo do e-mail.
- Suporte a entrada de texto manual ou upload de arquivos `.txt` e `.pdf`.
- Interface web simples e responsiva.

## Tecnologias Utilizadas

- Python com Flask
- API do Google Gemini
- HTML, CSS e Javascript

## Pré-requisitos

- Python 3.11 ou superior instalado
- Conta e chave de API do Google Gemini (Google Generative AI)

## Instalação

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/Classificador-de-e-mails.git
   cd Classificador-de-e-mails
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```sh
   python -m venv venv
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   - Crie um arquivo `.env` na raiz do projeto.
   - Adicione sua chave de API do Google Gemini:
     ```
     GOOGLE_API_KEY=sua_chave_aqui
     ```

## Como Executar

1. **Inicie o servidor Flask:**
   ```sh
   python app.py
   ```

2. **Acesse a aplicação:**
   - Abra o navegador e vá para: [http://localhost:5000](http://localhost:5000)

## Arquivos de exemplo
- Na pasta /exemplos alguns textos de exemplos são disponibilizados para testar a aplicação

## Estrutura do Projeto

```
.
├── app.py
├── requirements.txt
├── .env
├── static/
│   └── index.css
├── templates/
│   └── index.html
├── examples/
│   ├── email1.txt
│   ├── email2.txt
│   └── email3.pdf
└── README.md
```

## Observações

- O sistema utiliza a API do Google Gemini, que pode gerar custos dependendo do uso.
- Apenas arquivos `.txt` e `.pdf` são suportados para upload.

Desenvolvido por Alexandre De Casado Lima Vidal