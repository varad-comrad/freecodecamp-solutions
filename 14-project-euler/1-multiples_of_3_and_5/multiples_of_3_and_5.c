#include <stdio.h>

int sum_of_multiples_of_3_and_5(int upper_bound){
    int sum = 0;
    for(int i=0; i<upper_bound; i++)
        if(i%3==0 || i%5==0)
            sum+=i;
    return sum; 
}

int main(int argc, char **argv){
    int upper_bounds[] = {10,49,1000,8456,19564}; 
    for(int i = 0; i < 5; i++)
        printf("%d ", sum_of_multiples_of_3_and_5(upper_bounds[i]));
}