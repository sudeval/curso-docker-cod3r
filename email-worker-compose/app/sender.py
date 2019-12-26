import psycopg2
import redis
import json
# com o worker e redis nao vai mais ser utilizado o route e run, apenas Bottle
# from bottle import route, run, request
from bottle import Bottle, request


# sender herdando de Bottle
class Sender(Bottle):

    def __init__(self):
        super().__init__()
        # fazendo o que era feito com @route
        self.route('/', method='POST', callback=self.send)
        # host é o nome do serviço queue
        self.fila = redis.StrictRedis(host='queue', port=6379, db=0)

        # data source naming / db (nome do serviço) no host é para evitar definir um IP.
        DSN = 'dbname=email_sender user=postgres host=db'
        self.conn = psycopg2.connect(DSN)

    def register_message(self, assunto, mensagem):
        SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'
        cursor = self.conn.cursor()
        cursor.execute(SQL, (assunto, mensagem))
        self.conn.commit()
        cursor.close()

        msg = {'assunto': assunto, 'mensagem': mensagem}
        self.fila.rpush('sender', json.dumps(msg))

        print('Mensagem registrada  !')

    # @route('/', method='POST')
    def send(self):
        # assunto e mensagens são os campos (name) existente no formulario
        assunto = request.forms.get('assunto')
        mensagem = request.forms.get('mensagem')

        self.register_message(assunto, mensagem)
        return 'Mensagens enfileirada ! Assunto: {} Mensagem: {}'.format(
            assunto, mensagem
        )

# se for o arquivo principal, rodando na 8080
if __name__ == '__main__':
    sender = Sender()
    sender.run(host='0.0.0.0', port=8080, debug=True)