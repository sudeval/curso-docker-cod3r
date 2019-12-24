from bottle import route, run, request

@route('/', method='POST')
def send():
    # assunto e mensagens são os campos (name) existente no formulario
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')
    return 'Mensagens enfileirada ! Assunto: {} Mensagem: {}'.format(
        assunto, mensagem
    )

# se for o arquivo principal, rodando na 8080
if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)