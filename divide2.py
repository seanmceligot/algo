# vim:set makeprg=python
# import math
MIN = -2147483648
assert MIN == -(2**31)
MAX = 2147483647
assert MAX == 2**31 - 1
optimize = True

# def debug(unused ): # type: ignore
#    pass
MAX_INT = (1 << 31) - 1


def debug(s: str):
    print(s)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        debug(
            f"dividend {dividend} divisor {divisor} looking for {int(dividend/divisor)}"
        )
        assert divisor != 0
        if dividend == 0:
            return 0
        sign = 1 if ((dividend < 0) ^ (divisor < 0)) else 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            debug(f"while dividend {dividend} >= divisor {divisor}")
            k = 0
            while dividend >= divisor << (k + 1):
                # debug(f"while dividend {dividend}  >= divisor {divisor} <<{k+1}  [{divisor<<(k+1)}]")
                k += 1
            dividend -= divisor << k
            debug(f"k {k} divisor<<k {divisor<<k} res+={1<<k}")
            # debug(f"subtract (divisor<<k) from divident = {dividend}")
            # debug(f"dividend {dividend} divisor {divisor} looking for {int(dividend/divisor)}")
            res += 1 << k
            debug(f"res {res}")
        return -res if sign else (res if res <= MAX_INT else MAX_INT)


solution = Solution()


def div(dend, dor):
    expected = int(dend / dor)
    expected = min(expected, MAX)
    expected = max(expected, MIN)
    assert expected >= MIN
    assert expected <= MAX
    actual = int(solution.divide(dend, dor))
    if actual != expected:
        print(f"{dend} / {dor} expected {expected} got {actual}")
        assert actual == expected
    else:
        print(f"PASS {dend} / {dor} = {expected} == {actual}")


if __name__ == "__main__":
    s = Solution()
    # div(10, 3)
    # div(1, 3)
    # div(9, 3)
    # div(9, 2)
    # div(9, 1)
    # div(9, -3)
    # div(9, 9)
    # div(0, -3)
    # div(MAX, MAX)
    # div(MIN, MIN)
    # div(MAX, 1)
    # div(9, 9)
    # div(MIN, -1)
    # div(MIN, 1)
    div(2147483647, 2)
