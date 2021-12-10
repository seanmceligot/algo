from collections import deque

close_to_open = { ")":'(', "]":'[', "}":'{' }
open_to_close = { "(":')', "[":']', "{":'}'}

def get_end(opening):
  return open_to_close[opening]

def get_start(closing):
  return close_to_open[closing]
  
assert get_end('(') == ')'
assert get_end('[') == ']'
assert get_end('{') == '}'
assert get_start('}') == '{'

def match(open, close):
    is_match = open_to_close[open] == close
    if is_match:
        assert close_to_open[close] == open
    return is_match

assert match('(', ')')
assert match('{', '}')
assert match('[', ']')

def is_open(ch):
    return ch in open_to_close

assert is_open('(')
assert not is_open(')')

##  [ open
##  add to q
##  [{ open
##  add to q
##  } close
##  match(pop, ch)

class Solution:
    def isValid(self, s: str) -> bool:
      q = deque()
      for ch in s:
        if is_open(ch):
            q.append(ch)
        else:
            if len(q) == 0:
                return False
            if not match(q.pop(), ch):
                return False
      return len(q) == 0
sol = Solution()


def main():
    assert sol.isValid("{[]}")
    assert not sol.isValid("{[]}[")
    assert sol.isValid("{[]}()")
    assert not sol.isValid("{}}")
    assert sol.isValid("{[]}")

if __name__=="__main__":
    main()
