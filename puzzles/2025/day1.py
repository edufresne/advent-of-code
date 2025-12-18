"""
Solution to the day one problem. The starting solution just uses easy modulo math. The second solution when the
counting requirements change for # of passovers on 0, do individual int incrementing but I think this could also be done
with modulo math + a formula. Might try and improve later.
"""

from utils import puzzle


@puzzle
def part1(puzzle_input: list[str]):
    pos = 50
    number_of_zeros = 0
    print(f"Starts at {pos}")
    for item in puzzle_input:
        direction = item[0]
        distance = int(item[1:])
        print(f"Processing: {item}")
        if direction == "L":
            distance = -distance

        pos = (pos + distance) % 100
        print(f"New pos is: {pos}")
        if pos == 0:
            number_of_zeros += 1

    print(f"Answer: {number_of_zeros}")


@puzzle
def part2(puzzle_input: list[str]):
    pos = 50
    number_of_zeros = 0
    print(f"Starts at {pos}")
    for item in puzzle_input:
        direction = item[0]
        distance = int(item[1:])
        delta = 1
        print(f"Processing: {item}")
        if direction == "L":
            delta = -delta

        while distance != 0:
            pos += delta
            distance -= 1
            if pos == -1:
                pos = 99
            elif pos == 100:
                pos = 0
            if pos == 0:
                print(f"Found zero at distance: {distance}")
                number_of_zeros += 1

        print(f"New pos is: {pos}")

    print(f"Answer: {number_of_zeros}")


if __name__ == "__main__":
    part2()
