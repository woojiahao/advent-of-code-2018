import itertools


def find_frequency():
  with open('data.txt', 'r') as file:
    data = [int(line.replace('\n', '')) for line in file.readlines()]

  total = 0
  previous = set()

  for value in itertools.cycle(data):
    total += value
    if total in previous:
      print(f'Found: {total}')
      break
    previous.add(total)


find_frequency()
