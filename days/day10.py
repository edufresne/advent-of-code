import itertools
import re
from collections import defaultdict
from copy import copy, deepcopy

from utils import puzzle


@puzzle
def part1(machines: list[str]):
    """
    A couple notes.
    - Probably have to put everything into a lookup map. Look up the current state, figure out which ones need to be
    toggled on. This will essentially turn into a directed acyclic graph. Acyclic because doing two presses of the same
    button yields nothing so it's wasted presses.
    """
    result = 0
    for machine in machines:
        i = machine.find("]")
        j = machine.find("{")
        lights = {i: c == "#" for i, c in enumerate(machine[1:i])}
        buttons = [
            tuple(
                int(val)
                for val in item.strip().replace("(", "").replace(")", "").split(",")
            )
            for item in machine[i + 1 : j].split()
            if item.strip()
        ]
        for length in range(1, len(buttons) + 1):
            found = False
            combos = list(itertools.combinations(buttons, length))
            for combo in combos:
                current = {i: False for i in range(len(lights))}
                for button in combo:
                    for light in button:
                        current[light] = not current[light]
                if current == lights:
                    print(length)
                    result += length
                    found = True
                    break
            if found:
                break
    print(result)


@puzzle
def part2(machines: list[str]):
    """
    A couple notes.
    - Probably have to put everything into a lookup map. Look up the current state, figure out which ones need to be
    toggled on. This will essentially turn into a directed acyclic graph. Acyclic because doing two presses of the same
    button yields nothing so it's wasted presses.
    """
    result = 0
    for machine in machines:
        i = machine.find("]")
        j = machine.find("{")
        buttons = [
            tuple(
                int(val)
                for val in item.strip().replace("(", "").replace(")", "").split(",")
            )
            for item in machine[i + 1 : j].split()
            if item.strip()
        ]
        button_map = defaultdict(set)
        for button in buttons:
            for joltage in button:
                button_map[joltage].add(button)
        joltage_map = {i: int(val) for i, val in enumerate(machine[j:].replace('{', '').replace('}', '').strip().split(','))}
        print(f'For map: {joltage_map}')
        current_remaining = deepcopy(joltage_map)
        local_total = 0
        buttons_pressed = []
        while any(value > 0 for value in current_remaining.values()):
            max_button = list(buttons)[0]
            max_sum = sum(current_remaining[light] for light in max_button if current_remaining[light] > 0)
            for button in buttons:
                current_sum = sum(current_remaining[light] for light in button if current_remaining[light] > 0)
                if current_sum > max_sum:
                    max_sum = current_sum
                    max_button = button
            print(f'Pressing button: {max_button}')
            local_total += 1
            for joltage in max_button:
                current_remaining[joltage] -= 1
            buttons_pressed.append(max_button)
        assert len(buttons_pressed) == local_total
        _check_function(joltage_map, buttons_pressed)
        print(local_total)
        result += local_total
    print(result)


def _check_function(joltage_map: dict, buttons: list[tuple]) -> None:
    m = deepcopy(joltage_map)
    for button in buttons:
        for value in button:
            m[value] -= 1
    assert all(value <= 0 for value in m.values())



if __name__ == "__main__":
    part2()
