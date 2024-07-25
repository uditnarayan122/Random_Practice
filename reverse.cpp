#include <iostream>
#include <string>

// Function to reverse a string
void reverseString(std::string &str) {
    int length = str.length();
    for (int i = 0; i < length / 2; i++) {
        char temp = str[i];
        str[i] = str[length - i - 1];
        str[length - i - 1] = temp;
    }
}

int main() {
    std::string str = "Hello, World!";
    std::cout << "Original string: " << str << std::endl;
    
    reverseString(str);
    
    std::cout << "Reversed string: " << str << std::endl;
    
    return 0;
}
