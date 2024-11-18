const express = require('express');
const router = express.Router();
const db = require('../config/db');  // Conexión a la base de datos

// Ruta para mostrar el formulario de inicio de sesión
router.get('/', (req, res) => {
  if(req.session.user){
    res.redirect('/');
  } else {
    res.render('login'); // Renderiza el formulario de login
  }
});

// Ruta para manejar el inicio de sesión
router.post('/', (req, res) => {
  const { nombre, contrasena } = req.body;

  // Verificar las credenciales en la base de datos
  const query = 'SELECT * FROM Usuarios WHERE nombre = ? AND contrasena = ?';
  db.query(query, [nombre, contrasena], (err, results) => {
    if (err) {
      console.error('Error en la base de datos:', err);
      return res.status(500).send('Error al verificar las credenciales');
    }

    if (results.length > 0) {
      // Iniciar sesión (guardar el usuario en la sesión)
      req.session.user = results[0]; // Guarda los datos del usuario en la sesión
      return res.redirect('/'); // Redirigir a la página de inicio
    } else {
      return res.status(401).send('Credenciales incorrectas'); // Si las credenciales son incorrectas
    }
  });
});

module.exports = router;
