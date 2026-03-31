# Importando o Flask para a aplicação
from flask import render_template, request, redirect, url_for

#criando a funcao principla para inicializar as rotas
def init_app(app):
    
    listaConsoles = ['game of trones', 'the office ', 'bridgerton', 'carandiru']
    
    listaGames = [{"filme" : "game of trones", "faixaetaria": "+18", "genero": "fantasia"}]
      
    @app.route('/')
        # def cria funções no Python
    def home():
            return render_template('index.html')


    @app.route('/usuarios')
    def usuarios():
            # Criando variáveis para a rota de games
            filme = "bridgerton"
            genero = "drama de epoca"
            faixaetaria = "+16"

          
            # Enviando as variáveis para o HTML
            return render_template('usuarios.html',
                                filme=filme,
                                genero=genero,
                                faixaetaria=faixaetaria,
                               )


    @app.route('/consoles', methods=['GET' , 'POST'])
    def consoles():
            # Criando um objeto
            console = {"Nome": "",
                    "Fabricante": "Sony",
                    "Ano": 2000}
          
            
            #recebendo o valor do formulario
            if request.method == 'POST':
                if request.form.get('novofilme'):
                    listaConsoles.append(request.form.get
                    ('novofilme'))
                    
            return render_template('consoles.html',
                                console=console, listaConsoles= listaConsoles)    
            
            
            
    @app.route('/cadfilmes', methods=['GET', 'POST'])
    def cadfilmes():
            #recebendo dados e enviando para a pagina
            if request.method == 'POST':
                    #gravar dados na lista
                 listaGames.append({'filme' : request.form.get('filme'), 'genero': request.form.get('genero'), 'faixaetaria' : request.form.get('faixaetaria')})
                 return redirect(url_for('cadfilmes'))
            return render_template('cadfilmes.html',
                                   listaGames = listaGames)