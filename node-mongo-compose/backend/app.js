const express = require('express');
const restful = require('node-restful')
const server = express();
const mongoose = restful.mongoose;


// database - substituindo a API de promise do mongoose (deprecated) pela do node.
mongoose.Promise = global.Promise;

// server(db)/banco(mydb)
mongoose.connect('mongodb://db/mydb')


// teste (apenas responde backend)
server.get('/', (req, res, next) => res.send('Backend'))

// start server (porta 3000)
server.listen(3000)