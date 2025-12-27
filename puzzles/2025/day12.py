"""
I can't believe how easy this one was. Was scared there was going to be a part 2. Simply take the max area of each shape
which is 3x3. The shape size doesn't matter because none of them fit together such that they can optimize enough space.
"""

from utils import puzzle


class PresentType(tuple):
    def area(self) -> int:
        result = 0
        for item in self:
            for space in item:
                if space == "#":
                    result += 1
        return result

    def full_area(self) -> int:
        return sum(len(item) for item in self)


@puzzle
def part1(puzzle_input):
    present_shapes = []
    line1, line2 = None, None
    dimensions: list = []
    requirements: list = []
    for i, line in enumerate(puzzle_input):
        if ":" not in line and line.strip():
            if line1 is None:
                line1 = line
            elif line2 is None:
                line2 = line
            else:
                present_shapes.append(PresentType((line1, line2, line)))
                line1, line2 = None, None
        if "x" in line:
            parts = line.split(":")
            dimensions.append(tuple(int(v) for v in parts[0].split("x")))
            requirements.append([int(val) for val in parts[1].split()])

    answer = 0
    for dimension, requirement in zip(dimensions, requirements):
        print(f"{dimension} - {requirement}")
        width, length = dimension
        area = width * length
        required_area = 0
        for i, present_requirement in enumerate(requirement):
            required_area += present_shapes[i].full_area() * present_requirement

        if area < required_area:
            print(f"No good: {requirement}")
        else:
            print(f"Good: {requirement}")
            answer += 1

    print(answer)


if __name__ == "__main__":
    part1()
