const express = require('express');
const router = express.Router();
const db = require('../config/db');


router.post('/', (req, res) => {
    const query = 'SELECT id_jugador, nombre, puntuacion, model_sel FROM Jugadores INNER JOIN Usuarios ON Jugadores.id_usuario = Usuarios.id_usuario '
                + 'WHERE disponible = 1';
    db.query(query, (err, results) => {
        if (err) {
            console.error('Error en la base de datos:', err);
            return res.status(500).send('Error al obtener la lista de jugadores');
        }
        res.render('crear_partido', { jugadores: results }); // Renderiza la lista de jugadores en la vista ver_lista_jugadores.ejs
    });
    
});

module.exports = router;