// Q20. What is the meaning of header file in C? Describe 3 header file briefly with C program.

#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{
  int n, e, a;
  char name[10];
  printf("Enter Your name: ");
  scanf(" %s", name);
  printf("Enter number and exponet: ");
  scanf("%d %d", &n, &e);
  printf("Name -> ");
  for (int i = 0; i <= sizeof(strlen(name)); i++)
  {
    printf("%c", name[i]);
  }
  a = pow(n, e);
  printf("\n%d Power of %d -> %d", n, e, a);
  return 0;
}

// OUTPUT:
/*
Enter Your name: ADI
Enter number and exponet: 2 3
Name -> ADI
2 Power of 3 -> 8
*/