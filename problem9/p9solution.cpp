#include <cstdlib>
#include <iostream>

bool is_palindrome(int x) 
{
    // Edge cases:
    // - Negative numbers cannot be palindrome
    // - If the last number is a 0 then 'x' must be 0 to be palindrome
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false; 
    }

    // reverse half the number
    int rev_half = 0;
    while (x > rev_half) {
        int last_n = x % 10;
        rev_half *= 10;
        rev_half += last_n;
        x /= 10;
    }

    // Compare taking into account whether the number length 
    // is even or odd.
    return x == rev_half || x == rev_half / 10;
}


int main(int argc, char** argv)
{
    std::cout << "1221: " 
            << (is_palindrome(1221) ? "true" : "false") << std::endl;
    std::cout << "101: " 
            << (is_palindrome(101) ? "true" : "false") << std::endl;          
    std::cout << "34566543: " 
            << (is_palindrome(34566543) ? "true" : "false") << std::endl;
    std::cout << "9081809: " 
            << (is_palindrome(9081809) ? "true" : "false") << std::endl;
    std::cout << "45632: " 
            << (is_palindrome(45632) ? "true" : "false") << std::endl;
    std::cout << "98324: " 
            << (is_palindrome(98324) ? "true" : "false") << std::endl;
    return EXIT_SUCCESS;
}