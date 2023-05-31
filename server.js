const express = require('express');
const ejs = require('ejs');
const app = express();
const pool = require('./database');
app.set('view engine', 'ejs');
const PORT = 3000;

app.use(express.static('public'));
app.get('/', (req, res) => {
    res.render('Chatbot.ejs', { showButtons: false });
});

app.post('/', (req, res) => {
    res.render('Chatbot.ejs', { showButtons: true });
});

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});