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
const calificar_partidoRoutes = require('./routes/calificar_partido');
const calificar_jugadoresRoutes = require('./routes/calificar_jugadores');
const agregar_calificacionRoutes = require('./routes/agregar_calificacion');
const gestionar_participacionRoutes = require('./routes/gestionar_participacion');
const agregar_participacionRoutes = require('./routes/agregar_participacion');
const dar_de_baja_participacionRoutes = require('./routes/dar_de_baja_participacion');

const app = express();
const port = 5000;

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


// Variable para habilitar o deshabilitar el uso de datos simulados
const usarDatosSimulados = false;

// Datos simulados
const usuariosMock = [
  { id_usuario: 1, nombre: "UsuarioDemo", tipo: "USER" },
  { id_usuario: 2, nombre: "AdminDemo", tipo: "ADMIN" }
];

const notificacionesMock = [
  { id: 1, mensaje: "Notificación 1", leida: 0 },
  { id: 2, mensaje: "Notificación 2", leida: 0 }
];

const jugadoresMock = [
  { id_usuario: 1, model_sel: "Plan Básico", disponible: true },
  { id_usuario: 2, model_sel: "Plan Premium", disponible: false }
];

// Ruta principal (index)
app.get('/', (req, res) => {
  const user = req.session.user; //|| usuariosMock[0]; // Usar un usuario simulado si no hay sesión activa

  if (usarDatosSimulados) {
    if (user.tipo === 'USER') {
      // Datos simulados para la vista del usuario
      const notificaciones = notificacionesMock.filter(n => n.leida === 0);
      const jugadorData = jugadoresMock.find(j => j.id_usuario === user.id_usuario);

      const modelSel = jugadorData ? jugadorData.model_sel : "Plan Básico";
      const disponible = jugadorData ? jugadorData.disponible : false;

      res.render('main_user', { user, notificaciones, modelSel, disponible });
    } else {
      res.render('main_admin', { user });
    }
  } else {
    // Lógica original con base de datos
    if (user){
      if (user.tipo === 'USER') {
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

          const suscripcionQuery = 'SELECT model_sel, disponible FROM Jugadores WHERE id_usuario = ?';
          db.query(suscripcionQuery, [user.id_usuario], (err, result) => {
            if (err) {
              console.error('Error al obtener el model_sel:', err);
              return res.status(500).send('Error al obtener la suscripción del jugador');
            }

            const modelSel = result[0].model_sel;
            const disponible = result[0].disponible;

            res.render('main_user', { user, notificaciones, modelSel, disponible });
          });
        });
      } else {
        res.render('main_admin', { user });
      }
    } else {
      res.render('index');
    }
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

// Usar las rutas del módulo 'calificar_partido.js'
app.use('/calificar_partido', calificar_partidoRoutes);

//  Usar las rutas del módulo 'calificar_jugadores.js'
app.use('/calificar_jugadores', calificar_jugadoresRoutes);

//  Usar las rutas del módulo 'agregar_calificaciones.js'
app.use('/agregar_calificacion', agregar_calificacionRoutes);

// Usar las rutas del módulo 'gestionar_participacion.js'
app.use('/gestionar_participacion', gestionar_participacionRoutes);

// Usar las rutas del módulo 'agregar_participacion.js'
app.use('/agregar_participacion', agregar_participacionRoutes);

// Usar las rutas del módulo 'dar_de_baja_participacion.js'
app.use('/dar_de_baja_participacion', dar_de_baja_participacionRoutes);

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});
