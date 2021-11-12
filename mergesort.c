#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef size_t idx_t;
typedef uint8_t val_t;

void printa(const char *label, val_t *ar, idx_t lindex, idx_t rindex) {
  printf("%s: ", label);
  for (idx_t i = lindex; i <= rindex; i++) {
    printf("%d, ", ar[i]);
  }
  printf("\n");
}

void merge(val_t *ar, idx_t lindex, idx_t middle, idx_t rindex, val_t *tmp) {
  printf("merge %lu %lu %lu\n", lindex, middle, rindex);
  printa("merge", ar, lindex, rindex);
  idx_t left_read = lindex;
  idx_t right_read = middle + 1;
  idx_t write_index = lindex;

  while (left_read <= middle && right_read <= rindex) {
    printf("compare %d %d\n", ar[left_read], ar[right_read]);
    if (ar[left_read] <= ar[right_read]) {
      // left is smaller
      tmp[write_index] = ar[left_read];
      printa("left", tmp, lindex, write_index);
      left_read++;
      write_index++;
    } else {
      // right is smaller
      tmp[write_index] = ar[right_read];
      printa("right", tmp, lindex, write_index);
      right_read++;
      write_index++;
    }
  }
  while (left_read <= middle) {
    tmp[write_index] = ar[left_read];
    printa("finish left", tmp, lindex, write_index);
    left_read++;
    write_index++;
  }
  while (right_read <= rindex) {
    tmp[write_index] = ar[right_read];
    printa("finish left", tmp, lindex, write_index);
    right_read++;
    write_index++;
  }
  for (idx_t p = lindex; p <= rindex; p++) {
    ar[p] = tmp[p];
    printa("finish right ", tmp, lindex, write_index);
  }
  printa("after merge", ar, lindex, rindex);
}
void mergeSort(val_t ar[],idx_t lindex, id_t rindex, val_t* tmp)  {
   if(lindex < rindex) {
      idx_t middle = (lindex+ rindex) /2;
      mergeSort(ar,lindex,middle, tmp);
      mergeSort(ar,middle+1,rindex, tmp);
      merge(ar,lindex,middle,rindex, tmp);
   }
}

int main() {
  val_t ar[] = {3, 7, 9, 2, 6, 9, 1, 8, 2};
  idx_t N = sizeof(ar) / sizeof(val_t);
  val_t *tmp = (val_t *)malloc(sizeof(ar));
  mergeSort(ar, 0, N - 1, tmp);
  return 0;
}
