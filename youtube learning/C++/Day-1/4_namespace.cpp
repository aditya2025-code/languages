#include <iostream>

/*
int main()
{
    int x = 0;
    int x = 1; // its en error because we can't initilize both element twice
    std::cout << x;
    return 0;
}
*/

/*

Here comes namespace. it's provide a solution for preventing name
conflicts in large projects. Each entity needs a unique name . A
namespace allows for indentically named entities as long as the
namespace are different.

*/
/*
// This is an example of namespace

namespace frist{
    int x = 1;
}

namespace second{
    int x = 2;
}

int main(){
    int x = 0;
    std::cout << x << '\n'; // 0
    std::cout << frist::x << '\n'; // 1 becuase this x prefix by frist . frist::x
    std::cout << second::x << '\n'; // 2 becuase this x prefix by second . second::x
    return 0;
}
*/
/*
// Another we can use this way

int main(){
    using namespace std; // Mentioning this template , we dont need to type std repeatedly in our program 
     
    string name = "Aditya Das"; // Here we don't mention std but still its work

    // Same here
    cout << name ; // Aditya Das

    return 0;
}
*/