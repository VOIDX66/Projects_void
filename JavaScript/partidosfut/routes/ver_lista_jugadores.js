const express = require('express');
const router = express.Router();
const db = require('../config/db');

router.post('/', (req, res) => {
    const query = 'SELECT * FROM Jugadores INNER JOIN Usuarios ON Jugadores.id_usuario = Usuarios.id_usuario';
    db.query(query, (err, results) => {
        if (err) {
            console.error('Error en la base de datos:', err);
            return res.status(500).send('Error al obtener la lista de jugadores');
        }
        res.render('ver_lista_jugadores', { jugadores: results });
    });
});

module.exports = router;