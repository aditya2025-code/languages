#include <stdio.h>
#include <stdlib.h>
int main()
{
  char ch;
  char ch1[50] = "I am ";
  FILE *fp = NULL;
  fp = fopen("abc.txt", "r+");
  if (fp == NULL)
  {
    printf("Error:No file Exist");
    exit(1);
  }
  while(!feof(fp))
  {
    ch = fgetc(fp);
    printf("%c",ch);
  }
  fputs(ch1, fp);
  fclose(fp);
  return 0;
}