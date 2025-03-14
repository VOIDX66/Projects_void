#ifndef CORS_HPP
#define CORS_HPP

#include <boost/beast/http.hpp>

namespace http = boost::beast::http;

void set_cors(http::response<http::string_body>& res);
void handle_options(const http::request<http::string_body>& req, http::response<http::string_body>& res);

#endif // CORS_HPP
