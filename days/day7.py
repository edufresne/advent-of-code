"""
This one is pretty cool. At the start you have to just count the number of beams that you split but then the second
part you need to figure out the # of possibilities (timelines) on which path you can take. You an keep count of the #
of paths to get to where you are in the beam. When you hit a splitter, the # of possibilities gets split on each side.
Make sure you add up duplicate paths and then sum everything up together in the end.
"""

from utils import puzzle


@puzzle
def part1(puzzle_input):
    beams = {i for i, val in enumerate(puzzle_input[0]) if val == "S"}
    split_count = 0
    for i, line in enumerate(puzzle_input[1:]):
        beams_to_add = set()
        beams_to_remove = set()
        for beam in beams:
            if line[beam] == "^":
                beams_to_remove.add(beam)
                beams_to_add.add(beam - 1)
                beams_to_add.add(beam + 1)
                split_count += 1
        for beam in beams_to_remove:
            beams.remove(beam)
        beams |= beams_to_add
        print(f"For line: {line}")
        print(beams)
        print(f"split count: {split_count}")
    print(len(beams))


@puzzle
def part2(puzzle_input):
    beams = [1 if val == "S" else 0 for val in puzzle_input[0]]
    for line in puzzle_input[1:]:
        print([c for c in line])
        for i, timeline_count in enumerate(beams):
            if timeline_count > 0 and line[i] == "^":
                beams[i] = 0
                beams[i - 1] += timeline_count
                beams[i + 1] += timeline_count
        print([str(beam) for beam in beams])

    print(sum(beams))


if __name__ == "__main__":
    part2()
