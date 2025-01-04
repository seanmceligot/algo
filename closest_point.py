def dist(points: List[int]) -> float:
    assert len(points) == 2
    x, y = points
    return math.sqrt(math.pow(x - 0, 2) + math.pow(y - 0, 2))


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        retlist = []
        with_dist = []
        i = 0
        with_dist: List[Tuple[float, List[int]]]
        for xy in points:
            with_dist.append((dist(xy), xy))
        with_dist.sort(key=lambda tp: tp[0])
        print(f"len with_dist {len(with_dist)}")
        for dist_pt in with_dist[:k]:
            retlist.append(dist_pt[1])
        return retlist
