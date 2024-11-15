const mysql = require('mysql2');

// Crear la conexión
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'userpartidos',      // Reemplaza con tu usuario
  password: 'upartidos', // Reemplaza con tu contraseña
  database: 'partidos_db' // Reemplaza con tu base de datos
});

// Conectar
connection.connect((err) => {
  if (err) {
    console.error('Error de conexión: ' + err.stack);
    return;
  }
  console.log('Conectado a la base de datos como ID ' + connection.threadId);
});

module.exports = connection;