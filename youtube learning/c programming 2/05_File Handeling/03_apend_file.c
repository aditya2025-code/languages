#include <stdio.h>
#include <stdlib.h>
int main()
{
  char c = 'A';
  char ch[50] = "My name Aditya";
  char ch1[50] = "This print side-by-side";
  FILE *fp = NULL;
  fp = fopen("abc.txt", "a");
  if (fp == NULL)
  {
    printf("Error:No file Exist");
    exit(1);
  }
  // fprintf(fp, "\n%s", ch);
  //  fputc(c,fp);
  fputs(ch1, fp);
  fclose(fp);
  return 0;
}