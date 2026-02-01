#include <stdio.h>
#include <stdlib.h>
int main()
{
  char ch[50];
  FILE *fp = NULL;
  fp = fopen("abc.txt", "r");
  if (fp == NULL)
  {
    printf("Error:No file Exist");
    exit(1);
  }
  while (!feof(fp))
  {
    fgets(ch, 20, fp);
    printf("%s", ch);
  }
  /*while (!feof(fp))
  {
    ch = fgetc(fp);
    printf("%c", ch);
  }*/
  fclose(fp);
  return 0;
}