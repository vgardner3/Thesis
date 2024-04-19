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
