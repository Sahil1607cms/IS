#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream fin("even.txt");     // ----> Read the input file
    if (!fin) {
        cout << "Error opening file";
        return 1;
    }

    string line;
    string hidden = "";

    while (getline(fin, line)) {      // ----> Read each line
        for (char c : line) {
            if (!isspace(c)) {        // first non-whitespace character
                hidden += c;
                break;
            }
        }
    }

    cout << hidden;    // final hidden message
    return 0;
}