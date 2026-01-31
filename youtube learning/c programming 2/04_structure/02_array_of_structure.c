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
    printf("Enter %d id,name,department: \n", i+1);
    scanf("%d", &E[i].id);
    scanf(" %[^\n]%*c",E[i].name);
    scanf(" %[^\n]%*c",E[i].dept);
  }
  for (i = 0; i < 5; i++)
  {
    printf("Info of Employee %d", i+1);
    printf("\n\t%d\t%s\t%s\n", E[i].id, E[i].name, E[i].dept);
  }

  return 0;
}