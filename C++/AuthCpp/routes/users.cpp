#include <jwt-cpp/jwt.h> //Autenticacion por tokens
#include "routes/users.hpp" // Para manejar las rutas
#include "cors.hpp" // Para manejar las solicitudes
#include <pqxx/pqxx> // Conexion con la base de datos
#include <nlohmann/json.hpp> // Manejo de archivos json
#include <hash.hpp> // Para hashear la contraseña
#include <iostream> // Libreria estandar Cpp
using json = nlohmann::json;

std::string generate_secret_key() {
    // Obtener la fecha actual (día)
    auto now = std::chrono::system_clock::now();
    auto time_t_now = std::chrono::system_clock::to_time_t(now);
    std::tm tm_now = *std::localtime(&time_t_now);

    // Formatear la fecha en "YYYY-MM-DD"
    std::stringstream ss;
    ss << std::put_time(&tm_now, "%Y-%m-%d");

    // Devolver la clave secreta en el formato "usarioYYYY-MM-DD"
    return "usario" + ss.str();
}

void handle_get_users(const http::request<http::string_body>& req, http::response<http::string_body>& res, Database& db) {
    try {
        pqxx::work txn(db.get_connection());
        pqxx::result result = txn.exec("SELECT id, name FROM users;");

        json users_json = json::array(); // Crear un array JSON

        for (const auto& row : result) {
            users_json.push_back({{"id", row["id"].as<int>()}, {"name", row["name"].as<std::string>()}});
        }

        res.result(http::status::ok);
        res.set(http::field::content_type, "application/json");
        set_cors(res);  
        res.body() = users_json.dump();  // Convertir JSON a string
        txn.commit();
    } catch (const std::exception& e) {
        res.result(http::status::internal_server_error);
        set_cors(res);
        json error_json = {{"error", e.what()}};
        res.body() = error_json.dump();
    }
    res.prepare_payload();
}

void handle_login(const http::request<http::string_body>& req, http::response<http::string_body>& res, Database& db) {
    try {
        if (req.body().empty()) {
            throw std::invalid_argument("El cuerpo de la petición está vacío.");
        }

        json request_json = json::parse(req.body());
        std::string name = request_json.value("name", "");
        std::string password = request_json.value("password", "");

        if (name.empty() || password.empty()) {
            throw std::invalid_argument("El nombre o la contraseña no pueden estar vacíos.");
        }

        // Verificar si el usuario existe
        pqxx::work txn(db.get_connection());
        pqxx::result result = txn.exec_params("SELECT id, password FROM users WHERE name = $1;", name);

        if (result.empty()) {
            throw std::invalid_argument("El usuario no existe.");
        }

        int user_id = result[0]["id"].as<int>();
        std::string stored_hash = result[0]["password"].as<std::string>();

        // Hashear la contraseña ingresada y compararla con la almacenada
        std::string hashed_password = hash_password_with_python(password);

        if (hashed_password != stored_hash) {
            throw std::invalid_argument("Contraseña incorrecta.");
        }

        // Usar una clave secreta fija en toda la aplicación
        std::string secret_key = generate_secret_key();

        // Generar el JWT con los datos correctos
        auto token = jwt::create()
            .set_issuer("my_app")
            .set_subject(std::to_string(user_id))  // Guardamos el ID como subject
            .set_payload_claim("id", jwt::claim(std::to_string(user_id)))
            .set_payload_claim("name", jwt::claim(name))
            .set_expires_at(std::chrono::system_clock::now() + std::chrono::hours(24))
            .sign(jwt::algorithm::hs256{secret_key});

        res.result(http::status::ok);
        set_cors(res);
        res.body() = R"({"message": "Inicio de sesión exitoso", "token": ")" + token + R"("})";
    } catch (const std::invalid_argument& e) {
        res.result(http::status::bad_request);
        set_cors(res);
        res.body() = R"({"error": ")" + std::string(e.what()) + R"("})";
    } catch (const std::exception& e) {
        res.result(http::status::internal_server_error);
        set_cors(res);
        res.body() = R"({"error": ")" + std::string(e.what()) + R"("})";
    }
    res.prepare_payload();
}


void handle_register(const http::request<http::string_body>& req, http::response<http::string_body>& res, Database& db) {
    try {
        if (req.body().empty()) {
            throw std::invalid_argument("El cuerpo de la petición está vacío.");
        }

        json request_json = json::parse(req.body());
        std::string name = request_json.value("name", "");
        std::string password = request_json.value("password", "");

        if (name.empty() || password.empty()) {
            throw std::invalid_argument("El nombre o la contraseña no pueden estar vacíos.");
        }

        // Verificar si el usuario existe
        pqxx::work txn(db.get_connection());
        pqxx::result result = txn.exec_params("SELECT password FROM users WHERE name = $1;", name);

        if (result.size() == 1) {
            throw std::invalid_argument("El usuario ya existe.");
        }

        // Hashear la contraseña con Python
        std::string hashed_password = hash_password_with_python(password);

        txn.exec_params("INSERT INTO users (name, password) VALUES ($1, $2);", name, hashed_password);
        txn.commit();

        res.result(http::status::created);
        set_cors(res);
        res.body() = R"({"message": "Usuario registrado con éxito"})";
    } catch (const std::invalid_argument& e) {
        res.result(http::status::bad_request);
        set_cors(res);
        res.body() = R"({"error": ")" + std::string(e.what()) + R"("})";
    } catch (const std::exception& e) {
        res.result(http::status::internal_server_error);
        set_cors(res);
        res.body() = R"({"error": ")" + std::string(e.what()) + R"("})";
    }
    res.prepare_payload();
}
