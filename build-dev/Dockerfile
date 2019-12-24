FROM python:3.6
LABEL maintainer 'Curso Cod3r'

# concatenando para ficar em uma unica layer
RUN useradd www && \
    mkdir /app && \
    mkdir /log && \
    chown www /log

USER www
VOLUME /log
WORKDIR /app
EXPOSE 8080

# o que ele vai fazer ao entrar/iniciar
ENTRYPOINT [ "/usr/local/bin/python" ]
CMD [ "run.py" ]
# sudo docker image build -t ex-build-dev . 
# -it modo interativo ( para ver no console os logs )
# -v mapear o valume para o diretorio corrente (run.py) ser lido a partir do app
# -p mapear a porta interna 8080 para ser lida a partir da 80 (remapear)
# --name nome para o container
# ex-build-dev nome da imagem
# sudo docker container run -it -v $(pwd):/app -p 80:8000 --name python-server ex-build-dev
# container para ler o log gerado (atraves dos volumes mapeado em python-server)
# coloquei nome errado por engano na imagem htpp-server.log no lugar de http-server.log
# sudo docker container run -it --volumes-from=python-server debian cat /log/htpp-server.log