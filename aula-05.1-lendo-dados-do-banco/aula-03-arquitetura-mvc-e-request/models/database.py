# importando o flask 
from flask_sqlalchemy import SQLAlchemy
#carregando o SQLAlchemy em uma variavel
db = SQLAlchemy()
#criando classe para representar a entidade GAMES no banco
#schema
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer) 
    
    # inicalizando as variaveis na classe
    def __init__(self, titulo, ano, categoria, plataforma, preco, quantidade):
         self.titulo = titulo
         self.ano = ano
         self.categoria = categoria
         self.plataforma = plataforma
         self.preco = preco
         self.quantidade = quantidade
         