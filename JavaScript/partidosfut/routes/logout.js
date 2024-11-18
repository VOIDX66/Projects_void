const express = require('express');
const router = express.Router();

// Ruta para cerrar sesión
router.get('/', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      console.error('Error al cerrar sesión:', err);
      return res.status(500).send('Error al cerrar sesión');
    }
    res.redirect('/'); // Redirige al índice después de cerrar sesión
  });
});

module.exports = router;
