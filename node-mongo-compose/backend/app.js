const express = require('express');
const restful = require('node-restful')
const server = express();
const mongoose = restful.mongoose;

const bodyParser = require('body-parser')
// devido o backend ser executado em serv/porta diferente
const cors = require('cors')


// database - substituindo a API de promise do mongoose (deprecated) pela do node.
mongoose.Promise = global.Promise;

// server(db)/banco(mydb)
mongoose.connect('mongodb://db/mydb')

// Middlewares / filtros (parser do conteudo da requisicao - formato: urlencoded)
server.use(bodyParser.urlencoded({extended:true}))
server.use(bodyParser.json())
server.use(cors())

// teste (apenas responde backend)
// server.get('/', (req, res, next) => res.send('Backend'))

// ODM (entidade Cliente com apenas um atributo)
const Client = restful.model('Client', {
    name: { type: String, required: true }
})

// Rest API
// vai fazer a parte de persistencia com o mongoose e as rotas com o express
Client.methods(['get', 'post', 'put', 'delete'])
Client.updateOptions({new: true, runValidators: true})

// Routes
Client.register(server, '/clients')

// start server (porta 3000)
server.listen(3000)