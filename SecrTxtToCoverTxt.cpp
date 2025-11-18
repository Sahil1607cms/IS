#include <bits/stdc++.h>
using namespace std;

string to_bits(const string &s) {
    string out;
    for (unsigned char c : s) {
        for (int i = 7; i >= 0; --i)
            out.push_back((c >> i) & 1 ? '1' : '0');
    }
    return out;
}

string from_bits(const string &bits) {
    string s;
    for (size_t i = 0; i + 7 < bits.size(); i += 8) {
        int v = 0;
        for (int j = 0; j < 8; ++j)
            v = (v << 1) | (bits[i+j] - '0');
        s.push_back(char(v));
    }
    return s;
}

void encode(const string &cover_file, const string &secret_file, const string &output_file) {
    ifstream cover(cover_file);
    ifstream secret(secret_file);

    vector<string> lines;
    string line, secret_msg((istreambuf_iterator<char>(secret)), {});
    while (getline(cover, line)) lines.push_back(line);

    string bits = to_bits(secret_msg);
    if (bits.size() > lines.size()) {
        throw runtime_error("Not enough lines in cover text");
    }

    for (size_t i = 0; i < lines.size(); ++i) {
        if (i < bits.size())
            lines[i] += (bits[i] == '0' ? " " : "\t");
    }

    ofstream out(output_file);
    for (size_t i = 0; i < lines.size(); ++i)
        out << lines[i] << (i + 1 < lines.size() ? "\n" : "");
}

string decode(const string &file) {
    ifstream in(file);
    string line, bits;

    while (getline(in, line)) {
        if (!line.empty()) {
            if (line.back() == ' ') bits += '0';
            else if (line.back() == '\t') bits += '1';
        }
    }
    return from_bits(bits);
}

int main() {
    encode("cover_text.txt", "secret_message.txt", "stego_output.txt");
    cout << "Recovered message: " << decode("stego_output.txt") << "\n";
}
