from flask import session

session['var']='oi'
app.run()

app.secret_key = 'minha chave' (vai no main, tem q fazer isso antes de dar app.run)

#lista de funcionarios no depto
#objeto de depto no funcionario
#inserir admin no formulario (criar um admin padrao com TRUE ja)
#listar projetos > ver detalhes do projeto > (lista de funcionarios do projeto)
#> check box com os funcionarios, selecionar os funcionarios que quer vincular
#> enviar

#> ver detalhes > desvincular/adicionar
#> tratar erros pra ver se ja tem repetido....


"""
@app.before_first
def before_first_request(): 
    print('ndsjkd')

@app.before_request
def before_request():
    print(request.path)
    print('jdklajskd')


#executa smp qndo da uma exceção
@app.after_request
def after_request(response):
    print('jdklsa')
    return response
"""