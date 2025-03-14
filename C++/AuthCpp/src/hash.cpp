// src/hash.cpp
#include "hash.hpp"
#include <iostream>
#include <cstdlib>
#include <string>

std::string hash_password_with_python(const std::string& password) {
    // Comando para ejecutar el script de Python con la contraseña como argumento
    std::string command = "python3 scripts/hash_password.py " + password; 
    std::string result = "";

    // Ejecutar el script y capturar la salida
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        std::cerr << "Error al ejecutar el script de Python para hashear contraseña" << std::endl;
        return "";
    }

    char buffer[128];
    while (fgets(buffer, sizeof(buffer), pipe)) {
        result += buffer;  // Acumula la salida del script
    }

    // Cerrar el proceso correctamente con pclose
    pclose(pipe);

    // Eliminar el salto de línea al final si lo hay
    if (!result.empty() && result[result.size() - 1] == '\n') {
        result = result.substr(0, result.size() - 1);
    }

    return result;
}
