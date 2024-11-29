const express = require('express');
const router = express.Router();
const db = require('../config/db');

// Ruta para calificar jugadores
router.get('/', (req, res) => {
    const idPartido = req.query.id_partido;
    const idJugador = req.query.id_jugador;

    // Consulta para obtener los jugadores del partido
    const consultaJugadores = `
        SELECT 
            Usuarios.nombre AS NombreJugador,
            Jugadores.id_jugador
        FROM Partidos
        INNER JOIN Equipos ON Partidos.id_partido = Equipos.id_partido
        INNER JOIN Jugador_Equipo ON Equipos.id_equipo = Jugador_Equipo.id_equipo
        INNER JOIN Jugadores ON Jugador_Equipo.id_jugador = Jugadores.id_jugador
        INNER JOIN Usuarios ON Jugadores.id_usuario = Usuarios.id_usuario
        WHERE Partidos.id_partido = ?
        AND Partidos.estado = "JUGADO"
    `;

    // Consulta para obtener las calificaciones de un jugador específico para un partido
    const consultaCalificaciones = `
        SELECT 
            Calificaciones.puntuacion,
            Calificaciones.comentario,
            Usuarios.nombre AS Autor,
            Calificaciones.id_jugador_calificado
        FROM Calificaciones
        INNER JOIN Jugadores ON Calificaciones.id_jugador = Jugadores.id_jugador
        INNER JOIN Usuarios ON Jugadores.id_usuario = Usuarios.id_usuario
        WHERE Calificaciones.id_jugador_calificado = ? 
        AND Calificaciones.id_partido = ?
    `;

    // Consulta para verificar si el jugador actual ya calificó a este jugador
    const consultaYaCalifico = `
        SELECT 1 FROM Calificaciones 
        WHERE id_jugador = ? 
        AND id_jugador_calificado = ? 
        AND id_partido = ?
        LIMIT 1
    `;

    // Consulta para obtener el equipo de cada jugador
    const consultaEquipo = `
        SELECT Equipos.nombre AS EquipoCalificado
        FROM Jugador_Equipo
        INNER JOIN Equipos ON Jugador_Equipo.id_equipo = Equipos.id_equipo
        WHERE Jugador_Equipo.id_jugador = ?
    `;

    // Consultar los jugadores
    db.query(consultaJugadores, [idPartido], (err, jugadores) => {
        if (err) {
            console.error('Error al obtener jugadores:', err);
            return res.status(500).send('Error al cargar jugadores');
        }

        // Lista para almacenar jugadores con sus calificaciones
        const jugadoresConCalificaciones = [];
        let procesados = 0;

        // Consultar las calificaciones y equipo de cada jugador
        jugadores.forEach((jugador) => {
            // Verificar si el jugador actual (idJugador) ya ha calificado a este jugador
            db.query(consultaYaCalifico, [idJugador, jugador.id_jugador, idPartido], (err, resultado) => {
                if (err) {
                    console.error('Error al verificar si ya calificó:', err);
                    return res.status(500).send('Error al verificar si ya calificó');
                }

                // Si el resultado tiene una fila, significa que el jugador ya calificó a este jugador
                const yaCalifico = resultado.length > 0;

                // Consultar las calificaciones para este jugador
                db.query(consultaCalificaciones, [jugador.id_jugador, idPartido], (err, calificaciones) => {
                    if (err) {
                        console.error('Error al obtener calificaciones:', err);
                        return res.status(500).send('Error al cargar calificaciones');
                    }

                    // Consultar el equipo del jugador calificado
                    db.query(consultaEquipo, [jugador.id_jugador], (err, equipoCalificado) => {
                        if (err) {
                            console.error('Error al obtener equipo calificado:', err);
                            return res.status(500).send('Error al obtener equipo calificado');
                        }

                        // Almacenar los datos del jugador con sus calificaciones, equipo y si ya calificó o no
                        jugadoresConCalificaciones.push({
                            id_jugador: jugador.id_jugador,
                            NombreJugador: jugador.NombreJugador,
                            calificaciones,  // Las calificaciones específicas de este jugador
                            EquipoCalificado: equipoCalificado[0] ? equipoCalificado[0].EquipoCalificado : 'Desconocido',
                            yaCalifico: yaCalifico, // Si el jugador ya calificó a este jugador
                        });

                        procesados++;
                        // Renderizar la vista cuando se hayan procesado todos los jugadores
                        if (procesados === jugadores.length) {
                            res.render('calificar_jugadores', { jugadores: jugadoresConCalificaciones, idPartido, idJugador });
                        }
                    });
                });
            });
        });

        // Si no hay jugadores que calificar
        if (jugadores.length === 0) {
            res.render('calificar_jugadores', { jugadores: [], idPartido });
        }
    });
});

module.exports = router;
