#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <vector>

using namespace std;

const int MAX_SIZE = 8;  // Tamaño del buffer
vector<string> buffer(MAX_SIZE); // Cambiado a vector de strings
int producer_pos = 0;
int consumer_pos = 0;
int current_size = 0;
int global_process_counter = 1; // Contador global para procesos

mutex mtx;
condition_variable cv_producer, cv_consumer;

// Función para mostrar el estado del buffer
void mostrar_buffer() {
    cout << "Estado del buffer: ";
    if (current_size == 0) {
        cout << "Vacío" << endl;
    } else {
        cout << "[";
        for (int i = 0; i < current_size; ++i) {
            int pos = (consumer_pos + i) % MAX_SIZE;
            cout << "Posición " << (pos + 1) << ": " << buffer[pos] << (i < current_size - 1 ? ", " : "");
        }
        cout << "]" << endl;
    }
    cout << "Elementos en el buffer: " << current_size << ", Huecos restantes: " << (MAX_SIZE - current_size) << endl;
}

// Función para mostrar las posiciones del productor y del consumidor
void mostrar_posiciones() {
    cout << "Posición del productor: " << producer_pos + 1 << ", Posición del consumidor: " << consumer_pos + 1 << endl;
}

// Función para producir un elemento
void producir() {
    buffer[producer_pos] = "d" + to_string(global_process_counter++); // Asignar nombre como d1, d2, etc.
    producer_pos = (producer_pos + 1) % MAX_SIZE;
    current_size++;
}

// Función para consumir un elemento
string consumir() {
    string dato = buffer[consumer_pos];
    consumer_pos = (consumer_pos + 1) % MAX_SIZE;
    current_size--;
    return dato;
}

// Productor
void productor(int cantidad) {
    unique_lock<mutex> lock(mtx);
    for (int i = 0; i < cantidad; ++i) {
        cv_producer.wait(lock, [] { return current_size < MAX_SIZE; }); // Espera hasta que haya espacio

        producir(); // Cambiado para no usar el índice
        cout << "Productor produjo: d" << (global_process_counter - 1) << endl; // Mostrar el último producido
        mostrar_posiciones(); // Mostrar las posiciones del productor y consumidor
        mostrar_buffer();
        cout << endl; // Salto de línea después de la acción de producción

        // Notificar al consumidor
        cv_consumer.notify_one();
    }
    if (cantidad == 0)
    {
        cout << "Productor produjo: \n"<< endl;
    }    
}

// Consumidor
void consumidor(int cantidad) {
    unique_lock<mutex> lock(mtx);
    for (int i = 0; i < cantidad; ++i) {
        cv_consumer.wait(lock, [] { return current_size > 0; }); // Espera hasta que haya elementos disponibles

        string dato = consumir();
        cout << "Consumidor consumió: " << dato << endl;
        mostrar_posiciones(); // Mostrar las posiciones del productor y consumidor
        mostrar_buffer();
        cout << endl; // Salto de línea después de la acción de consumo

        // Notificar al productor
        cv_producer.notify_one();
    }
    if(cantidad == 0) {
        cout << "Consumidor consumió: \n"<< endl;
    }}

int main() {
    thread t1(productor, 4);  // Iniciar productor
    thread t2(consumidor, 0); // Iniciar consumidor

    thread t3(productor, 3);
    thread t4(consumidor, 3); 

    thread t5(productor, 3); 
    thread t6(consumidor, 2);

    thread t7(productor, 2);
    thread t8(consumidor, 0);

    thread t9(productor, 2);
    thread t10(consumidor, 0);

    thread t11(productor, 0);
    thread t12(consumidor, 4);

    thread t13(productor, 0);
    thread t14(consumidor, 4);

    t1.join();
    t2.join();
    t3.join();
    t4.join();
    t5.join();
    t6.join();
    t7.join();
    t8.join();
    t9.join();
    t10.join();
    t11.join();
    t12.join();
    t13.join();
    t14.join();

    return 0;
}
