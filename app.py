from flask import Flask

app = Flask(__name__)

@app.route('/')
def pagina_simples():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Página Simples</title>
    </head>
    <body>
    <h1>Olá do Cloud Run!</h1>
    <p>Esta é uma página web simples exibida após o curl.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
