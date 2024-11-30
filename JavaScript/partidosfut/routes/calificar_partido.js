const express = require('express');
const router = express.Router();
const db = require('../config/db');

router.get('/', (req, res) => {
    const usuario = req.session.user;

    // Consulta para obtener los partidos jugados
    const consultaPartidos = `
        SELECT 
            Partidos.id_partido,
            Partidos.fecha,
            Jugadores.id_jugador
        FROM Usuarios
        INNER JOIN Jugadores ON Usuarios.id_usuario = Jugadores.id_usuario
        INNER JOIN Jugador_Equipo ON Jugadores.id_jugador = Jugador_Equipo.id_jugador
        INNER JOIN Equipos ON Jugador_Equipo.id_equipo = Equipos.id_equipo
        INNER JOIN Partidos ON Equipos.id_partido = Partidos.id_partido
        WHERE Usuarios.id_usuario = ?
        AND Partidos.estado = "JUGADO"
        ORDER BY Partidos.fecha DESC
    `;

    // Consulta para obtener los nombres de los equipos por partido
    const consultaEquipos = `
        SELECT 
            Equipo1.nombre AS NombreEquipo1,
            Equipo2.nombre AS NombreEquipo2
        FROM Equipos AS Equipo1
        INNER JOIN Equipos AS Equipo2 ON Equipo1.id_partido = Equipo2.id_partido
        WHERE Equipo1.id_partido = ?
        AND Equipo1.id_equipo < Equipo2.id_equipo
    `;

    // Obtener partidos jugados
    db.query(consultaPartidos, [usuario.id_usuario], (err, partidos) => {
        if (err) {
            console.error('Error en la base de datos:', err);
            return res.status(500).send('Error al obtener los partidos jugados');
        }
        
        if (partidos.length === 0) {
            // No hay partidos jugados
            return res.render('calificar_partido', { partidos: [], idJugador });
        }
        idJugador = partidos[0].id_jugador;

        // Obtener los nombres de los equipos para cada partido
        const partidosConEquipos = [];
        let procesados = 0;

        partidos.forEach((partido) => {
            db.query(consultaEquipos, [partido.id_partido], (err, equipos) => {
                if (err) {
                    console.error('Error al obtener los equipos:', err);
                    return res.status(500).send('Error al obtener los equipos');
                }

                if (equipos.length > 0) {
                    // Agregar los equipos al partido
                    partidosConEquipos.push({
                        id_partido: partido.id_partido,
                        fecha: partido.fecha,
                        NombreEquipo1: equipos[0].NombreEquipo1,
                        NombreEquipo2: equipos[0].NombreEquipo2,
                    });
                }

                procesados++;
                if (procesados === partidos.length) {
                    // Cuando todas las consultas terminan, renderizar la vista
                    res.render('calificar_partido', { partidos: partidosConEquipos, idJugador });
                }
            });
        });
    });
});

module.exports = router;
