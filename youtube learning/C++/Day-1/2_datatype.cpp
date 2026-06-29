#include <iostream>
int main()
{

    // Integer variable (Whole Number)

    int a = 10;
    int b = 500;
    int c = 2.5; // it's not integer it's float

    std::cout << c << '\n'; // 2

    // Double variable (Number including decimal)

    double price = 10.5;
    double cgpa = 7.89;

    std::cout << price << '\n'; // 10.5

    // Single Character

    char grade = 'A';
    char dollarSign = '$';

    std::cout << dollarSign << '\n'; // $

    // Boolean ( True(1) or False(0) )

    bool power = false;
    bool isgood = true;

    std::cout << power << '\n';  // 0
    std::cout << isgood << '\n'; // 1

    // String (Object that represent a sequence of text)

    std::string name = "Adi";
    std::string day = "Monday";
    std::string address = "Kalyani";

    // Now this is called String literal print the whole string

    std::cout << "Hello " << name << '\n'; // Hello Adi
    std::cout << "You get " << grade << " grade"; // You get A grade
    return 0;
}