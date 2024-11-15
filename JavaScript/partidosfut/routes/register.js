const express = require('express');
const router = express.Router();
const db = require('../config/db'); // Importa la conexión a la base de datos

// Ruta GET para mostrar el formulario de registro
router.get('/', (req, res) => {
  res.render('register'); // Renderiza la vista "register.ejs"
});

// Ruta POST para manejar el registro de usuarios
router.post('/', (req, res) => {
  const { nombre, id_usuario, contrasena } = req.body;

  // Verificar si el ID de usuario ya existe
  const queryVerification = 'SELECT id_usuario FROM Usuarios WHERE id_usuario = ?';
  db.query(queryVerification, [id_usuario], (err, result) => {
    if (err) {
      console.error('Error al verificar el ID en la base de datos:', err);
      return res.status(500).send('Error del servidor al verificar el ID.');
    }

    if (result.length > 0) {
      // Si el ID ya existe, notificar al usuario
      return res.status(400).send('El ID ya está registrado. Por favor, utiliza otro.');
    }

    // Si el ID no existe, insertar el nuevo usuario
    const queryInsert = 'INSERT INTO Usuarios (id_usuario, nombre, contrasena) VALUES (?, ?, ?)';
    db.query(queryInsert, [id_usuario, nombre, contrasena], (err) => {
      if (err) {
        console.error('Error al insertar en la base de datos:', err);
        return res.status(500).send('Error al registrar al usuario.');
      }

      const quertInsertJugador = 'INSERT INTO Jugadores (id_usuario) VALUES (?)';
      db.query(quertInsertJugador, [[id_usuario]], (err) => {
        if (err) {
          console.error('Error al insertar jugador en la base de datos:', err);
          return res.status(500).send('Error al registrar al jugador.');
        }
        // Renderizar la página de confirmación
        res.render('confirmacion', { nombre });
      });
    });
  });
});

module.exports = router;
