#include <stdio.h>
#include <stdlib.h>


void fizzbuzz(int arg, int lower, int upper){
    for(int i=1; i<= arg; i++){
        if(i%lower == 0) 
            printf("Fizz");
        if(i%upper == 0)
            printf("Buzz");
        if(i%lower && i%upper)
            printf("%d",i);
        printf("\n");
    }
    printf("\n");
    printf("\n");
}


int main(int argc, char **argv){
    fizzbuzz(atoi(argv[1]), atoi(argv[2]), atoi(argv[3]));
}