#include <iostream>
#include <thread>
#include <mutex>
#include <vector>
#include <chrono> 
#include <condition_variable>

using namespace std;

const int MAX_SIZE = 8;  // Tamaño del buffer
vector<string> buffer(MAX_SIZE);

int producer_pos = 0;
int consumer_pos = 0;
int current_size = 0;
int global_process_counter = 1; // Contador global para procesos

// Semáforos
class Semaphore {
public:
    Semaphore(int initial) : value(initial) {}

    void wait() {
        unique_lock<mutex> lock(mtx);
        value--;
        if (value < 0) {
            cv.wait(lock); // Bloquea si el semáforo es negativo
        }
    }

    void signal() {
        unique_lock<mutex> lock(mtx);
        value++;
        if (value <= 0) {
            cv.notify_one(); // Desbloquea un hilo si hay uno esperando
        }
    }

private:
    int value; // Valor del semáforo
    mutex mtx; // Mutex para proteger el acceso
    condition_variable cv; // Variable de condición
};

// Inicializar semáforos
Semaphore huecos(MAX_SIZE); // Huecos disponibles en el buffer
Semaphore elementos(0); // elementos en el buffer
mutex buffer_mutex; // Mutex para proteger el acceso al buffer

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
    buffer[producer_pos] = "d" + to_string(global_process_counter++); // Asignar nombre como p1, p2, etc.
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
    for (int i = 0; i < cantidad; ++i) {
        huecos.wait(); // Espera hasta que haya espacio vacío
        {
            lock_guard<mutex> lock(buffer_mutex); // Protege la sección crítica
            producir(); // Producción
            cout << "Productor produjo: d" << (global_process_counter - 1) << endl; // Mostrar el último producido
            mostrar_posiciones(); // Mostrar las posiciones del productor y consumidor
            mostrar_buffer();
            cout << endl; // Salto de línea después de la acción de producción
        }
        elementos.signal(); // Señala que hay un nuevo elemento producido
    }
}

// Consumidor
void consumidor(int cantidad) {
    for (int i = 0; i < cantidad; ++i) {
        elementos.wait(); // Espera hasta que haya elementos disponibles
        {
            lock_guard<mutex> lock(buffer_mutex); // Protege la sección crítica
            string dato = consumir(); // Consumo
            cout << "Consumidor consumió: " << dato << endl;
            mostrar_posiciones(); // Mostrar las posiciones del productor y consumidor
            mostrar_buffer();
            cout << endl; // Salto de línea después de la acción de consumo
        }
        huecos.signal(); // Señala que hay un espacio vacío
    }
}

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
