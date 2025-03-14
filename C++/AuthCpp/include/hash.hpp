// src/hash.hpp
#ifndef HASH_HPP
#define HASH_HPP

#include <string>

// Declaración de la función que llama al script de Python para hacer el hash
std::string hash_password_with_python(const std::string& password);

#endif // HASH_HPP
