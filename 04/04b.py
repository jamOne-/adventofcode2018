import sys
import re
from collections import defaultdict

line_re = re.compile('^\[.*:(\d+)] (.*)$')
guard_number_re = re.compile('^.*#(\d+) ')


def get_best_minute(sleep):
    return max(sleep.items(), key=lambda kv: kv[1])


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

    best_minutes = [(guard, *get_best_minute(sleep))
                    for guard, sleep in guards.items()]
    guard, best_minute, value = max(best_minutes, key=lambda gmv: gmv[2])
    return guard * best_minute


print(solve(sys.stdin))
