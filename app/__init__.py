from flask import Flask # importação das bibliotecas de Flask

app = Flask(__name__) #Instância para que o Flask funcione / Objeto

from app.controllers import default #chamando controle padrão para direcionar para a pagina inicial

