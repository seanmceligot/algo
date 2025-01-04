from typing import List


def new_grid(n_rows: int, n_cols: int, val: bool) -> List[List[bool]]:
    grid = []
    for _ in range(n_rows):
        grid.append([val for _ in range(n_cols)])
    return grid


def visit_spot(
    grid: List[List[str]],
    n_rows: int,
    n_cols: int,
    rowi: int,
    coli: int,
    visited: List[List[bool]],
):
    print(f"visit_spot [{rowi}][{coli}] n_cols {n_cols} n_rows {n_rows}")
    if rowi < 0 or coli < 0:
        return
    if rowi >= n_rows or coli >= n_cols:
        return
    if visited[rowi][coli]:
        return
    visited[rowi][coli] = True
    if grid[rowi][coli] == "1":
        visit_nearby(grid, n_rows, n_cols, rowi, coli, visited)


def visit_nearby(
    grid: List[List[str]],
    n_rows: int,
    n_cols: int,
    rowi: int,
    coli: int,
    visited: List[List[bool]],
):
    visit_spot(grid, n_rows, n_cols, rowi + 1, coli, visited)  # up
    visit_spot(grid, n_rows, n_cols, rowi - 1, coli, visited)  # down
    visit_spot(grid, n_rows, n_cols, rowi, coli - 1, visited)  # left
    visit_spot(grid, n_rows, n_cols, rowi, coli + 1, visited)  # right


class Solution:
    def numIslands(self, grid: List[List[str]], n_cols: int, n_rows: int) -> int:
        visited = new_grid(n_rows, n_cols, False)
        print(
            f"grid {len(grid)} visited {len(visited)} n_rows {n_rows} n_cols {n_cols}"
        )
        assert len(visited) == len(grid)
        assert len(visited[0]) == len(grid[0])
        print(f"visited {visited}")
        islands = 0
        for rowi in range(n_rows):
            for coli in range(n_cols):
                if not visited[rowi][coli]:
                    visited[rowi][coli] = True
                    if grid[rowi][coli] == "1":
                        islands += 1
                        visit_nearby(grid, n_rows, n_cols, rowi, coli, visited)
        return islands


if __name__ == "__main__":
    solution = Solution()
    gridi = [
        [1, 1, 1],  # cols = 3
        [0, 1, 0],
        [1, 0, 0],
        [1, 0, 1],  # rows = 4
    ]
    grid = [[str(y) for y in x] for x in gridi]
    print(grid)
    n_rows = len(grid)
    n_cols = len(grid[0]) if n_rows > 0 else 0
    assert n_rows == 4
    assert n_cols == 3
    assert grid[n_rows - 1][n_cols - 1] == "1"
    n = solution.numIslands(grid, n_cols, n_rows)
    assert n == 3

    grid = [["1"]]
    n_rows = len(grid)
    n_cols = len(grid[0]) if n_rows > 0 else 0
    n = solution.numIslands(grid, n_cols, n_rows)
    assert n == 1

    grid = [["0"]]
    n_rows = len(grid)
    n_cols = len(grid[0]) if n_rows > 0 else 0
    n = solution.numIslands(grid, n_cols, n_rows)
    assert n == 0

    grid = [[]]
    n_rows = len(grid)
    n_cols = len(grid[0]) if n_rows > 0 else 0
    n = solution.numIslands(grid, n_cols, n_rows)
    assert n == 0
