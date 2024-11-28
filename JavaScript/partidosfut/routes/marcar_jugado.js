const express = require('express');
const router = express.Router();
const db = require('../config/db');

router.post('/', (req, res) => {
    const id_partido = req.body.id_partido;
    const jugado = 'UPDATE Partidos SET estado = "JUGADO" WHERE id_partido = ?';

    db.query(jugado, [id_partido], (error, results) => {
        if (error) {
            console.error('Error al actualizar el estado del partido:', error);
            return res.status(500).send('<script>alert("Error al marcar el partido como jugado."); window.history.back();</script>');
        }

        // Enviar respuesta con un alert y recargar la página
        res.send(`
            <script>
                alert("El partido ha sido marcado como jugado.");
                window.location.href = "/";
            </script>
        `);
    });
});

module.exports = router;
