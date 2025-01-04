from typing import Tuple, Optional


def read_two(s, s_len, index) -> Tuple[Optional[str], Optional[str]]:
    ch1 = None
    ch2 = None
    if index < s_len:
        ch1 = s[index]
    index += 1
    if index < s_len:
        ch2 = s[index]
    return ch1, ch2


def value(ch: str) -> int:
    if ch == "I":
        return 1
    elif ch == "V":
        return 5
    elif ch == "X":
        return 10
    elif ch == "L":
        return 50
    elif ch == "C":
        return 100
    elif ch == "D":
        return 500
    elif ch == "M":
        return 1000
    assert False


class Solution:
    def romanToInt(self, s: str) -> int:
        print(f"romanToInt {s}")
        s_len = len(s)
        index = 0
        number = 0
        while True:
            ch1, ch2 = read_two(s, s_len, index)
            index += 1
            if ch1 is None:
                print(f"return {number}")
                return number
            v1 = value(ch1)
            if ch2 is None:
                v1 = value(ch1)
                number += v1
                print(f"n + {v1} = {number}")
                return number
            v2 = value(ch2)
            print(f"v1 {v1} v2 {v2} n {number}")
            if v1 > v2 or v1 == v2:
                number += v1
                print(f"n + {v1} = {number}")
            else:
                # iv=4
                # v1=1
                # v2=5
                # v2(5) - v1(1) = 4
                number += v2 - v1
                index += 1  # parse both numbers
                print(f"n + {v2} - {v1} = {number}")


sol = Solution()

if __name__ == "__main__":
    assert sol.romanToInt("I") == 1
    assert sol.romanToInt("II") == 2
    assert sol.romanToInt("III") == 3
    assert sol.romanToInt("IV") == 4  ## best case O(n/2)
    assert sol.romanToInt("V") == 5
    assert sol.romanToInt("VI") == 6
    assert sol.romanToInt("XIV") == 14
