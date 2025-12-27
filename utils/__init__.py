import os.path
import re
from pathlib import Path
from typing import Callable

_REGEX = re.compile(r"/(\d+)/day(\d+).py$")


def puzzle(f: Callable) -> Callable:
    def _callable() -> None:
        file_name = f.__code__.co_filename
        cache_dir = Path(__file__).parents[1].joinpath(".puzzle_cache")
        if not cache_dir.exists():
            os.makedirs(cache_dir)

        match = _REGEX.search(file_name)
        if not match:
            raise ValueError(f"Cannot determine puzzle day for file: {file_name}")
        year = match.group(1)
        if not cache_dir.joinpath(year).exists():
            cache_dir.joinpath(year).mkdir()
        day = match.group(2)
        cache_filename = cache_dir.joinpath(year, f"{day}.txt")
        if not cache_filename.exists():
            raise ValueError(f"Missing puzzle input for day: {day}")
        else:
            puzzle_input = cache_filename.read_text()
        f(puzzle_input.splitlines())

    return _callable


def adj_coords(
    grid: list[str] | list[list], row: int, col: int
) -> list[tuple[int, int]]:
    n_rows = len(grid)
    n_cols = len(grid[0])
    return [
        pos
        for pos in [
            (row - 1, col - 1),
            (row - 1, col),
            (row, col - 1),
            (row - 1, col + 1),
            (row + 1, col - 1),
            (row + 1, col),
            (row, col + 1),
            (row + 1, col + 1),
        ]
        if 0 <= pos[0] < n_rows and 0 <= pos[1] < n_cols
    ]
