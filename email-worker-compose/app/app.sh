#!/bin/sh
# instalando o framework bottle
# pip install bottle==0.12.13
# adicionando a dependencia do banco (psycopg2)
# o curso recomenda a versao 2.7.1, mas tive problema com a instalacao dela.
pip install bottle==0.12.13 psycopg2==2.7.4
python -u sender.py