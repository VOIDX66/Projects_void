#ifndef ROUTES_HPP
#define ROUTES_HPP

#include <boost/beast.hpp>
#include <boost/asio.hpp>
#include "db.hpp"

namespace beast = boost::beast;
namespace http = beast::http;
namespace net = boost::asio;
using tcp = net::ip::tcp;

void handle_request(const http::request<http::string_body>& req, http::response<http::string_body>& res, Database& db);

#endif // ROUTES_HPP
