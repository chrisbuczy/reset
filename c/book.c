// book.c
// following c how to program book
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include "book.h"



void main() {
    double avg = 0;
    int count = 0;
    int grade = 0;

    printf("\ninput a grade: ");
    scanf("%d", &grade);
    while (grade != -1) {

        count++;

        avg += grade;
        printf("%.2f", avg);

        printf("\ninput a grade: ");
        scanf("%d", &grade);
    }

    avg /= count;
    printf("\n%.2f\n", avg);
}