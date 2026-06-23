# Comentário no Python
# Importando o Flask para a aplicação
from flask import Flask, render_template
# Carregando o Flask na variável "app"

#importar py my sql
import pymysql
#importando sqlalchemy  e model
from models.database import db, Game
#definindo o nome para o banco
DB_NAME = 'thegames' 

from controllers import routes 
# Declarando variável no Python
app = Flask(__name__, template_folder='views')
# Variáveis com __ são variáveis de ambiente do Python
# __name__ representa o nome da aplicação

#passando o nome do banco para o flask
app.config['DATABASE_NAME'] = DB_NAME

#passando  o endercodo banco para o flask-sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://root@localhost/{DB_NAME}"
# CRIANDO A ROTA PRINCIPAL DO SITE
routes.init_app(app)





if __name__ == '__main__':
    #conectando-se ao mysql para criar o banco de dados
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')
            print("o banco está criado")
    except Exception as error:
        print(f"ocorreu um erro {error}")
    finally:
        connection.close()
        
        db.init_app(app=app)
        with app.test_request_context():
            db.create_all()
            
    # Verificando se o arquivo gravado em __name__ é o arquivo principal
    # Iniciando o servidor na porta 5000
    app.run(port=5000, debug=True)
# O método .run() inicia o servidor
