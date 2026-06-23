# Importando o Flask para a aplicação
from flask import render_template, request, redirect, url_for
from models.database import Game, db
#criando a funcao principla para inicializar as rotas
def init_app(app):
    
    listaConsoles = ['playstation 5', 'xbox one', 'super nintendo', 'atari', '3DS']
    
    listaGames = [{"'titulo" : "CS-GO", "ano": 2012, "categoria": "FPS online", "plataforma": "PC(window)"}]
      
    @app.route('/')
        # def cria funções no Python
    def home():
            return render_template('index.html')


    @app.route('/games')
    def games():
            # Criando variáveis para a rota de games
            titulo = "Portal 2"
            ano = 2011
            categoria = "Puzzle"
            # Lista de jogadores (uma lista é um vetor/array)
            jogadores = ['Marcos', 'Richard', 'Miguel', 'Renato', 'Pedro']
            # Enviando as variáveis para o HTML
            return render_template('games.html',
                                titulo=titulo,
                                ano=ano,
                                categoria=categoria,
                                jogadores=jogadores)


    @app.route('/consoles', methods=['GET' , 'POST'])
    def consoles():
            # Criando um objeto
            console = {"Nome": "Playstation 2",
                    "Fabricante": "Sony",
                    "Ano": 2000}
          
            
            #recebendo o valor do formulario
            if request.method == 'POST':
                if request.form.get('novofilme'):
                    listaConsoles.append(request.form.get
                    ('novofilme'))
                    
            return render_template('consoles.html',
                                console=console, listaConsoles= listaConsoles)    
            
            
            
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
            #recebendo dados e enviando para a pagina
            if request.method == 'POST':
                    #gravar dados na lista
                 listaGames.append({'titulo' : request.form.get('titulo'), 'ano': request.form.get('ano'), 'categoria' : request.form.get('categoria'), 'plataforma': request.form.get('plataforma')})
                 return redirect(url_for('cadgames'))
            return render_template('cadgames.html',
                                   listaGames = listaGames)
            
    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/delete<int:id>')
    def estoque(id=None):
        #Verificando se o ID foi passado pra rota
        if id:
            game=Game.query.get(id) #Seleciona o jogo
            db.session.delete(game) #Deleta o jogo
            db.session.commit() #Confirma a exclusão
            return redirect(url_for('estoque')) #Redireciona para a página de estoque
            
            
            if request.method == 'POST':
                    
                    dados = request.form.to_dict()
                    newgame = Game(
                            dados['titulo'],
                             dados['ano'],
                              dados['categoria'],
                               dados['plataforma'],
                                dados['preco'],
                                 dados['quantidade'],
                            
                    )
                    db.session.add(newgame)
                    db.session.commit()
                    return redirect(url_for('estoque'))
            games= Game.query.all()
            return render_template('estoque.html', games=games)
    
    
    @app.route('/estoque_consoles', methods=['GET', 'POST'])
    def estoque_consoles():
            
            if request.method == 'POST':
                    
                    dados = request.form.to_dict()
                    newestoqueconsole = estoque_consoles(
                            dados['nome'],
                             dados['ano'],
                              dados['fabricante'],
                                dados['preco'],
                            
                    )
                    db.session.add(newestoqueconsole)
                    db.session.commit()
                    return redirect(url_for('estoque_consoles'))
            newestoqueconsole= estoque_consoles.query.all()
            return render_template('estoque_consoles.html', estoque_consoles = estoque_consoles)
    
    
    @app.route('estoque/editar', methods=['GET', 'POST'])
    def editar():
            return render_template(edtiGame.html)