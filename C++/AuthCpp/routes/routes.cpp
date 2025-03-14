#include "routes/routes.hpp"
#include "routes/users.hpp"
#include "routes/auth.hpp"
#include "cors.hpp"
#include <iostream>

void handle_request(const http::request<http::string_body>& req, http::response<http::string_body>& res, Database& db) {
    if (req.target() == "/" && req.method() == http::verb::get) {
        res.result(http::status::ok);
        res.set(http::field::content_type, "application/json");
        res.body() = R"({"mensaje": "¡Bienvenido a mi API en C++!"})";
    } 

    // Ruta para obtener todos los usuarios mediante metodo GET
    else if (req.target().starts_with("/usuarios")) {
        if (req.method() == http::verb::get) {
            handle_get_users(req, res, db);
        } else {
            res.result(http::status::method_not_allowed);
            res.body() = R"({"error": "Método no permitido"})";
        }
    }

    // Ruta para registrar un usuario mediante metodo POST
    else if (req.target().starts_with("/register")){
        if (req.method() == http::verb::post) {
            handle_register(req, res, db);
        } else {
            res.result(http::status::method_not_allowed);
            res.body() = R"({"error": "Método no permitido"})";
        }
    }

    // Ruta para loguear con un usuario mediante metodo POST
    else if (req.target().starts_with("/login")) {
        if (req.method() == http::verb::post) {
            handle_login(req, res, db);
        } else {
            res.result(http::status::method_not_allowed);
            res.body() = R"({"error": "Método no permitido"})";
        }
    }

    // Ruta para obtener los datos mediante autentificacion
    else if (req.target().starts_with("/get_user")) {
        if (req.method() == http::verb::post){
                authenticate_user(req, res);
        } else {
            res.result(http::status::method_not_allowed);
            res.body() = R"({"error": "Método no permitido"})";
        } 

    // Respuesta en caso de usar una ruta no definida    
    } else {
        res.result(http::status::not_found);
        res.body() = R"({"error": "Ruta no encontrada"})";
    }

    res.prepare_payload();
}
