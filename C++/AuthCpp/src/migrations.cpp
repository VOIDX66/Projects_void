#include "migrations.hpp"
#include <iostream>

void run_migrations(Database& db) {
    std::cout << "Migración en curso...\n";
    
    try {
        pqxx::connection& conn = db.get_connection();
        pqxx::work txn(conn);
        txn.exec(R"(
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            );
        )");
        txn.commit();
        std::cout << "Migración completada.\n";
    } catch (const std::exception& e) {
        std::cerr << "Error en migración: " << e.what() << "\n";
    }
}
