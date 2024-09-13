#include <iostream>
#include <fstream>

std::string createStarPattern(int n) {
    std::string pattern;

    for (int i = 1; i <= n; i += 2) {
        pattern += std::string((n - i) / 2, ' ') + std::string(i, '*') + "\n";
    }

    for (int i = n - 2; i >= 1; i -= 2) {
        pattern += std::string((n - i) / 2, ' ') + std::string(i, '*') + "\n";
    }

    return pattern;
}

int main() {
    std::ifstream inputFile("input2.txt");
    std::ofstream outputFile("output2.txt");

    if (inputFile && outputFile) {
        int n;
        inputFile >> n;

        std::string pattern = createStarPattern(n);
        outputFile << pattern;
    } else {
        std::cerr << "Error opening file!" << std::endl;
    }

    inputFile.close();
    outputFile.close();

    return 0;
}
