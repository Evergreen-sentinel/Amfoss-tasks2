#include <stdio.h>
#include <stdlib.h>

void print_star_pattern_to_file(int n, FILE *outputFile) {
    for (int i = 1; i <= n; i += 2) {
        for (int j = 0; j < (n - i) / 2; j++) {
            fputc(' ', outputFile);
        }
        for (int j = 0; j < i; j++) {
            fputc('*', outputFile);
        }
        fputc('\n', outputFile);
    }

    for (int i = n - 2; i >= 1; i -= 2) {
        for (int j = 0; j < (n - i) / 2; j++) {
            fputc(' ', outputFile);
        }
        for (int j = 0; j < i; j++) {
            fputc('*', outputFile);
        }
        fputc('\n', outputFile);
    }
}

int main() {
    FILE *inputFile = fopen("input2.txt", "r");
    if (inputFile == NULL) {
        perror("Error opening input file");
        return 1;
    }

    int n;
    fscanf(inputFile, "%d", &n);
    fclose(inputFile);

    FILE *outputFile = fopen("output2.txt", "w");
    if (outputFile == NULL) {
        perror("Error opening output file");
        return 1;
    }

    print_star_pattern_to_file(n, outputFile);
    fclose(outputFile);

    return 0;
}
