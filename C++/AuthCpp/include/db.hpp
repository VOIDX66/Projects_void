#ifndef DB_HPP
#define DB_HPP

#include <pqxx/pqxx>
#include <memory>
#include <iostream>

class Database {
public:
    Database(); // Constructor
    pqxx::connection& get_connection(); // Obtener la conexión

private:
    std::unique_ptr<pqxx::connection> conn;
};

#endif // DB_HPP
