#include "cors.hpp"

void set_cors(http::response<http::string_body>& res) {
    res.set(http::field::access_control_allow_origin, "*");  
    res.set(http::field::access_control_allow_methods, "GET, POST, PUT, DELETE, OPTIONS");  
    res.set(http::field::access_control_allow_headers, "Content-Type, Authorization");
}

void handle_options(const http::request<http::string_body>& req, http::response<http::string_body>& res) {
    res.result(http::status::no_content);
    set_cors(res);
    res.prepare_payload();
}
