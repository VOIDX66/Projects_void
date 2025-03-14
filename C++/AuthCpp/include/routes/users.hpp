#ifndef USERS_HPP
#define USERS_HPP

#include <boost/beast.hpp>
#include <boost/asio.hpp>
#include <nlohmann/json.hpp>
#include <string>
#include <hash.hpp>
#include "db.hpp"

namespace beast = boost::beast;
namespace http = beast::http;

void handle_get_users(const http::request<http::string_body>& req, http::response<http::string_body>& res, Database& db);
void handle_register(const http::request<http::string_body>& req, http::response<http::string_body>& res, Database& db);
void handle_login(const http::request<http::string_body>& req, http::response<http::string_body>& res, Database& db);
std::string generate_secret_key();

#endif // USERS_HPP
