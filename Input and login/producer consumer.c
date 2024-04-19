#include <pthread.h>

#include <stdio.h>
#include <semaphore.h>

#define BUFF_SIZE 4
#define FULL 0
#define EMPTY 0

char buffer[BUFF_SIZE];
int nextIn = 0;
int nextOut = 0;

sem_t empty_sem_mutex; // producer semaphore
sem_t full_sem_mutex;  // consumer semaphore

void Put(char item) {
    sem_wait(&empty_sem_mutex); // get the mutex to fill the buffer
    buffer[nextIn] = item;
    nextIn = (nextIn + 1) % BUFF_SIZE;
    printf("Producing %c ...nextIn %d..Ascii=%d\n", item, nextIn, item);
    if (nextIn == FULL) {
        sem_post(&full_sem_mutex);
        sleep(1);
    }
    sem_post(&empty_sem_mutex);
}

void *Producer() {
    int i;
    for (i = 0; i < 10; i++) {
        Put((char)('A' + i % 26));
    }
}

void Get() {
    int item;
    sem_wait(&full_sem_mutex); // gain the mutex to consume from buffer
    item = buffer[nextOut];
    nextOut = (nextOut + 1) % BUFF_SIZE;
    printf("\t...Consuming %c ...nextOut %d..Ascii=%d\n", item, nextOut, item);
    if (nextOut == EMPTY) {
        sleep(1);
    }
    sem_post(&full_sem_mutex);
}

void *Consumer() {
    int i;
    for (i = 0; i < 10; i++) {
        Get();
    }
}

int main() {
    pthread_t ptid, ctid;

    // initialize the semaphores
    sem_init(&empty_sem_mutex, 0, 1);
    sem_init(&full_sem_mutex, 0, 0);

    // creating producer and consumer threads
    if (pthread_create(&ptid, NULL, Producer, NULL)) {
        printf("\nERROR creating producer thread\n");
        exit(1);
    }

    if (pthread_create(&ctid, NULL, Consumer, NULL)) {
        printf("\nERROR creating consumer thread\n");
        exit(1);
    }

    // wait for threads to finish
    pthread_join(ptid, NULL);
    pthread_join(ctid, NULL);

    sem_destroy(&empty_sem_mutex);
    sem_destroy(&full_sem_mutex);

    return 0;
}
