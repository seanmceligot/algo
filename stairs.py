# vim: set makeprg=python
from typing import List


def next_two(n: int, cache: List[int]) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    # if n==2:
    #    return 2
    assert len(cache) >= n
    print(f"n {n} len{len(cache)}")
    if cache[n - 1] > 0:
        return cache[n - 1]
    a, b = next_two(n - 1, cache), next_two(n - 2, cache)
    print(f"call {n-1}={a} + {n-2}={b}")
    cache[n - 1] = a + b
    return cache[n - 1]


def climb_n_stairs(n: int) -> int:
    cache: List[int] = [-1] * n
    assert len(cache) == n
    return next_two(n, cache)


if __name__ == "__main__":
    assert climb_n_stairs(1) == 1
    assert climb_n_stairs(2) == 2
    assert climb_n_stairs(3) == 3
    assert climb_n_stairs(4) == 5
    assert climb_n_stairs(5) == 8
