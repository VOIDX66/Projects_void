const express = require('express');
const router = express.Router();
const db = require('../config/db');

// Ruta para obtener los partidos y las infracciones del jugador
router.post('/', (req, res) => {
    const id_usuario = req.body.id_usuario; // Recibimos el id del jugador desde el formulario

    // Consulta para obtener los partidos y las infracciones
    const queryPartidos = `
        SELECT 
            Partidos.fecha,
            Usuarios.nombre AS NombreUsuario,
            Infracciones.descripcion,
            Equipo1.nombre AS NombreEquipo1,
            Equipo2.nombre AS NombreEquipo2
        FROM Infracciones
        INNER JOIN Partidos ON Infracciones.id_partido = Partidos.id_partido
        INNER JOIN Jugadores ON Infracciones.id_jugador = Jugadores.id_jugador
        INNER JOIN Usuarios ON Jugadores.id_usuario = Usuarios.id_usuario
        LEFT JOIN Equipos AS Equipo1 ON Partidos.id_partido = Equipo1.id_partido
        LEFT JOIN Equipos AS Equipo2 ON Partidos.id_partido = Equipo2.id_partido
        WHERE Usuarios.id_usuario = ?
        AND Equipo1.id_equipo < Equipo2.id_equipo
        ORDER BY Partidos.fecha DESC
    `;

    db.query(queryPartidos, [id_usuario], (err, results) => {
        if (err) {
            console.error('Error en la base de datos:', err);
            return res.status(500).send('Error al obtener los partidos e infracciones');
        }

        // Renderizamos la vista pasando la lista de partidos e infracciones
        res.render('consultar_infracciones', { partidos: results });
    });
});

module.exports = router;
