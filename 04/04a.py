import sys
import re
from collections import defaultdict

line_re = re.compile('^\[.*:(\d+)] (.*)$')
guard_number_re = re.compile('^.*#(\d+) ')


def get_max_sleeper(guards):
    return -max([(sum(sleep.values()), -guard) for guard, sleep in guards.items()])[1]


def get_best_minute(sleep):
    return max(sleep.items(), key=lambda kv: kv[1])[0]


def solve(lines):
    records = sorted(lines)
    guards = defaultdict(lambda: defaultdict(int))

    last_guard = None
    last_asleep_minute = None

    for record in records:
        minute, action = line_re.match(record).groups()
        minute = int(minute)

        if action.startswith('Guard'):
            last_guard = int(guard_number_re.match(action).group(1))
        elif action == 'falls asleep':
            last_asleep_minute = minute
        elif action == 'wakes up':
            for minute in range(last_asleep_minute, minute):
                guards[last_guard][minute] += 1

    guard = get_max_sleeper(guards)
    minute = get_best_minute(guards[guard])
    return guard * minute


print(solve(sys.stdin))
