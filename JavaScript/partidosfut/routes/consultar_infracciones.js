const express = require('express');
const router = express.Router();
const db = require('../config/db');

// Ruta para obtener los partidos y las infracciones del jugador
router.post('/', (req, res) => {
    const id_usuario = req.body.id_usuario; // Recibimos el id del jugador desde el formulario

    // Consulta para obtener los partidos y las infracciones
    const queryPartidos = `
        SELECT 
            Equipo1.nombre As NombreEquipo1,
            Equipo2.nombre As NombreEquipo2,
            Partidos.fecha,
            Usuarios.nombre,
            Infracciones.descripcion
        FROM Partidos
        INNER JOIN Equipos AS Equipo1 ON Partidos.id_partido = Equipo1.id_partido
        INNER JOIN Equipos AS Equipo2 ON Partidos.id_partido = Equipo2.id_partido
        INNER JOIN Jugador_Equipo ON Equipo1.id_equipo  = Jugador_Equipo.id_equipo
        INNER JOIN Jugadores ON Jugador_Equipo.id_jugador = Jugadores.id_jugador 
        INNER JOIN Usuarios ON Jugadores.id_usuario = Usuarios.id_usuario
        INNER JOIN Infracciones ON Jugadores.id_jugador = Infracciones.id_jugador 
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
        console.log(results)
        res.render('consultar_infracciones', { partidos: results });
    });
});

module.exports = router;
