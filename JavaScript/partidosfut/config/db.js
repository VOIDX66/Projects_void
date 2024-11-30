const mysql = require('mysql2');

const db = mysql.createConnection({
    host: '25.56.37.228',
    user: 'userpartidos',
    password: 'upartidos',
    database: 'partidos_db'
});

db.connect((err) => {
    if (err) {
        throw err;
    }
    console.log('Connecting to database');
});

module.exports = db;