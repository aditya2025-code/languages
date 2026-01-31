#include <stdio.h>

struct student
{
  int rollno;
  char name[15];
  float marks;
} s = {01, "Aditya", 10};

// struct student s1 ={02,"Arif",9};
struct student s1;
int main()
{
  printf("s info = %d %s %.2f\n", s.rollno, s.name, s.marks);
  printf("Enter rollno. name & marks: ");
  scanf("%d %s %f", &s1.rollno, &s1.name, &s1.marks);
  printf("s1 info = %d %s %.2f", s1.rollno, s1.name, s1.marks);
  return 0;
}

// OUTPUT:
/*
s info = 1 Aditya 10.00
Enter rollno. name & marks: 2 adi 9
s1 info = 2 adi 9.00
*/