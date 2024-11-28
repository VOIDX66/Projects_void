const express = require('express');
const router = express.Router();
const db = require('../config/db');

// Obtener los partidos
router.post('/', (req, res) => {
    const query = `
        SELECT Partidos.id_partido, Partidos.fecha, Partidos.estado, 
               GROUP_CONCAT(Equipos.nombre SEPARATOR ' vs ') AS equipos
        FROM Partidos
        INNER JOIN Equipos ON Partidos.id_partido = Equipos.id_partido
        GROUP BY Partidos.id_partido
    `;
    db.query(query, (err, results) => {
        if (err) {
            console.error('Error en la base de datos:', err);
            return res.status(500).send('Error al obtener el historial de partidos');
        }
        res.render('ver_historial_partidos', { partidos: results });
    });
});

// Marcar un partido como jugado
router.post('/marcar_jugado', (req, res) => {
    const { id_partido } = req.body;
    const updateQuery = `UPDATE Partidos SET estado = 'Jugado' WHERE id_partido = ? AND estado = 'Confirmado'`;

    db.query(updateQuery, [id_partido], (err, result) => {
        if (err) {
            console.error('Error al actualizar el estado del partido:', err);
            return res.status(500).send('Error al marcar el partido como jugado');
        }
        res.redirect('/historial');
    });
});

module.exports = router;
