const express = require('express');
const session = require('express-session');
const path = require('path'); // Para manejar rutas
const db = require('./config/db');

// Importar las rutas
const registerRoutes = require('./routes/register');
const loginRoutes = require('./routes/login');
const logoutRoutes = require('./routes/logout');
const ver_lista_jugadoresRoutes = require('./routes/ver_lista_jugadores');
const gestionar_infraccionesRoutes = require('./routes/gestionar_infracciones');
const crear_partidoRoutes = require('./routes/crear_partido');
const confirmar_equiposRoutes = require('./routes/confirmar_equipos');
const ver_historial_partidosRoutes = require('./routes/ver_historial_partidos');
const marcar_jugadoRoutes = require('./routes/marcar_jugado');
const nueva_infraccionRoutes = require('./routes/nueva_infraccion');
const agregar_infraccionRoutes = require('./routes/agregar_infraccion');
const eliminar_infraccionRoutes = require('./routes/eliminar_infraccion');
const marcar_notificacion_leidaRoutes = require('./routes/marcar_notificacion_leida');
const actualizar_suscripcionRoutes = require('./routes/actualizar_suscripcion');
const consultar_infraccionesRoutes = require('./routes/consultar_infracciones');

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
  const user = req.session.user;
  if (user) {
    // Si el usuario está autenticado, mostrar la página principal
    if (user.tipo === 'USER') {
      // Obtener las notificaciones
      const notificacionesQuery = `
        SELECT * FROM Notificaciones
        INNER JOIN Jugadores ON Notificaciones.id_jugador = Jugadores.id_jugador
        INNER JOIN Usuarios ON Jugadores.id_usuario = Usuarios.id_usuario
        WHERE Usuarios.id_usuario = ? AND Notificaciones.leida = 0
      `;
      db.query(notificacionesQuery, [user.id_usuario], (err, notificaciones) => {
        if (err) {
          console.error('Error en la base de datos:', err);
          return res.status(500).send('Error al obtener las notificaciones');
        }

        // Obtener el model_sel de la tabla Jugadores
        const suscripcionQuery = 'SELECT model_sel, disponible FROM Jugadores WHERE id_usuario = ?';
        db.query(suscripcionQuery, [user.id_usuario], (err, result) => {
          if (err) {
            console.error('Error al obtener el model_sel:', err);
            return res.status(500).send('Error al obtener la suscripción del jugador');
          }

          const modelSel = result[0].model_sel; // Valor por defecto en caso de que no se encuentre
          const disponible = result[0].disponible; // Valor por defecto en caso de que no se encuentre
          //console.log(disponible,modelSel);

          // Pasar los datos a la vista 'main_user'
          res.render('main_user', { user, notificaciones, modelSel, disponible });
        });
      });
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

// Usar las rutas del módulo 'confirmar_equipos.js'
app.use('/confirmar_equipos', confirmar_equiposRoutes);

// Usar las rutas del módulo'ver_historial_partidos.js'
app.use('/ver_historial_partidos', ver_historial_partidosRoutes);

// Usar las rutas del módulo'marcar_jugado.js'
app.use('/marcar_jugado', marcar_jugadoRoutes);

// Usar las rutas del módulo'nueva_infraccion.js'
app.use('/nueva_infraccion', nueva_infraccionRoutes);

// Usar las rutas del módulo'agregar_infraccion.js'
app.use('/agregar_infraccion', agregar_infraccionRoutes);

// Usar las rutas del módulo'agregar_infraccion.js'
app.use('/eliminar_infraccion', eliminar_infraccionRoutes);

// Usar las rutas del módulo'marcar_notificacion_leida.js'
app.use('/marcar_notificacion_leida', marcar_notificacion_leidaRoutes);

// Usar las rutas del módulo'actualizar_suscripcion.js'
app.use('/actualizar_suscripcion', actualizar_suscripcionRoutes);

// Usar las rutas del módulo 'consultar_infracciones.js'
app.use('/consultar_infracciones', consultar_infraccionesRoutes);

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});
