#include <stdio.h>
#include <stdlib.h>
int main()
{
  char ch;
  char ch1[50] = "\nI am a student my id:\nJIS******";
  FILE *fp = NULL;
  fp = fopen("a.txt", "a+");
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