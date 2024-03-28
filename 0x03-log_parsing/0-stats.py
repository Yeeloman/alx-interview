#!/usr/bin/python3
"""0-state.py"""

import sys
from typing import List
import re

REGEX_PATTERN = re.compile(r"(^(?:[0-9]{1,3}\.){3}[0-9]{1,3}) - \[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d+\]\s\"GET \/projects\/260 HTTP\/1.1\"\s(\d{3})\s(\d+)$")  # noqa

total_file_size: int = 0
lines_printed: int = 0
possible_states: List[List[int]] = [
    [200, 0], [301, 0],
    [400, 0], [401, 0],
    [403, 0], [404, 0],
    [405, 0], [500, 0]
]


def print_status(status_arr: List[List[int]]) -> None:
    """print_status"""
    for status in status_arr:
        print(f"{status[0]}: {status[1]}")


def print_infos(total_file_size: int, possible_states: List[List[int]]) -> None:  # noqa
    """print_infos"""
    print("File size: {}".format(total_file_size))
    print_status(possible_states)


def update_possible_states(poss_stats: List[List[int]], matched_stat: int) -> None:  # noqa
    """update_possible_states"""
    for stat in poss_stats:
        if stat[0] == matched_stat:
            stat[1] += 1
            break


try:
    for line in sys.stdin:
        matched = re.search(REGEX_PATTERN, line)
        if not matched:
            continue
        total_file_size += int(matched.group(3))
        update_possible_states(possible_states, int(matched.group(2)))
        if lines_printed < 10:
            print_infos(total_file_size, possible_states)
            lines_printed = 0
except Exception as e:
    pass
