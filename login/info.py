from flask import session

session['var']='oi'
app.run()

app.secret_key = 'minha chave' (vai no main, tem q fazer isso antes de dar app.run)


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