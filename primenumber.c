#include<stdio.h>

int main(){
    int  num;
    int *ptr;
    num=10;
    ptr=&num;

    printf("The value of num variable is: %d\n",num);
    printf("The value stored at adress in pointer ptr is: %d\n",*ptr);
    printf("The adress of variable num is: %d\n",&num);
    printf("The value stored at pointer ptr is: %d\n",ptr);
// pointer arithmetic
         printf("The value stored at pointer ptr is: %d\n",ptr+1);
            printf("The value stored at pointer ptr is: %d\n",ptr-1);

   return 0;

}