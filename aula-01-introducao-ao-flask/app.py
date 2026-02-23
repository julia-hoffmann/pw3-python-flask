#importando o flask para a aplicacao
from flask import Flask, render_template
#carregando Flask na variavel "app"
#declarando variavel python
app = Flask(__name__, template_folder='views') #variaveis com dois _ são variaveis de ambiente do pyhton
# __name__ representa o nome da aplicação ou seja __name__ = app.py
  
  #criando a rota principal do site
@app.route('/')
  #def cria funcoes no python
def home():
  return render_template('index.html')
#iniciando servidor(tipo xampp) na porta 5000



@app.route('/games')
def games():
  return render_template('games.html')


@app.route('/consoles')
def consoles():
  return render_template('consoles.html')


if __name__ =='__main__': #verifica se o arquivo em __name__ é o principal 
    app.run(port=5000, debug=True)
# .run() inicia 

