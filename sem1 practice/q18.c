// Q18. Write a C program to compute a^b (a to the power b) using a loop (without using pow()).

#include <stdio.h>

int main()
{
  int i, n, e, power=1;
  printf("Enter the number and exponet: ");
  scanf("%d %d", &n, &e);
  for (i = 1; i <= e; i++)
    power *= n;
  printf("%d^%d = %d",n,e, power);
  return 0;
}