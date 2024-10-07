void pensar(){
    continue;;
}

filosofo() {
    while (true) {
    pensar();                  // El filósofo está pensando.
    wait(semaforo_tenedor[i]); // Toma el tenedor izquierdo.
    wait(semaforo_tenedor[(i+1) % 5]); // Toma el tenedor derecho.
    comer();                   // El filósofo está comiendo.
    signal(semaforo_tenedor[i]); // Suelta el tenedor izquierdo.
    signal(semaforo_tenedor[(i+1) % 5]); // Suelta el tenedor derecho.
}    