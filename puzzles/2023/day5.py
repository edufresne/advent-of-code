from collections import deque

from utils import puzzle


@puzzle
def part1(puzzle_input):
    seeds = [int(seed) for seed in puzzle_input[0].split(":")[1].strip().split()]
    seed_to_soil_map = {}
    soil_to_fert_map = {}
    fert_to_water_map = {}
    water_to_light_map = {}
    light_to_temp_map = {}
    temp_to_humidity_map = {}
    humidity_to_location_map = {}

    dicts_to_parse = deque(
        [
            seed_to_soil_map,
            soil_to_fert_map,
            fert_to_water_map,
            water_to_light_map,
            light_to_temp_map,
            temp_to_humidity_map,
            humidity_to_location_map,
        ]
    )
    for line in puzzle_input[2:]:
        if not line:
            dicts_to_parse.popleft()
        elif "-" not in line:
            d = dicts_to_parse[0]
            dest_start, source_start, range_length = [int(val) for val in line.split()]
            d[(source_start, source_start + range_length - 1)] = (
                dest_start,
                dest_start + range_length - 1,
            )

    locations = []
    for seed in seeds:
        for location in locations:
            

    print(min(locations))



def _overlaps(t1: tuple[int, int], t2: tuple[int, int]) -> bool:
    return (
        t2[0] <= t1[0] <= t2[1]
        or t2[0] <= t1[1] <= t2[1]
        or t1[0] <= t2[0] <= t1[1]
        or t1[0] <= t2[1] <= t1[1]
    )


if __name__ == "__main__":
    part1()
