const express = require('express');
const session = require('express-session');
const path = require('path'); // Para manejar rutas

// Importar las rutas
const registerRoutes = require('./routes/register');
const loginRoutes = require('./routes/login');
const logoutRoutes = require('./routes/logout');


const app = express();
const port = 3000;

// Configurar el motor de vistas
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'public/views'));

// Configurar middleware de sesión
app.use(session({
  secret: 'tu-secreto',  // Una cadena secreta para firmar la sesión
  resave: false,         // No re-guardar la sesión si no ha cambiado
  saveUninitialized: true,  // Guardar sesiones sin inicializar
  cookie: { secure: false } // Para HTTP (si usas HTTPS cambia a true)
}));

// Middleware para parsear datos enviados desde formularios
app.use(express.urlencoded({ extended: true }));

// Json
app.use(express.json());


// Ruta principal (index)
app.get('/', (req, res) => {
  const user = req.session.user
  if (user) {
    // Si el usuario está autenticado, mostrar la página principal
    if (user.tipo === 'USER'){
      res.render('main_user', { user });
    } else {
      res.render('main_admin', { user });
    }
  } else {
    // Si no está autenticado, mostrar opciones de login y registro
    res.render('index'); // Vista con opciones de login y registro
  }
});

// Usar las rutas del módulo 'registro.js'
app.use('/register', registerRoutes);

// Usar las rutas del módulo 'login.js'
app.use('/login', loginRoutes);

// Usar las rutas del módulo 'logout.js'
app.use('/logout', logoutRoutes); 

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});
