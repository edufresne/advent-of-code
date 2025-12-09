"""
Pre-computing and sorting distance is much faster than checking each time which is why part 1 is so slow. Part 1 is
actually harder than part 1 as you need to find the groups of circuits. Part 2 you just need to find when everything is
connected, so you can just use a set to track which items are connected and once all are, you can break and return the
result.
"""
import itertools
import math
from collections import defaultdict

from utils import puzzle



@puzzle
def part1(puzzle_input):
    # This runs super slow. part2 will do better.
    nodes = [tuple(int(val) for val in line.split(',')) for line in puzzle_input]
    circuits = [{i} for i in range(len(nodes))]
    connection_map = defaultdict(set)
    print(circuits)
    for _ in range(1000):
        min_distance = None
        a, b = None, None
        for i, node1 in enumerate(nodes):
            for j, node2 in enumerate(nodes):
                if i == j or i in connection_map[j] or j in connection_map[i]:
                    continue
                distance = _distance(node1, node2)
                if min_distance is None or distance < min_distance:
                    min_distance = distance
                    a = i
                    b = j
        print(f'Closest together are: {nodes[a]} and {nodes[b]} with distance: {min_distance}')
        connection_map[a].add(b)
        connection_map[b].add(a)

        new_circuit = set(itertools.chain.from_iterable([circuit for circuit in circuits if a in circuit or b in circuit]))
        circuits = [circuit for circuit in circuits if a not in circuit and b not in circuit] + [new_circuit]

    print(circuits)
    counts = [len(circuit) for circuit in sorted(circuits, key=lambda circuit: len(circuit))[-3:]]
    print(counts[0] * counts[1] * counts[2])


@puzzle
def part2(puzzle_input):
    # This runs super slow. part2 will do better.
    nodes = [tuple(int(val) for val in line.split(',')) for line in puzzle_input]
    node_combos = [(i, k) for i in range(len(nodes)) for k in range(len(nodes)) if i != k]
    sorted_combos = sorted(node_combos, key=lambda combo: _distance(nodes[combo[0]], nodes[combo[1]]))
    connected = set()
    for a, b in sorted_combos:
        print(f'{nodes[a]} -> {nodes[b]}')
        print(f'Distance: {_distance(nodes[a], nodes[b])}')
        connected |= {a, b}
        if len(connected) == len(nodes):
            print(nodes[a][0] * nodes[b][0])
            break



def _distance(node1: tuple, node2: tuple) -> float:
    return math.sqrt((node2[0] - node1[0]) ** 2 + (node2[1] - node1[1]) ** 2 + (node2[2] - node1[2]) ** 2)



if __name__ == '__main__':
    part2()