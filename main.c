#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define READ_TIMES 999999999
#define TEST_RANGE 24

int main() {

  int size = pow(2, 23);

  srand(time(NULL));

  int *block = (int*)calloc(size, sizeof(int));

  int j, temp;
  clock_t start = clock(), total_time;

  for (j = 0; j < READ_TIMES; ++j) temp += block[rand() % size];

  total_time = clock() - start;

  printf("At size: %ldB, we need %lf sec\n", size*sizeof(int), (double)total_time / CLOCKS_PER_SEC);

  return 0;
  
}