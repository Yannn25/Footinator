// database.js

const { Pool } = require('pg');

const pool = new Pool({
    user: 'olivier',
    host: 'localhost',
    database: 'footinator',
    password: 'olivier',
    port: 5432,
});

module.exports = pool;