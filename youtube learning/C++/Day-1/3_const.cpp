#include<iostream>
int main(){

    // const which is constant , it is basically means an entity read-only and immutable after its initialization

    const int light_speed = 299792458; // Light speed cannot be changed
    /*
    light_speed = 20000000; // This is not posible to change a const variable

    std::cout << light_speed; // Error
    */

    // Same as -->

    const double PI = 3.14159;
    const int max_player = 50;

    return 0;
}