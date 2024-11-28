const express = require('express');
const session = require('express-session');
const path = require('path'); // Para manejar rutas

// Importar las rutas
const registerRoutes = require('./routes/register');
const loginRoutes = require('./routes/login');
const logoutRoutes = require('./routes/logout');
const ver_lista_jugadoresRoutes = require('./routes/ver_lista_jugadores');
const gestionar_infraccionesRoutes = require('./routes/gestionar_infracciones');
const crear_partidoRoutes = require('./routes/crear_partido');

const app = express();
const port = 3000;

// Configurar el motor de vistas
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));


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

// Usar las rutas del módulo'ver_lista_jugadores.js'
app.use('/ver_lista_jugadores', ver_lista_jugadoresRoutes);

// Usar las rutas del módulo 'gestionar_infracciones.js'
app.use('/gestionar_infracciones', gestionar_infraccionesRoutes);

// Usar las rutas del módulo 'crear_partido.js'
app.use('/crear_partido', crear_partidoRoutes);

// Datos simulados
const jugadoresMock = [
  { nombre: "Juan Pérez", equipo: "Equipo A" },
  { nombre: "María Gómez", equipo: "Equipo B" },
  { nombre: "Carlos Díaz", equipo: "Equipo A" }
];

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});
