const express = require('express');
const router = express.Router();
const db = require('../config/db');

router.post('/', (req, res) => {
    const idUsuario = req.session.user.id_usuario; // Asumiendo que usas sesiones para identificar al usuario
    const nombreJugador = req.session.user.nombre;

    // Consulta para obtener los partidos no jugados
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
        WHERE Equipo1.id_equipo < Equipo2.id_equipo
        AND Partidos.estado != "JUGADO"
        ORDER BY Partidos.fecha DESC;
    `;

    // Consulta para verificar en qué partidos está inscrito el jugador y qué equipo tiene
    const queryJugadorEnEquipo = `
        SELECT je.id_equipo, j.id_jugador, p.id_partido, 
               e.nombre AS nombre_equipo, je.id_equipo AS equipo_id
        FROM Jugador_Equipo je
        INNER JOIN Equipos e ON je.id_equipo = e.id_equipo
        INNER JOIN Partidos p ON e.id_partido = p.id_partido
        INNER JOIN Jugadores j ON je.id_jugador = j.id_jugador
        INNER JOIN Usuarios u ON j.id_usuario = u.id_usuario
        WHERE u.id_usuario = ?
    `;

    // Obtener todos los partidos no jugados
    db.query(queryPartidos, (errorPartidos, resultsPartidos) => {
        if (errorPartidos) {
            console.error('Error al obtener los partidos:', errorPartidos);
            return res.status(500).send('Error al obtener los partidos');
        }

        // Verificar en qué partidos está inscrito el jugador y qué equipo tiene
        db.query(queryJugadorEnEquipo, [idUsuario], (errorJugador, resultsJugador) => {
            if (errorJugador) {
                console.error('Error al verificar participación del jugador:', errorJugador);
                return res.status(500).send('Error al verificar participación del jugador');
            }

            // Crear un array de los id_partido donde el jugador está inscrito
            const partidosJugador = resultsJugador.map(row => ({
                id_partido: row.id_partido,
                nombre_equipo: row.nombre_equipo,
                equipo_id: row.equipo_id
            }));

            // Mapear los partidos para determinar si el jugador está inscrito y en qué equipo
            const partidos = resultsPartidos.map(partido => {
                const jugadorEnPartido = partidosJugador.find(jugador => jugador.id_partido === partido.id_partido);
                return {
                    ...partido,
                    estaEnPartido: !!jugadorEnPartido,
                    equipoJugador: jugadorEnPartido ? jugadorEnPartido.nombre_equipo : null
                };
            });

            // Renderizar la vista con los partidos y la información de participación
            res.render('gestionar_participacion', { 
                jugador: nombreJugador, 
                idUsuario, 
                partidos 
            });
        });
    });
});

// Exportar el router
module.exports = router;
