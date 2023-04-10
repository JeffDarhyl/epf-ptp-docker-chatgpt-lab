from flask import Flask,request
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_KEY')

def generate_code_from_content(language, content):
    code = f"{language} code generated from  content : {content}"
    return code


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/chatgpt')
def chatgpt():
    args = request.args
    message = args.get("message")
    print(message)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return completion['choices'][0]['message']['content']

@app.route('/code')
def personal_chatgpt():
    args = request.args
    message =args.get("message")
    language =args.get("language")
    demande = f"Write{message} in {language}"
    print(message)
    print(language)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": demande}]
    )
    return completion['choices'][0]['message']['content']
