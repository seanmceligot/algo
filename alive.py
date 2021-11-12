from typing import Tuple, List, Dict


alive_by_year: Dict[int,int] = dict()

def main():   
    ar: List[Tuple[int,int]]= [(1900, 1950), (1899, 1900)]
    print(ar) 
    for b, d in ar:
        for y in range(b,d+1):
            count = alive_by_year.get(y, 0)
            alive_by_year[y] = count + 1
    print(alive_by_year)
    j

if __name__ == "__main__":
    main();
