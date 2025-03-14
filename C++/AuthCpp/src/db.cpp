#include "db.hpp"

Database::Database() {
    try {
        conn = std::make_unique<pqxx::connection>("dbname=cpp_db user=cpp_back password=cppassword hostaddr=127.0.0.1 port=5432");
        if (conn->is_open()) {
            std::cout << "✅ Conexión exitosa a PostgreSQL!" << std::endl;
        }
    } catch (const std::exception &e) {
        std::cerr << "❌ Error de conexión: " << e.what() << std::endl;
    }
}

pqxx::connection& Database::get_connection() {
    return *conn;
}
