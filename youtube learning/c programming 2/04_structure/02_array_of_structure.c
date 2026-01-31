#include <stdio.h>

struct employee
{
  int id;
  char name[20];
  char dept[20];
};

struct employee E[5];

int main()
{
  int i;
  for (i = 0; i < 5; i++)
  {
    printf("Enter %d id,name,department: \n", i + 1);
    scanf("%d", &E[i].id);
    scanf(" %[^\n]%*c", E[i].name);
    scanf(" %[^\n]%*c", E[i].dept);
  }
  for (i = 0; i < 5; i++)
  {
    printf("Info of Employee %d", i + 1);
    printf("\n\t%d\t%s\t%s\n", E[i].id, E[i].name, E[i].dept);
  }

  return 0;
}
// OUTPUT:
/*
Enter 1 id,name,department:
1001
Aditya Das
BCA
Enter 2 id,name,department:
1002
Asish Sarkar
BCA
Enter 3 id,name,department:
1003
Arif Alam SK
BCA
Enter 4 id,name,department:
1004
Amir Khan
BCA
Enter 5 id,name,department:
1005
Anaj Shek
BCA
Info of Employee 1
        1001    Aditya Das      BCA
Info of Employee 2
        1002    Asish Sarkar    BCA
Info of Employee 3
        1003    Arif Alam SK    BCA
Info of Employee 4
        1004    Amir Khan       BCA
Info of Employee 5
        1005    Anaj Shek       BCA
*/