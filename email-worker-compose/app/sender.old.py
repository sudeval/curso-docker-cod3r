import psycopg2
# com o worker e redis nao vai mais ser utilizado o route e run, apenas Bottle
from bottle import route, run, request
#from bottle import Bottle, request

# data source naming / db (nome do serviço) no host é para evitar definir um IP.
DSN = 'dbname=email_sender user=postgres host=db'
SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'

def register_message(assunto, mensagem):
    conn = psycopg2.connect(DSN)
    cursor = conn.cursor()
    cursor.execute(SQL, (assunto, mensagem))
    conn.commit()
    cursor.close()
    conn.close()

    print('Mensagem registrada  !')

@route('/', method='POST')
def send():
    # assunto e mensagens são os campos (name) existente no formulario
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')

    register_message(assunto, mensagem)
    return 'Mensagens enfileirada ! Assunto: {} Mensagem: {}'.format(
        assunto, mensagem
    )

# se for o arquivo principal, rodando na 8080
if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)