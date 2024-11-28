const express = require('express');
const router = express.Router();
const db = require('../config/db');

router.post('/', (req, res) => {
  const id_usuario = req.body.id_usuario;  // Obtener el id_usuario de la solicitud
  const suscripcion = req.body.suscripcion;
  
  if (!id_usuario) {
    return res.status(400).json({ success: false, message: 'No se encuentra el id_usuario en la solicitud' });
  }
  
  // Consulta para obtener el id_jugador y el campo es_solidario a partir del id_usuario
  const queryJugador = 'SELECT id_jugador, es_solidario, model_sel FROM Jugadores WHERE id_usuario = ?';
  
  db.query(queryJugador, [id_usuario], (err, results) => {
    if (err) {
      console.error('Error al obtener id_jugador:', err);
      return res.status(500).json({ success: false, message: 'Error al obtener el id_jugador' });
    }
    
    if (results.length === 0) {
      return res.status(404).json({ success: false, message: 'Jugador no encontrado para este usuario' });
    }
    
    const id_jugador = results[0].id_jugador;
    const es_solidario = results[0].es_solidario;
    const currentModelSel = results[0].model_sel;  // El valor actual de model_sel
    
    if (es_solidario === 1 && suscripcion === 'FRECUENTE') {
      // Si es jugador solidario y quiere cambiar a FRECUENTE
      return res.status(400).json({ 
        success: false, 
        message: 'No puedes cambiar a FRECUENTE, tienes muchas infracciones. Actualmente eres un jugador solidario.',
        currentModelSel // Devolver el modelo actual para mantenerlo seleccionado en el frontend
      });
    }
    
    let queryActualizar;
    let parametros;
    
    if (suscripcion === 'NO DISPONIBLE') {
      // Si se selecciona "NO DISPONIBLE", actualizar el campo 'disponible' a 0
      queryActualizar = 'UPDATE Jugadores SET disponible = 0 WHERE id_jugador = ?';
      parametros = [id_jugador];
    } else if (suscripcion === 'OCASIONAL' || suscripcion === 'FRECUENTE') {
      // Si se selecciona "OCASIONAL" o "FRECUENTE", actualizar 'model_sel' y 'disponible'
      queryActualizar = 'UPDATE Jugadores SET model_sel = ?, disponible = 1 WHERE id_jugador = ?';
      parametros = [suscripcion, id_jugador];
    } else {
      return res.status(400).json({ success: false, message: 'Suscripción no válida', currentModelSel });
    }

    // Ejecutar la actualización en la base de datos
    db.query(queryActualizar, parametros, (err) => {
      if (err) {
        console.error('Error al actualizar la suscripción:', err);
        return res.status(500).json({ success: false, message: 'Error al actualizar la suscripción', currentModelSel });
      }
      
      res.json({ success: true, message: 'Suscripción actualizada correctamente' });
    });
  });
});

module.exports = router;
