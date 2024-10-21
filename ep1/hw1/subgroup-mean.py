# split 100 data into 10 groups and calculate mean and standard deviation of each subgroup
from statistics import mean, stdev
from scipy.stats import sem
import re

with open('inputdata.txt','r') as fin:
    read_str = re.split(r'[\n]', fin.read())
    pattern = re.compile("([0-9]*[.]+?[0-9]+)")
    data = []
    subarr_idx = 0
    data.append([])
    for x in read_str:
      match = re.search(pattern, x)
      if match:
            data[subarr_idx].append(float(match.group()))
            if len(data[subarr_idx]) == 10:
                average = mean(data[subarr_idx])
                print(f"arithmetic mean for group {subarr_idx}", average)
                standard_deviation = stdev(data[subarr_idx])
                print(f"standard deviation for group {subarr_idx}", standard_deviation)
                subarr_idx += 1
                if subarr_idx < 10:
                  data.append([])
    print(data)
