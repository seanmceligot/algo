#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int MIN = -2147483648;
int MAX = 2147483647;
int max(int a, int b) {
  if (a > b) {
    return a;
  }
  return b;
}
int min(int a, int b) {
  if (a < b) {
    return a;
  }
  return b;
}

bool optimize = true;

int divide(int dividend, int divisor) {
  assert(divisor != 0);
  if (dividend == divisor) {
    return 1;
  }
  if (divisor == 1) {
    return max(dividend, MIN);
  }
  if (divisor == -1) {
    if (dividend == MIN) {
      return MAX;
    } else {
      return min(-dividend, MAX);
    }
  }
  bool negate = false;
  if (divisor < 0) {
    divisor = -divisor;
    negate = !negate;
  }
  int neg_dividend = 0;
  if (dividend > 0) {
    neg_dividend = -dividend;
  } else {
    negate = !negate;
    neg_dividend = dividend;
  }
  assert(neg_dividend <= 0);
  int quotient = 0;
  int number = 0;
  if (optimize) {
    printf("divisor %d < dividend %d optimize=%d\n", divisor, dividend,
           divisor - dividend);
    if (divisor < dividend) {
      // neg_multiples = -div, -dev*2, -div*3,...
      int neg_multiples = -divisor;
      assert(neg_multiples < 0);
      int times = 1;
      while (neg_multiples >= neg_dividend - neg_multiples) {
        printf("%d * %d = %d\n", divisor, times, neg_multiples);
        neg_multiples = neg_multiples >> 1;
        times += times;
        assert(neg_multiples <= 0);
        printf("%d + %d >= %d\n", neg_multiples, neg_multiples, neg_dividend);
        assert(times < abs(dividend));
      }
      // debug(f"{divisor} * {times} = {neg_multiples}")
      number = neg_multiples;
      quotient = times;
      number = neg_multiples;
      printf("optimized number %d quotient %d divisor %d\n", number, quotient,
             divisor);
    }
  }
  while (number - divisor >= neg_dividend) {
    quotient = quotient + 1;
    number = number - divisor;
    // debug(f"number {number} quotient {quotient} divisor {divisor}")
  }
  assert(number >= MIN);
  // assert number <= max

  if (negate) {
    quotient = -quotient;
  }
  if (quotient > MAX) {
    return MAX;
  }
  // debug(max)
  if (quotient < MIN) {
    return MIN;
  }
  return quotient;
}

void div_and_check(int dend, int dor) {

  int expected = dor == -1 ? -dend : dend / dor;
  expected = min(expected, MAX);
  expected = max(expected, MIN);
  assert(expected >= MIN);
  assert(expected <= MAX);
  int actual = (int)divide(dend, dor);
  if (actual != expected) {
    printf("%d / %d expected %d got %d\n", dend, dor, expected, actual);
    assert(actual == expected);
  } else {
    printf("PASS %d / %d expected %d got %d\n", dend, dor, expected, actual);
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
  div_and_check(MIN, -1);
  div_and_check(MIN, 1);
  div_and_check(2147483647, 1);
  div_and_check(2147483647, 2);
  div_and_check(-2147483648, 2);
  div_and_check(-2147483648, 1);
}
