from typing import Optional, List
from collections import deque

  def maxDepth(self, root: Optional[TreeNode]) -> int:
        if  root is None:
            return 0
        
        queue = deque();
        max_level = level = 1
        queue.append( (level, root)) 
        while len(queue) != 0:
            level, cur = queue.popleft()
            max_level = max(level, max_level)
            if cur.left is not None:
                queue.append((level+1, cur.left))
            if cur.right is not None:
                queue.append((level+1, cur.right))
        return max_level
