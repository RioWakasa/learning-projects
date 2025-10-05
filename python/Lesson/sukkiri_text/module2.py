file = open('sample.txt', 'r')
for line in file:
  copy = line.rstrip()
  print(copy)
  with open('copy.txt', 'a') as file:
    file.write(copy + '\n')
file.close()