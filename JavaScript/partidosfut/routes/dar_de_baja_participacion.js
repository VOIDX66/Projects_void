const express = require('express');
const router = express.Router();
const db = require('../config/db');

// Ruta para dar de baja a un jugador de un partido
router.post('/', (req, res) => {
    const idPartido = req.body.id_partido;
    const usuario = req.session.user;

    // Consulta para obtener el id_jugador del usuario que hace la solicitud
    const consultaJugador = `
        SELECT id_jugador FROM Jugadores WHERE id_usuario = ?
    `;
    db.query(consultaJugador, [usuario.id_usuario], (errJugador, resultsJugador) => {
        if (errJugador || resultsJugador.length === 0) {
            console.error('Error al obtener el jugador:', errJugador);
            return res.send(`
                <script>
                    alert('Error al obtener el jugador.');
                    window.location.href = '/';
                </script>
            `);
        }
        const idJugador = resultsJugador[0].id_jugador;

        // Consulta para obtener los jugadores disponibles para reemplazo
        const consultaJugadoresDisponibles = `
            SELECT j.id_jugador, u.nombre 
            FROM Jugadores j
            INNER JOIN Usuarios u ON j.id_usuario = u.id_usuario
            WHERE j.id_jugador NOT IN (
                SELECT je.id_jugador
                FROM Jugador_Equipo je
                INNER JOIN Equipos e ON je.id_equipo = e.id_equipo
                WHERE e.id_partido = ?
            )
            AND j.id_jugador != ?  -- Excluir al jugador que se da de baja
        `;
        
        db.query(consultaJugadoresDisponibles, [idPartido, idJugador], (errJugadores, resultsJugadores) => {
            if (errJugadores) {
                return res.send(`
                    <script>
                        alert('Error al obtener jugadores disponibles.');
                        window.location.href = '/';
                    </script>
                `);
            }

            if (resultsJugadores.length === 0) {
                return res.send(`
                    <script>
                        alert('No hay jugadores disponibles para reemplazo.');
                        window.location.href = '/';
                    </script>
                `);
            }

            res.render('dar_de_baja', { 
                jugadoresDisponibles: resultsJugadores, 
                idPartido,
                usuario,
                idJugador
            });
        });
    });
});

// Ruta para procesar la baja y el reemplazo
router.post('/confirmar', (req, res) => {
    const idPartido = req.body.id_partido;
    const idJugador = req.body.id_jugador;  // Jugador que se quiere dar de baja
    const idReemplazo = req.body.id_reemplazo;  // Jugador seleccionado para reemplazo (si existe)

    if (idReemplazo) {
        // Reemplazar al jugador solidario
        const queryReemplazar = `
            UPDATE Jugador_Equipo je
            JOIN Equipos e ON je.id_equipo = e.id_equipo
            SET je.id_jugador = ?
            WHERE je.id_jugador = ? AND e.id_partido = ?
        `;
        db.query(queryReemplazar, [idReemplazo, idJugador, idPartido], (errReemplazar) => {
            if (errReemplazar) {
                return res.send(`
                    <script>
                        alert('Error al reemplazar al jugador.');
                        window.location.href = '/';
                    </script>
                `);
            }

            // Notificar al jugador reemplazado
            const queryNotificacion = `
                INSERT INTO Notificaciones (id_jugador, contenido) 
                VALUES (?, ?)
            `;
            const mensaje = `Has sido asignado a un partido por otro jugador.`;
            db.query(queryNotificacion, [idReemplazo, mensaje], (errNotificacion) => {
                if (errNotificacion) {
                    return res.send(`
                        <script>
                            alert('Error al enviar notificación.');
                            window.location.href = '/';
                        </script>
                    `);
                }

                res.send(`
                    <script>
                        alert('Te has dado de baja y has sido reemplazado.');
                        window.location.href = '/';
                    </script>
                `);
            });
        });
    } else {
        // Eliminar al jugador de Jugador_Equipo
        const queryEliminarJugador = `
            DELETE je
            FROM Jugador_Equipo je
            INNER JOIN Equipos e ON je.id_equipo = e.id_equipo
            WHERE je.id_jugador = ? AND e.id_partido = ?
        `;
        db.query(queryEliminarJugador, [idJugador, idPartido], (errEliminar) => {
            if (errEliminar) {
                return res.send(`
                    <script>
                        alert('Error al eliminar al jugador.');
                        window.location.href = '/';
                    </script>
                `);
            }

            // Registrar infracción
            const queryInfraccion = `
                INSERT INTO Infracciones (id_jugador, id_partido, descripcion) 
                VALUES (?, ?, 'Darse de baja sin reemplazo')
            `;
            db.query(queryInfraccion, [idJugador, idPartido], (errInfraccion) => {
                if (errInfraccion) {
                    return res.send(`
                        <script>
                            alert('Error al registrar la infracción.');
                            window.location.href = '/';
                        </script>
                    `);
                }

                res.send(`
                    <script>
                        alert('Te has dado de baja sin reemplazo, se ha registrado una infracción y el espacio quedó libre.');
                        window.location.href = '/';
                    </script>
                `);
            });
        });
    }
});

module.exports = router;
