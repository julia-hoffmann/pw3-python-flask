
# Comentário no Python
# Importando o Flask para a aplicação
from flask import Flask, render_template
# Carregando o Flask na variável "app"
from controlers import routes 
# Declarando variável no Python
app = Flask(__name__, template_folder='views')
# Variáveis com __ são variáveis de ambiente do Python
# __name__ representa o nome da aplicação
# CRIANDO A ROTA PRINCIPAL DO SITE
routes.init_app(app)




# Iniciando o servidor na porta 5000
if __name__ == '__main__':
    # Verificando se o arquivo gravado em __name__ é o arquivo principal
    app.run(port=5000, debug=True)
# O método .run() inicia o servidor