const express = require('express');
const ejs = require('ejs');
const app = express();
const pool = require('./database');
app.set('view engine', 'ejs');
const PORT = 3000;

app.use(express.static('public'));
app.use(express.urlencoded({ extended: true })); // Middleware pour parser les données du corps de la requête
app.get('/', (req, res) => {
    res.render('Chatbot.ejs', { showButtons: false });
});

app.post('/', async (req, res) => {
    if (req.body.commencer) {
        try {
            const result = await pool.query('SELECT * FROM questions ORDER BY RANDOM() LIMIT 1');
            const liaison = result.rows[0].liaison;
            const question = result.rows[0].question;
            const resultLiaison = await pool.query(`SELECT ${liaison} FROM joueurs ORDER BY RANDOM() LIMIT 1`);
            const joueur = resultLiaison.rows[0][liaison];
            let full = "";
            if (liaison == "age") {
                full = "ans?";
            }
            else {
                full = "?";
            }
            const resultat = question + joueur + full;
            res.render('Chatbot.ejs', { showButtons: true, question: resultat });
        } catch (err) {
            console.error(err);
            res.status(500).send("Erreur lors de la récupération des données");
        }
    } else {
        res.render('Chatbot.ejs', { showButtons: false });
    }
});

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});