const express = require('express');
const router = express.Router();
const db = require('../config/db');

// Ruta para agregar una calificación
router.post('/', (req, res) => {
    const { id_partido, id_jugador_calificado, id_jugador, puntuacion, comentario } = req.body;

    // Paso 1: Insertar la calificación
    const insertarCalificacion = `
        INSERT INTO Calificaciones (id_partido, id_jugador_calificado, id_jugador, puntuacion, comentario)
        VALUES (?, ?, ?, ?, ?)
    `;

    db.query(insertarCalificacion, [id_partido, id_jugador_calificado, id_jugador, puntuacion, comentario], (err) => {
        if (err) {
            console.error('Error al insertar calificación:', err);
            return res.status(500).send('Error al agregar calificación');
        }

        // Paso 2: Calcular el promedio de todas las calificaciones de ese jugador
        const obtenerPromedioCalificaciones = `
            SELECT AVG(puntuacion) AS promedio
            FROM Calificaciones
            WHERE id_jugador_calificado = ?
        `;

        db.query(obtenerPromedioCalificaciones, [id_jugador_calificado], (err, result) => {
            if (err) {
                console.error('Error al calcular promedio de calificaciones:', err);
                return res.status(500).send('Error al calcular promedio');
            }

            const promedio = result[0].promedio;

            // Paso 3: Actualizar la puntuación del jugador en la tabla Jugadores
            const actualizarPuntuacionJugador = `
                UPDATE Jugadores
                SET puntuacion = ?
                WHERE id_jugador = ?
            `;

            db.query(actualizarPuntuacionJugador, [promedio, id_jugador_calificado], (err) => {
                if (err) {
                    console.error('Error al actualizar la puntuación del jugador:', err);
                    return res.status(500).send('Error al actualizar puntuación');
                }

                // Redirigir después de que se haya guardado la calificación y actualizado el promedio
                res.redirect(`/calificar_partido?id_partido=${id_partido}&id_jugador=${id_jugador}`);
            });
        });
    });
});

module.exports = router;
