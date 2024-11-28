const express = require('express');
const router = express.Router();
const db = require('../config/db');

router.post('/', (req, res) => {
    const idJugador = req.body.id_jugador;
    const idPartido = req.body.id_partido;
    const descripcion = req.body.descripcion;
    
    const agregar = 'INSERT INTO Infracciones (id_jugador, id_partido, descripcion) VALUES (?, ?, ?)'

    db.query(agregar, [idJugador, idPartido, descripcion], (err) => {
        if (err) {
            console.error('Error al agregar la infracción:', err);
            return res.status(500).send('Error al agregar la infracción');
        }
        res.send(`
            <script>
                alert("La infracción ha sido agregada con éxito.");
                window.location.href = '/';
            </script>
        `);
    });
});

module.exports = router;