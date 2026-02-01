#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
  int b = 2025;
  int d = 9999;
  char c = '/';
  char a[50] = "JIS";
  char a1[50] = "I'm a Student my id : \n";
  FILE *fp = NULL;
  fp = fopen("abc.txt", "w");
  if (fp == NULL)
  {
    printf("Error");
    exit(1);
  }
  fputs(a1,fp);
  fprintf(fp,"%s%c%d%c%d",a,c,b,c,d);
  // for(int i =0 ;i != strlen(a);i++)
  // fputc(a[i],fp);
  fclose(fp);
  return 0;
}