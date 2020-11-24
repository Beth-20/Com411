import csv
import matplotlib.pyplot as plt

header = None

def read_data():
  global header
  with open ('Visual/subplots/temps.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    temps = {header[0]:[], header[1]:[]}
    
    for line in csv_reader:
      temps[header[0]].append(float(line[0].strip()))
      temps[header[1]].append(float(line[1].strip()))

  return temps

def run():
  data = read_data()
  fig, (ax1, ax2) = plt.subplots(2, 1)
  ax1.plot(range(1,8), data[header[0]])
  ax2.plot(range(1,8), data[header[1]])
  plt.tight_layout()
  plt.show()

run()
