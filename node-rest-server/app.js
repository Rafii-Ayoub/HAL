const express = require('express');
const app = express();
const cors = require('cors');
const port = process.env.PORT || 5000
const coauthors = require('./data/coauthors.json');
const publications = require('./data/publications.json');
const authors_info = require('./data/authors_info.json');
const publications_info = require('./data/publications_info.json');
const listic = require('./data/listic.json');

var corsOptions = {
  origin: '*',
  optionsSuccessStatus: 200 // For legacy browser support
}
app.use(cors(corsOptions));
app.listen(port, () => {
  console.log('====================================');
  console.log(`Server up, listening on port ${port}`);
  console.log('====================================');
});



app.get('/coauthors', function(req, res) {
  res.json(coauthors);
});

app.get('/publications', function(req, res) {
  res.json(publications);
});

app.get('/authors_info', function(req, res) {
  res.json(authors_info);
});

app.get('/publications_info', function(req, res) {
  res.json(publications_info);
});
app.get('/listic', function(req, res) {
  res.json(listic);
});