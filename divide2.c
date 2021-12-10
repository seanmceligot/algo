#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int MIN = -2147483648;
int MAX = 2147483647;
int min(int a, int b) {
	if (a < b) {
	    return a;
	}
	return b;
}
int max(int a, int b) {
	if (a > b) {
	    return a;
	}
	return b;
}
int negate(int n) {
  if (n <= MIN) {
    printf("negate %d = MAX\n", n);
    return MAX;
  }
  if (n > MAX) {
    printf("negate %d = MIN\n", n);
    return MIN;
  }
    
  printf("negate %d = %d\n", n, -n);
  return -n;
}
bool optimize = true;
void div_and_check(int dividend, int divosor) {

  int expected = divosor == -1 ? negate(dividend) : dividend / divosor;
  expected = min(expected, MAX);
  expected = max(expected, MIN);
  assert(expected >= MIN);
  assert(expected <= MAX);
  int actual = (int)divide(dividend, divosor);
  if (actual != expected) {
    printf("%d / %d expected %d got %d\n", dividend, divosor, expected, actual);
    assert(actual == expected);
  } else {
    printf("PASS %d / %d expected %d got %d\n", dividend, divosor, expected, actual);
  }
}

int main(int argc, char **argv) {
  // div_and_check(10, 3);
  // div_and_check(1, 3);
  // div_and_check(9, 3);
  // div_and_check(9, 2);
  // div_and_check(9, 1);
  // div_and_check(9, -3);
  // div_and_check(9, 9);
  // div_and_check(0, -3);
  // div_and_check(MAX, MAX);
  // div_and_check(MIN, MIN);
  // div_and_check(MAX, 1);
  // div_and_check(9, 9);
  //div_and_check(MIN, -1);
  //div_and_check(MIN, 1);
  //div_and_check(2147483647, 1);
  //div_and_check(2147483647, 2);
  div_and_check(-2147483648, 2);
  //div_and_check(-2147483648, 1);
}
