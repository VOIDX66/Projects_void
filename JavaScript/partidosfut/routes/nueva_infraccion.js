const express = require('express');
const router = express.Router();
const db = require('../config/db');

router.post('/', (req, res) => {
    const idJugador = req.body.id_jugador;
    const idPartido = req.body.id_partido;
    const nombreJugador = req.body.nombre;
    res.render('nueva_infraccion', {idJugador, idPartido, nombreJugador});
});

module.exports = router;