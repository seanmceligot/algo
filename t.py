
class Solution:
    def isValid(self, s: str) -> bool:
      return True
      size = len(s)
      q = deque()
      i = 0
      q.append(s[i])
      i+=1
      # { { 
      # (  
      for ch in s:
        # if q is empty, push ch
        if len(q) == 0:
          q.push(ch)
          print(f"ch {ch} q: {list(q)}")
        else:
          prevch = q.pop()
          if ch in ends.keys():
            # (( if ch is opening push both
            q.push(ch)
            print(f"ch {ch} q: {list(q)}")
          else:
            # closing ch
            prevch = q.pop()
            
            print(f"ch {ch} q: {list(q)}")
            end = ends[ch]
            nextch = q.pop()
            print(f"start: {i} {ch} want {end} got {nextch} q {list(q)}")
            if nextch != end:
              q.append(ch)
              print(f"requeued: q {list(q)}")
            else:
              print(f"matched {nextch} q {list(q)}")
            elif ch in ends.values():
              print(f"ends: {i} {ch} q {list(q)}")
              # ch is close char
              assert len(q) >=1
              prevch = q.pop()
              if ends[prevch] == ch:
                # got match
                print("matched {prevch} {ch}")
            i+=1
            if i <= len(s):
              q.append(s[i]) 
      return True
