#include "routes/auth.hpp"
#include "routes/users.hpp"
#include <jwt-cpp/jwt.h>
#include <nlohmann/json.hpp>
#include <iostream>

using json = nlohmann::json;

// Función para decodificar el JWT y extraer datos del usuario
bool decode_jwt_token(const std::string& token, User& user) {
    try {
        // Obtener la misma clave secreta usada en login
        std::string secret_key = generate_secret_key();

        // Decodificar el token y verificar la firma
        auto verifier = jwt::verify()
            .allow_algorithm(jwt::algorithm::hs256{secret_key})
            .with_issuer("my_app");

        auto decoded_token = jwt::decode(token);
        verifier.verify(decoded_token);  // Verifica la firma y la validez

        // Extraer datos del usuario
        user.id = std::stoi(decoded_token.get_payload_claim("id").as_string());
        user.name = decoded_token.get_payload_claim("name").as_string();

        return true;
    } catch (const std::exception& e) {
        return false;
    }
}


// Middleware para autenticar al usuario
void authenticate_user(const http::request<http::string_body>& req, http::response<http::string_body>& res) {
    // Verificar si la cabecera "Authorization" está presente
    auto auth_header = req[http::field::authorization];
    if (auth_header.empty()) {
        res.result(http::status::unauthorized);
        res.body() = R"({"error": "Token de autenticación faltante"})";
        res.prepare_payload();
        return;
    }

    // Extraer el token (Formato: "Bearer <token>")
    std::string token = auth_header.substr(7);

    // Intentar decodificar el token
    User user;
    if (!decode_jwt_token(token, user)) {
        res.result(http::status::unauthorized);
        res.body() = R"({"error": "Token inválido"})";
        res.prepare_payload();
        return;
    }

    // Crear respuesta JSON con los datos del usuario autenticado
    json user_json;
    user_json["id"] = user.id;
    user_json["name"] = user.name;

    res.result(http::status::ok);
    res.body() = user_json.dump();
    res.prepare_payload();
}
