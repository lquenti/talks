with open("nummern.txt", "r") as fp:
  line = fp.readline()
xs = [int(x) for x in line.split(',')]
print(sum(xs)/len(xs))
