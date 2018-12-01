def calculate():
  with open('data.txt', 'r') as file:
    data = [int(line.replace('\n', '')) for line in file.readlines()]
  
  print(sum(data))

calculate()