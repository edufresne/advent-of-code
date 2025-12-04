"""
Solution to the day two problem. This is all string manipulation with a bit of modulo math optimization.
It starts off easy, you simply need to start off by comparing the left and right side to see if a number repeats. This
can only happen on a string with an even number of digits. Then in part two, you need to check if it is containing only
repetitions. Again, you can do the same calculation but check for repetitions by the segment length. You can then
optimize by only checking segments that are evenly divisible by the number of digits. ie. 1111 can be broken up into
4 segments and two segments of 1s. A string like 1231234 can't contain repetitions as you can't evenly break it apart.
"""
from utils import puzzle


@puzzle
def part1(puzzle_input):
    item = puzzle_input[0]
    id_ranges = [tuple(item.split('-')) for item in item.split(',')]
    invalid_ids = 0
    for start, end in id_ranges:
        start, end = int(start), int(end)
        for i in range(start, end + 1):
            s = str(i)
            if len(s) % 2 != 0:
                continue
            mid_point = len(s) // 2
            if s[mid_point:] == s[:mid_point]:
                print(s)
                invalid_ids += int(s)

    print(invalid_ids)


@puzzle
def part2(puzzle_input):
    item = puzzle_input[0]
    id_ranges = [tuple(item.split('-')) for item in item.split(',')]
    invalid_ids = 0
    for start, end in id_ranges:
        start, end = int(start), int(end)
        print(f'Searching: {(start, end)}')
        for i in range(start, end + 1):
            s = str(i)
            length = len(s)
            segment_lengths = [j for j in range(1, (length // 2) + 1) if length % j == 0]
            invalid = False
            for segment_length in segment_lengths:
                segments = [s[j:j + segment_length] for j in range(0, length, segment_length)]
                if all(item == segments[0] for item in segments):
                    invalid_ids += int(s)
                    print(f'Invalid ID: {s} -> {segments}')
                    invalid = True
                    break
            if not invalid:
                print(f'Valid ID: {s}')

    print(invalid_ids)

if __name__ == '__main__':
    part2()