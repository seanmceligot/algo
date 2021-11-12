#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int idx_t;
typedef int val_t;

void printa(const char *label, val_t *ar, idx_t lindex, idx_t rindex) {
  printf("%s: ", label);
  for (idx_t i = lindex; i <= rindex; i++) {
    printf("%d, ", ar[i]);
  }
  printf("\n");
}

void merge(int *left_array, int left_array_size, int left_count,
           int *right_array, int right_array_size, int right_count) {

  int left_read = 0;
  int right_read = 0;
  int *tmp = (int *)malloc(sizeof(int) * (left_count + right_count));
  int tmp_index = 0;
  int *dest = left_array;

  printa("left: before merge", left_array, 0, left_count - 1);
  printa("right: before merge", right_array, 0, right_count - 1);
  while (left_read < left_count && right_read < right_count) {
    printf("compare [%d]%d < [%d]%d\n", left_read, left_array[left_read], right_read, right_array[right_read]);
    if (left_array[left_read] <= right_array[right_read]) {
      tmp[tmp_index] = left_array[left_read];
      tmp_index++;
      left_read++;
    } else {
      tmp[tmp_index] = right_array[right_read];
      tmp_index++;
      right_read++;
    }
  }
  while (left_read < left_count) {
    tmp[tmp_index] = left_array[left_read];
    tmp_index++;
    left_read++;
  }
  while (right_read < right_count) {
    tmp[tmp_index] = right_array[right_read];
    tmp_index++;
    right_read++;
  }
  dest = (int*) memcpy(dest, tmp, left_array_size*sizeof(int));
  printa("after merge", left_array, 0, left_count + right_count - 1);
  free(tmp);
}
int _main() {
  int la[] = {1, 2, 3, 0, 0, 0, -1, -1, -1};
  int m = 3;
  int ra[] = {2, 5, 6};
  int n = 3;

  merge(la, m + n, m, ra, n, n);
  return 0;
}
int main() {
  int la[] = {1};
  int m = 1;
  int ra[] = {};
  int n = 0;

  merge(la, m + n, m, ra, n, n);
  return 0;
}
