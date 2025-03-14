#ifndef AUTH_HPP
#define AUTH_HPP

#include <jwt-cpp/jwt.h>
#include <string>
#include <optional>
#include <nlohmann/json.hpp>
#include <boost/beast.hpp>
#include <boost/asio.hpp>

namespace beast = boost::beast;
namespace http = beast::http;

// Estructura para almacenar los datos del usuario
struct User {
    int id;
    std::string name;
};

// Función para decodificar el JWT y obtener los datos del usuario
bool decode_jwt_token(const std::string& token, const std::string& secret_key, User& user);

// Middleware para autenticar al usuario usando el token JWT
void authenticate_user(const http::request<http::string_body>& req, http::response<http::string_body>& res);

#endif // AUTH_HPP
