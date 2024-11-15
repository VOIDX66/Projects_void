const express = require('express');
const path = require('path'); // Para manejar rutas
const registroRoutes = require('./routes/register');

const app = express();
const port = 3000;

// Configurar el motor de vistas
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'public/views'));

// Middleware para parsear datos enviados desde formularios
app.use(express.urlencoded({ extended: true }));

// Rutas de Inicio
app.get('/', (req, res) => {
    res.render('index', { title: 'Bienvenido', message: '¡Hola! Esta es la página principal.' });
  });

// Usar las rutas del módulo 'registro.js'
app.use('/register', registroRoutes);

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});
