const express = require('express');
const router = express.Router();
const db = require('../config/db');

router.post('/', (req, res) => {
    try {
        const equipo_1 = JSON.parse(req.body.equipo1);
        const equipo_2 = JSON.parse(req.body.equipo2);
        const nombre_equipo_1 = req.body.nombreEquipo1;
        const nombre_equipo_2 = req.body.nombreEquipo2;
        const fecha = req.body.fecha;

        const crear_partido = 'INSERT INTO Partidos (fecha) VALUES (?)';

        db.query(crear_partido, [fecha], (err, result) => {
            if (err) {
                console.error('Error al crear el partido:', err);
                return res.status(500).send('Error al crear el partido');
            }

            const id_partido = result.insertId;

            const crear_equipo = 'INSERT INTO Equipos (nombre, id_partido) VALUES (?, ?)';

            // Crear equipo 1
            db.query(crear_equipo, [nombre_equipo_1, id_partido], (err, result) => {
                if (err) {
                    console.error('Error al crear el equipo 1:', err);
                    return res.status(500).send('Error al crear el equipo 1');
                }

                const id_equipo_1 = result.insertId;

                // Crear equipo 2
                db.query(crear_equipo, [nombre_equipo_2, id_partido], (err, result) => {
                    if (err) {
                        console.error('Error al crear el equipo 2:', err);
                        return res.status(500).send('Error al crear el equipo 2');
                    }

                    const id_equipo_2 = result.insertId;

                    const jugador_equipo = 'INSERT INTO Jugador_Equipo (id_equipo, id_jugador) VALUES (?, ?)';
                    const notificacion = 'INSERT INTO Notificaciones (id_jugador, contenido, fecha_partido) VALUES (?, ?, ?)';

                    // Asociar jugadores al equipo 1 y crear notificaciones
                    equipo_1.forEach(jugador => {
                        const id_jugador = jugador.id_jugador;
                        const mensaje = `Has sido asignado al equipo ${nombre_equipo_1}`;

                        db.query(jugador_equipo, [id_equipo_1, id_jugador], (err) => {
                            if (err) {
                                console.error('Error al insertar jugador en el equipo 1:', err);
                            }
                        });

                        db.query(notificacion, [id_jugador, mensaje, fecha], (err) => {
                            if (err) {
                                console.error('Error al insertar notificación para el jugador:', err);
                            }
                        });
                    });

                    equipo_2.forEach(jugador => {
                        const id_jugador = jugador.id_jugador;
                        const mensaje = `Has sido asignado al equipo ${nombre_equipo_2}`;

                        db.query(jugador_equipo, [id_equipo_2, id_jugador], (err) => {
                            if (err) {
                                console.error('Error al insertar jugador en el equipo 2:', err);
                            }
                        });

                        db.query(notificacion, [id_jugador, mensaje, fecha], (err) => {
                            if (err) {
                                console.error('Error al insertar notificación para el jugador:', err);
                            }
                        });
                    });

                    // Enviar un alert al navegador y redirigir
                    res.send(`
                        <script>
                            alert('Partido creado con éxito.');
                            window.location.href = '/';
                        </script>
                    `);
                });
            });
        });
    } catch (err) {
        console.error('Error al procesar los datos:', err);
        return res.status(400).send('Datos inválidos.');
    }
});


module.exports = router;
