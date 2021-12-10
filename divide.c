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

int divide(int dividend, int divisor) { 
    printf("%d\n", dividend);
    printf("__\n");
    printf("%d\n", divisor);
    assert(negate(2)==-2);
    assert(negate(-2)==2);
    assert(negate(MIN)==MAX);
    assert(negate(MAX)==-2147483647);
    assert(divisor != 0);
    if (dividend == divisor) {
        return 1;
    }
    if (divisor == 1) {
        return max(dividend , MIN);
    }
    if (divisor == -1) {
        if (dividend == MIN) {
          return MAX;
        }
        return negate(dividend);
    }
    bool negate_result = false;
    if (divisor < 0) {
        divisor = divisor == MIN? MAX:negate(divisor);
        negate_result = !negate_result;
    }
    int neg_dividend=0;
    if (dividend > 0) {
        neg_dividend = negate(dividend);
    } else {
        negate_result = !negate_result;
        neg_dividend= dividend;
    }
    assert(neg_dividend <= 0);
    int quotient = 0;
    int number = 0;
    if (optimize) {
        printf("if divisor %d < dividend %d optimize\n", divisor, dividend);
        if (divisor < dividend) {
            // neg_multiples = -div, -dev*2, -div*3,...
            int neg_multiples = negate(divisor);
            assert(neg_multiples < 0);
            int times = 1;
            while (neg_multiples >= neg_dividend-neg_multiples) {
                printf("%d * %d = %d\n", divisor,times, neg_multiples);
                neg_multiples = neg_multiples <<1;
                times += times;
                printf("times %d\n", times);
                assert(neg_multiples<= 0);
                //assert(times < abs(dividend));
    	}
            //printf"{divisor} * {times} = {neg_multiples}")
            number = neg_multiples;
            quotient = times;
            number = neg_multiples;
            printf("optimized number %d quotient %d divisor %d\n", number, quotient, divisor);
    }
    }
    while (number >= neg_dividend+divisor) {
        quotient = quotient + 1;
        number = number - divisor;
        //printf"number {number} quotient {quotient} divisor {divisor}")
    }
    assert(number >= MIN);
    //assert number <= max

    if (negate_result) {
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
  div_and_check(MIN, -1);
  div_and_check(MIN, 1);
  div_and_check(2147483647, 1);
  div_and_check(2147483647, 2);
  div_and_check(-2147483648, 2);
  div_and_check(-2147483648, 1);
}
