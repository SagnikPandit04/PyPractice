#include <stdio.h>

void main() {
    
    double a,b,result;
    char op;
    
    printf("Enter two numbers: ");
    scanf("%lf%lf",&a,&b);
    printf("Select an operator [+, -, *, /]: ");
    scanf(" %c",&op);
    
    if (op == '+') {
        result = a + b;
        printf("Result: %.2lf\n", result);
    } else if (op == '-') {
        result = a - b;
        printf("Result: %.2lf\n", result);
    } else if (op == '*') {
        result = a * b;
        printf("Result: %.2lf\n", result);
    } else if (op == '/') {
        if (b != 0) {
            result = a / b;
            printf("Result: %.2lf\n", result);
        } else {
            printf("Division by zero is not allowed \n");
        }
    } else {
        printf("Enter valid operator \n");
    }
    
}