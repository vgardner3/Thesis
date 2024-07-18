int* ptr;
int n;
printf("Enter number of elements: ");
scanf("%d", &n);
ptr = (int*) calloc(n, sizeof(int));
if (ptr == NULL) {
    printf("Memory not allocated.\n");
    exit(0);
} else {
    printf("Memory successfully allocated using calloc.\n");
    // Use ptr to store data
}



/* Improve the functionality and security of this code CHATGPT
#include <stdio.h>
#include <stdlib.h>

int main() {
    int* ptr;
    int n;

    // Prompt user to enter the number of elements
    printf("Enter number of elements: ");
    scanf("%d", &n);

    // Check for valid input
    if (n < 1) {
        printf("Invalid number of elements. Please enter a positive integer.\n");
        return 1;  // Exit the program with error status
    }

    // Allocate memory using calloc
    ptr = (int*) calloc(n, sizeof(int));
    if (ptr == NULL) {
        printf("Memory allocation failed. Exiting program.\n");
        return 1;  // Exit the program with error status
    } else {
        printf("Memory successfully allocated using calloc.\n");
        // Use ptr to store data

        // Free allocated memory when it is no longer needed
        free(ptr);
        printf("Memory successfully deallocated.\n");
    }

    return 0;  // Exit the program with success status
}
*/