const express = require('express');
const router = express.Router();
const db = require('../config/db');


router.post('/', (req, res) => {
    // Aquí puedes procesar el ID y redirigir o responder
    const idJugador =  req.body.id_jugador
    const nombreJugador = req.body.nombre
    const query = 'SELECT * FROM Jugadores '
    + 'INNER JOIN Infracciones ON Jugadores.id_jugador = Infracciones.id_jugador '
    + 'INNER JOIN Partidos ON Infracciones.id_partido = Partidos.id_partido '
    + 'WHERE Jugadores.id_jugador = ?'

    db.query(query, [idJugador], (error, results) => {
        if (error) {
            console.error('Error al ejecutar la consulta:', error);
        } else {
            res.render('gestionar_infracciones', { jugador : results[0], idJugador, nombreJugador }); // Renderiza la vista o responde con datos
        }
    });

    
});

module.exports = router;