import sqlite3
from sqlite3 import Error

from services.database import db_class


class Cliente:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def incluir(self, sql):
        db_class.cursor.execute(sql, self.nome, self.idade, self.profissao)
        db_class.conn.commit()
