import sys
from typing import Mapping


def fizzbuzz(n: int, rules: Mapping[int,str]) -> list[str]:
    ans: list[str] = []
    for i in range(1,n+1):
        aux: str = ''
        for idx, elem in rules.items():
            if i%idx == 0:
                aux+=elem
        ans.append(aux or str(i))
    return ans


def main():
    n = int(sys.argv[1])
    lower = int(sys.argv[2])
    upper = int(sys.argv[3])
    rules = {lower: "Fizz", upper: "Buzz"}
    print(*fizzbuzz(n, rules), sep='\n')

if __name__ == '__main__':
    main()