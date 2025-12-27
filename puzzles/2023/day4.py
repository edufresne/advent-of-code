from utils import puzzle


def solve_card(winners: set[int], numbers: set[int]):
    count = len({number for number in numbers if number in winners})
    if count == 0:
        return 0
    elif count == 1:
        return 1
    return 2 ** (count - 1)

@puzzle
def part1(puzzle_input):
    result = 0
    for card in puzzle_input:
        values = card[card.index(':') + 1:].strip().split('|')
        winners = {int(val) for val in values[0].strip().split()}
        numbers = {int(val) for val in values[1].strip().split()}
        print(card)
        points = solve_card(winners, numbers)
        print(points)
        result += points
    print(result)


@puzzle
def part2(puzzle_input):
    card_map = {i: 1 for i in range(len(puzzle_input))}
    result = len(puzzle_input)
    win_count_map = {}
    for i, card in enumerate(puzzle_input):
        values = card[card.index(':') + 1:].strip().split('|')
        winners = {int(val) for val in values[0].strip().split()}
        numbers = {int(val) for val in values[1].strip().split()}
        win_count_map[i] = len(winners & numbers)
    while cards_to_process := {k: v for k, v in card_map.items() if v > 0}:
        for id_, value in cards_to_process.items():
            card_map[id_] -= 1
            for i in range(id_ + 1, id_ + 1 + win_count_map[id_]):
                card_map[i] += 1
                result += 1

    print(result)





if __name__ == '__main__':
    part2()