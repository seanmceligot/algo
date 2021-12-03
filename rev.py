# vim: set makeprg=python
from typing import Any,List,Optional

def reverse(ar: List[Any]) -> Optional[List[Any]]:

    if len(ar) > 0:
        r = reverse(ar[1:])
        if r:
            result = r + [ar[0]]  
            print(f"{r} + {ar[0]} = {result}")
            return result
        else:
            return [ar[0]]
    return None
    

if __name__ == "__main__":
    ar = [1,2,3]
    print(reverse(ar))

