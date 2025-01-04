import time


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hsize = len(haystack)
        nsize = len(needle)
        if nsize == 0:
            return 0
        for i in range(0, hsize - nsize + 1):
            print(f"{haystack[i:i+nsize]} !? {needle}")
            if haystack[i : i + nsize] == needle:
                return i
        ###          for j in range(nsize):
        ###            ch1 = haystack[i+j]
        ###            ch2 = needle[j]
        ###            if ch1 != ch2:
        ###              #print(f"{ch1} {ch2} {i} {j} no match (brea)")
        ###              break
        ###            #print(f"{ch1} {ch2} {i} {j} match (continue)")
        ###            if j == nsize-1:
        ###              #print(f"{ch1} {ch2} {i} {j} final match {haystack[i:i+j]}")
        ###              return i
        return -1


sol = Solution()

if __name__ == "__main__":
    start = time.time()
    print("hello")
    a = "a" * 1000 + "b"
    b = "a" * 1000 + "b"
    assert sol.strStr(a, b) == 0
    end = time.time()
    print(end - start)
