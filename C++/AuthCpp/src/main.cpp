#include <boost/beast.hpp>
#include <boost/asio.hpp>
#include <iostream>
#include <thread>
#include "db.hpp"
#include "migrations.hpp"
#include "routes/routes.hpp"
#define PORT 4500

namespace beast = boost::beast;
namespace http = beast::http;
namespace net = boost::asio;
using tcp = net::ip::tcp;

void handle_connection(tcp::socket socket, Database& db) {
    try {
        beast::flat_buffer buffer;
        http::request<http::string_body> req;
        http::read(socket, buffer, req);

        http::response<http::string_body> res;
        handle_request(req, res, db);

        http::write(socket, res);
        socket.shutdown(tcp::socket::shutdown_send);
    } catch (const std::exception& e) {
        std::cerr << "Error en conexión: " << e.what() << "\n";
    }
}

int main() {
    Database db;
    
    // Ejecutar migraciones antes de iniciar el servidor
    run_migrations(db);

    try {
        net::io_context ioc;
        tcp::acceptor acceptor(ioc, {tcp::v4(), PORT});
        std::cout << "🚀 Servidor corriendo en http://localhost:"<<PORT<<"\n";

        while (true) {
            tcp::socket socket(ioc);
            acceptor.accept(socket);
            std::thread(handle_connection, std::move(socket), std::ref(db)).detach();
        }
    } catch (const std::exception& e) {
        std::cerr << "❌ Error del servidor: " << e.what() << "\n";
    }
}
