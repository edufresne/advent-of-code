from utils import puzzle


def solve_single(line: str) -> int:
    pass


@puzzle
def part2(puzzle_input):
    val = 0
    for line in puzzle_input:
        val += solve_single(line)
    print(val)

def convert_to_digit(s) -> int | None:
    s = s.lower()
    if s == 'one':
        return 1
    elif s == 'two':
        return 2
    elif s == 'three':
        return 3
    elif s == 'four':
        return 4
    elif s == 'five':
        return 5
    elif s == 'six':
        return 6
    elif s == 'seven':
        return 7
    elif s == 'eight':
        return 8
    elif s == 'nine':
        return 9
    else:
        return None



if __name__ == '__main__':
    part2()