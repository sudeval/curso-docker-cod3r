import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
    r = redis.Redis(host='queue', port=6379, db=0)
    print('Aguardando mensagens ...')
    # laço infinito para consumir as mensagens
    while True:
        # pegando a mensagem dentro da fila 'sender'
        mensagem = json.loads(r.blpop('sender')[1])
        # simulando envio do email
        print('Mandando a mensagem:', mensagem['assunto'])
        sleep(randint(15, 45))
        print('Mensagem:', mensagem['assunto'], 'enviada')