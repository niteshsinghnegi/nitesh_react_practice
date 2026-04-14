#include <stdio.h>

int main() {
    int n, m;
    printf("Enter size of first sorted array: ");
    scanf("%d", &n);
    int arr1[n];
    printf("Enter %d elements of first sorted array:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr1[i]);
    }

    printf("Enter size of second sorted array: ");
    scanf("%d", &m);
    int arr2[m];
    printf("Enter %d elements of second sorted array:\n", m);
    for (int i = 0; i < m; i++) {
        scanf("%d", &arr2[i]);
    }

    int merged[n + m];
    int i = 0, j = 0, k = 0;

    while (i < n && j < m) {
        if (arr1[i] < arr2[j]) {
            merged[k++] = arr1[i++];
        } else {
            merged[k++] = arr2[j++];
        }
    }

    while (i < n) {
        merged[k++] = arr1[i++];
    }

    while (j < m) {
        merged[k++] = arr2[j++];
        
    }

    printf("Merged sorted array:\n");
    for (int l = 0; l < n + m; l++) {
        printf("%d ", merged[l]);
    }

    return 0;
}
