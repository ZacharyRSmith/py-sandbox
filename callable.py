from collections import defaultdict


class CountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


counter = CountMissing()
current = {
    'blue': 2, 'green': 4
}
increments = [
    ('red', 3),
    ('blue', 2),
    ('orange', 1)
]
result = defaultdict(counter, current)
for key, incr in increments:
    result[key] += incr
assert counter.added == 3
