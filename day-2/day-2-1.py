from itertools import groupby


def has_repeat(word: str, count: int) -> bool:
  return any(i == count for i in [len(''.join(grp)) for _, grp in groupby(list(sorted(word.lower())))])


def count_repeats() -> tuple:
  _twos, _threes = 0, 0

  with open('data.txt', 'r') as file:
    for line in file:
      if has_repeat(line, 2): _twos += 1
      if has_repeat(line, 3): _threes += 1

  return _twos, _threes


twos, threes = count_repeats()
print(f'Checksum: {twos * threes}')
