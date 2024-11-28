const express = require('express');
const router = express.Router();
const db = require('../config/db');

router.post('/', (req, res) => {
    const idNotificacion = req.body.id;
    //console.log('ID recibido:', idNotificacion); // Verifica el ID recibido

    const marcar = 'UPDATE Notificaciones SET leida = 1 WHERE id_notificacion = ?';

    db.query(marcar, [idNotificacion], (err) => {
        if (err) {
            console.error('Error al marcar la notificación como leída:', err);
            return res.status(500).json({ success: false, message: 'Error al marcar como leída' });
        }
        return res.json({ success: true, message: 'Notificación marcada como leída' });
    });
});


module.exports = router;
