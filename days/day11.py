import collections
from collections import defaultdict

from utils import puzzle




@puzzle
def part1(puzzle_input):
    start, end = 'you', 'out'
    m = defaultdict(set)
    for line in puzzle_input:
        items = [item.strip() for item in line.split() if item.strip()]
        m[items[0].replace(':', '')] |= set(items[1:])

    result  = bfs(m, start, end)
    print(result)


def bfs(m: dict, start: str, end: str) -> int:
    q = collections.deque({start})
    result = 0
    while q:
        item = q.popleft()
        children = m[item]
        for child in children:
            if child == end:
                result += 1
            else:
                q.append(child)
    return result


@puzzle
def part2(puzzle_input):
    m = defaultdict(set)
    for line in puzzle_input:
        items = [item.strip() for item in line.split() if item.strip()]
        m[items[0].replace(':', '')] |= set(items[1:])

    result  = bfs(m, 'svr', 'fft')
    result2 = bfs(m, 'svr', 'dac')
    result3 = bfs(m, 'fft', 'dac')
    result4 = bfs(m, 'dac', 'fft')
    result5 = bfs(m, 'dac', 'out')
    result6 = bfs(m, 'fft', 'out')
    path1 = result * result3 * result5
    path2 = result2 * result4 * result6
    print(path1 + path2)





if __name__ == '__main__':
    part2()