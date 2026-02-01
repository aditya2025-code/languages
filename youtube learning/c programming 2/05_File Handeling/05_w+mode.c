#include <stdio.h>
#include <stdlib.h>
int main()
{
  char ch;
  char ch1[50] = "I am iron man";
  FILE *fp = NULL;
  fp = fopen("abc.txt", "w+");
  if (fp == NULL)
  {
    printf("Error:No file Exist");
    exit(1);
  }
  fputs(ch1, fp);
  rewind(fp);
  while (!feof(fp))
  {
    ch = fgetc(fp);
    printf("%c", ch);
  }
  fclose(fp);
  return 0;
}