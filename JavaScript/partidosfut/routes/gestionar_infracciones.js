const express = require('express');
const router = express.Router();
const db = require('../config/db');

router.post('/', (req, res) => {
    const idJugador = req.body.id_jugador;
    const nombreJugador = req.body.nombre;

    // Obtener las infracciones del jugador y los partidos asociados
    const queryInfracciones = `
    SELECT DISTINCT
        Jugadores.id_jugador, 
        Usuarios.nombre AS nombreJugador, 
        Infracciones.id_infraccion, 
        Infracciones.descripcion, 
        Partidos.id_partido, 
        Partidos.fecha, 
        Partidos.estado
    FROM Jugadores
    INNER JOIN Usuarios ON Jugadores.id_usuario = Usuarios.id_usuario
    LEFT JOIN Infracciones ON Jugadores.id_jugador = Infracciones.id_jugador
    LEFT JOIN Partidos ON Infracciones.id_partido = Partidos.id_partido
    LEFT JOIN Equipos ON Partidos.id_partido = Equipos.id_partido
    WHERE Jugadores.id_jugador = ?
`;

    // Obtener los partidos en los que el jugador ha jugado
    const queryPartidos = `
        SELECT 
            Partidos.id_partido, 
            Partidos.fecha, 
            Partidos.estado,
            Equipo1.nombre AS equipo_1, 
            Equipo2.nombre AS equipo_2
        FROM Partidos
        INNER JOIN Equipos AS Equipo1 ON Partidos.id_partido = Equipo1.id_partido
        INNER JOIN Equipos AS Equipo2 ON Partidos.id_partido = Equipo2.id_partido
        INNER JOIN Jugador_Equipo ON Jugador_Equipo.id_equipo = Equipo1.id_equipo 
                                    OR Jugador_Equipo.id_equipo = Equipo2.id_equipo
        WHERE Jugador_Equipo.id_jugador = ?
        AND Equipo1.id_equipo < Equipo2.id_equipo
    `;

    // Ejecutar ambas consultas
    db.query(queryInfracciones, [idJugador], (errorInfracciones, resultsInfracciones) => {
        if (errorInfracciones) {
            console.error('Error al obtener las infracciones y partidos:', errorInfracciones);
            return res.status(500).send('Error al obtener las infracciones del jugador');
        }

        // Ejecutar la consulta de partidos
        db.query(queryPartidos, [idJugador], (errorPartidos, resultsPartidos) => {
            if (errorPartidos) {
                console.error('Error al obtener los partidos:', errorPartidos);
                return res.status(500).send('Error al obtener los partidos');
            }

            // Filtrar las infracciones (si existen) y los partidos en los que el jugador ha jugado
            const infracciones = resultsInfracciones.filter(result => result.id_infraccion);
            const partidos = resultsPartidos;  // Solo los partidos en los que el jugador ha jugado

            // Renderizar la vista con los datos correspondientes
            res.render('gestionar_infracciones', { 
                jugador: nombreJugador, 
                idJugador, 
                infracciones: infracciones,
                partidos: partidos  // Solo los partidos en los que el jugador ha jugado
            });
        });
    });
});

module.exports = router;
