const express = require('express');
const router = express.Router();
const db = require('../config/db');

// Ruta para eliminar una infracción
router.post('/', (req, res) => {
    const idInfraccion = req.body.id_infraccion;

    const eliminarInfraccion = 'DELETE FROM Infracciones WHERE id_infraccion = ?';

    db.query(eliminarInfraccion, [idInfraccion], (err) => {
        if (err) {
            console.error('Error al eliminar la infracción:', err);
            return res.status(500).send('Error al eliminar la infracción');
        }
        
        res.send(`
            <script>
                alert("La infracción ha sido eliminada con éxito.");
                window.location.href = '/';
            </script>
        `);
    });
});

module.exports = router;
