# calculate mean, standard deviation, standard error from inputdata.txt
from statistics import mean, stdev
from scipy.stats import sem
import re

with open('inputdata.txt','r') as fin:
    read_str = re.split(r'[\n]', fin.read())
    pattern = re.compile("([0-9]*[.]+?[0-9]+)")
    data = []
    for x in read_str:
      match = re.search(pattern, x)
      if match:
         data.append(float(match.group()))
    print(data)

average = mean(data)
print(average)

standard_deviation = stdev(data)
print(standard_deviation)

standard_error = sem(data)
print(standard_error)
