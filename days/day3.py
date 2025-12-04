"""

"""
from utils import puzzle


@puzzle
def part1(puzzle_input):
    total = 0
    for bank in puzzle_input:
        first, second = 0, 0
        for i, battery in enumerate(bank):
            val = int(battery)
            if val > first and i != len(bank) - 1:
                first = val
                second = 0
            elif val > second:
                second = val
        total += int(str(first) + str(second))
        print(f'Bank: {bank}, max joltage:{int(str(first) + str(second))}')
    print(total)

@puzzle
def part2(puzzle_input):
    total = 0
    for bank in puzzle_input:
        max_digits = [0] * 12
        left = 0
        for i, battery in enumerate(bank):
            val = int(battery)
            if val > max_digits[left] and i != len(bank) - 12:
                max_digits[left] = val
                left += 1
            elif val > second:
                second = val
        total += int(str(first) + str(second))
        print(f'Bank: {bank}, max joltage:{int(str(first) + str(second))}')
    print(total)



if __name__ == '__main__':
    part2()