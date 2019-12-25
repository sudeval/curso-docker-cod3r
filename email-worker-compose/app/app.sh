#!/bin/sh
# instalando o framework bottle
# pip install bottle==0.12.13
# adicionando a dependencia do banco (psycopg2)
pip install bottle==0.12.13 psycopg2==2.7.1
python -u sender.py