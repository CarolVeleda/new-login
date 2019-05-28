import psycopg2

class Dao:
    def __init__(self):
        self._conexao = "dbname=funcionario user=postgres password=postgres host=localhost port=5432"
        con = psycopg2.connect(self._conexao)