#include <stdio.h>
#include <math.h>
int main() {
    int number;
    int i ;
    scanf("%d", &number);
    
    for(i = 1; i <= number; i++){
        
        printf("%d %d %d\n", i, i*i, i*i*i);
        
    }
    return 0;
}