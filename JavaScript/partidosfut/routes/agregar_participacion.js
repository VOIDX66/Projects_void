const express = require('express');
const router = express.Router();
const db = require('../config/db');

// Ruta para agregar a un jugador a un partido
router.post('/', (req, res) => {
    const id_partido = req.body.id_partido;
    const id_usuario = req.session.user.id_usuario;

    // Obtener el ID del jugador a partir del ID del usuario
    const queryJugador = `SELECT id_jugador FROM Jugadores WHERE id_usuario = ?`;
    db.query(queryJugador, [id_usuario], (errJugador, resultsJugador) => {
        if (errJugador || resultsJugador.length === 0) {
            return res.status(500).json({ error: 'Error al obtener el jugador.' });
        }
        const id_jugador = resultsJugador[0].id_jugador;

        // Verificar cuántos jugadores hay en los equipos del partido
        const queryEquipos = `
            SELECT e.id_equipo, e.nombre, COUNT(je.id_jugador) AS num_jugadores
            FROM Equipos e
            LEFT JOIN Jugador_Equipo je ON e.id_equipo = je.id_equipo
            WHERE e.id_partido = ?
            GROUP BY e.id_equipo
        `;
        db.query(queryEquipos, [id_partido], (errEquipos, resultsEquipos) => {
            if (errEquipos) {
                return res.status(500).json({ error: 'Error al verificar equipos.' });
            }

            // Buscar un equipo con espacio disponible (menos de 5 jugadores)
            const equipoDisponible = resultsEquipos.find(equipo => equipo.num_jugadores < 5);

            if (equipoDisponible) {
                // Agregar al jugador al equipo con espacio disponible
                const queryAgregar = `
                    INSERT INTO Jugador_Equipo (id_equipo, id_jugador) VALUES (?, ?)
                `;
                db.query(queryAgregar, [equipoDisponible.id_equipo, id_jugador], (errAgregar) => {
                    if (errAgregar) {
                        return res.status(500).json({ error: 'Error al agregar al jugador al equipo.' });
                    }
                    return res.status(200).json({ message: `Te has unido al equipo ${equipoDisponible.nombre}.` });
                });
            } else {
                // Si no hay espacio, buscar un jugador solidario para reemplazar
                const querySolidarios = `
                    SELECT je.id_jugador, e.id_equipo, e.nombre AS enombre, u.nombre AS nombre_solidario
                    FROM Jugador_Equipo je
                    INNER JOIN Equipos e ON je.id_equipo = e.id_equipo
                    INNER JOIN Jugadores j ON je.id_jugador = j.id_jugador
                    INNER JOIN Usuarios u ON j.id_usuario = u.id_usuario
                    WHERE e.id_partido = ? AND j.es_solidario = 1
                `;
                db.query(querySolidarios, [id_partido], (errSolidarios, resultsSolidarios) => {
                    if (errSolidarios) {
                        return res.status(500).json({ error: 'Error al buscar jugadores solidarios.' });
                    }

                    if (resultsSolidarios.length > 0) {
                        const jugadorSolidario = resultsSolidarios[0];

                        // Reemplazar al jugador solidario
                        const queryReemplazar = `
                            UPDATE Jugador_Equipo
                            SET id_jugador = ?
                            WHERE id_jugador = ? AND id_equipo = ?
                        `;
                        db.query(queryReemplazar, [id_jugador, jugadorSolidario.id_jugador, jugadorSolidario.id_equipo], (errReemplazar) => {
                            if (errReemplazar) {
                                return res.status(500).json({ error: 'Error al reemplazar al jugador solidario.' });
                            }

                            // Agregar notificación al jugador solidario reemplazado
                            const queryNotificacion = `
                                INSERT INTO Notificaciones (id_jugador, contenido) 
                                VALUES (?, ?)
                            `;
                            const mensaje = `Has sido reemplazado en un partido por otro jugador.`;
                            db.query(queryNotificacion, [jugadorSolidario.id_jugador, mensaje], (errNotificacion) => {
                                if (errNotificacion) {
                                    return res.status(500).json({ error: 'Error al enviar notificación.' });
                                }
                                return res.status(200).json({ message: `Te has unido al equipo ${jugadorSolidario.enombre}. Has reemplazado a un jugador solidario.` });
                            });
                        });
                    } else {
                        // No hay espacio ni jugadores solidarios
                        return res.status(400).json({ error: 'No hay cupos disponibles en el partido ni jugadores solidarios.' });
                    }
                });
            }
        });
    });
});

module.exports = router;
