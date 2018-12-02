from itertools import groupby, combinations

def has_one_difference(word_one: str, word_two: str) -> bool:
  if len(word_one) != len(word_two): return False

  return len([pair for pair in zip(list(word_one), list(word_two)) if pair[0] != pair[1]]) == 1


def count_repeats():
  with open('data.txt', 'r') as file:
    filtered_data = [
      group
      for group in [
        list(grp)
        for _, grp in groupby(sorted([
          line.replace('\n', '')
          for line in file
        ]), lambda x: x[0])
      ]
      if len(group) > 1
    ]
    for combination in [list(combinations(i, 2)) for i in filtered_data]:
      for pair in combination:
        if has_one_difference(pair[0], pair[1]):
          print(pair)
          return

count_repeats()