import psycopg2
from datetime import datetime

class Projeto:
    
    def __init__(self,nome,dataPrevista):
        self._nome = nome
        self._dataPrevista = format(datetime.strptime(str(dataPrevista),"%d/%m/%Y"),"%d/%m/%Y")
        #self._dataPrevista = dataPrevista.srtftime("%d/%m/%Y")

    def _get_nome(self):
        return self._nome
    
    def _get_dataPrevista(self):
        return self._dataPrevista
    
    def _get_id(self):
        return self._id

    def _set_nome(self, nome):
        self._nome = nome
    
    def _set_id(self, id):
        self._id = id
    
    def _set_dataPrevista(self, data):
        self._dataPrevista = datetime.strptime(data,'%d/%m/%Y')
    

    nome = property(_get_nome,_set_nome)
    dataPrevista = property(_get_dataPrevista,_set_dataPrevista)
    id = property(_get_id,_set_id)





class projetoDao:

    def __init__(self):
        self._conexao = "dbname=funcionario user=postgres password=postgres host=localhost port=5432"

    def listar(self):
        con = psycopg2.connect(self._conexao)
        v=[]
        with con as c:
            cursor = c.cursor()
            cursor.execute('select * from projeto')
            for l in cursor.fetchall():
                dt=l[2].strftime("%d/%m/%Y")
                p = Projeto(l[1],dt)
                p.id=int(l[0])
                v.append(p)
            
        cursor.close()
        return v
    

    
    def salvar(self, p):

        verifica=hasattr(p, 'id')

        if (verifica):
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('UPDATE projeto SET nome = %s, dtPrevista = %s WHERE idProjeto = %s',(p.nome,p.dataPrevista,int(p.id)))
                con.commit()
                cursor.close()


        else:
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('insert into projeto (nome,dtPrevista) values (%s,%s) RETURNING idProjeto', (p.nome,p.dataPrevista))
                cod = (cursor.fetchone())[0]
                con.commit()
                p.id = cod
                cursor.close()



    def buscar(self,cod):
        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('SELECT * FROM projeto WHERE idProjeto = %s',[cod])
        l = cursor.fetchone()
        dt=l[2].strftime("%d/%m/%Y")
        p = Projeto(l[1],dt)
        cursor.close()
        return p


    def excluir(self,id):

        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('DELETE FROM projeto WHERE idProjeto = %s',[id])
        con.commit()
        cursor.close()


#p=Projeto("projeto 3","20/06/2019")
pdao=projetoDao()
print(pdao.listar())