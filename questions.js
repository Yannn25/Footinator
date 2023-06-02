const { pool } = require('./database');

async function getQuestions() {
    const res = await pool.query('SELECT * FROM questions');
    return res.rows;
}

module.exports = { getQuestions };