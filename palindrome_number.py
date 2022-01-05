 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        ln = len(s)
        if ln%2==0:
            return False
        print("x", x)
        print("len", ln)
        low: int = 0;
        high: int = ln-1
        while low<high:
            print(f"low: {low} high {high}")
            if s[low] != s[high]:
                print(f"{s[low]} != {s[high]}")
                return False
            print(f"{s[low]} == {s[high]}")
            low+=1
            high-=1
        return True

sol = Solution()
if __name__ == "__main__":
    assert sol.isPalindrome(4321234) == True
    assert sol.isPalindrome(1321234) == False
