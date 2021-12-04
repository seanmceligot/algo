# vim:set makeprg=python
#import math
MIN = -2147483648
assert MIN == -2** 31
MAX = 2147483647
assert MAX == 2**31-1
optimize = True

#def debug(unused ): # type: ignore
#    pass
def debug(s:str):
    print(s)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        debug(f"dividend {dividend} divisor {divisor} looking for {int(dividend/divisor)}")
        assert divisor != 0
        debug(f"MIN={min}")
        debug(f"MAX={max}")
        if dividend == divisor:
            return 1
        if divisor == 1:
            return max(dividend , MIN)
        if divisor == -1:
            return min(-dividend , MAX)
        negate = False
        if divisor < 0:
            divisor = -divisor
            negate = not negate
        if dividend > 0:
            neg_dividend = -dividend
        else:
            negate = not negate
            neg_dividend= dividend
        assert neg_dividend <= 0
        quotient = 0
        number = 0
        if optimize:
            debug(f"divisor {divisor} < dividend {dividend} optimize={divisor < dividend}")
            if divisor < dividend:
                # neg_multiples = -div, -dev*2, -div*3,...
                neg_multiples = -divisor
                assert neg_multiples < 0
                times = 1
                while neg_multiples+neg_multiples >= neg_dividend:
                    #debug(f"{divisor} * {times} = {neg_multiples}")
                    neg_multiples = neg_multiples+neg_multiples 
                    times += times
                    #assert neg_multiples<= 0
                    #debug(f"{neg_multiples+neg_multiples} >= {neg_dividend}")
                    #assert times < abs(dividend)
                #debug(f"{divisor} * {times} = {neg_multiples}")
                number = neg_multiples
                quotient = times
                number = neg_multiples
                debug(f"optimized number {number} quotient {quotient} divisor {divisor}")
        while number-divisor >= neg_dividend:
            quotient = quotient + 1
            number = number - divisor
            #debug(f"number {number} quotient {quotient} divisor {divisor}")
        assert number >= MIN
        #assert number <= max

        if negate:
            quotient = -quotient
        if quotient > MAX:
            return MAX
        # debug(max)
        if quotient < MIN:
            return MIN
        return quotient


solution = Solution()


def div(dend, dor):
    expected = int(dend/dor)
    expected = min(expected, MAX)
    expected = max(expected, MIN)
    assert expected >= MIN
    assert expected <= MAX
    actual= int(solution.divide(dend, dor))
    if actual != expected:
        print(f"{dend} / {dor} expected {expected} got {actual}")
        assert actual == expected
    else:
        print(f"PASS {dend} / {dor} = {expected} == {actual}")


if __name__ == "__main__":
    s = Solution()
    div(10, 3)
    div(1, 3)
    div(9, 3)
    div(9, 2)
    div(9, 1)
    div(9, -3)
    div(9, 9)
    div(0, -3)
    div(MAX, MAX)
    div(MIN, MIN)
    div(MAX, 1)
    div(9, 9)
    div(MIN, -1)
    div(MIN, 1)
    #div(2147483647, 2)
