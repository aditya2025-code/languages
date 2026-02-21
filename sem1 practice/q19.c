// Q19. Sum of series: 1² + 2² + 3² + … + n². Write a C program to find the sum of squares of first n natural numbers using a loop.

#include <math.h>
#include <stdio.h>

int main()
{
  int i, n, sum = 0;
  printf("Enter n'th term: ");
  scanf("%d", &n);
  for (i = 1; i <= n; i++)
    sum += pow(i, 2);
  printf("Sum of serise: %d", sum);
  return 0;
}