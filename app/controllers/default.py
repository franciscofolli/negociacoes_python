from app import app

@app.route('/') # Define Rotas para serem executadas / Embrulho --> descorador --> Wrap
# e logo a seguir as requisições permitidas em determinada rota 
def index():#Chamada de função que ira ser executada ao utilizar a Rota
    return "Hello World"