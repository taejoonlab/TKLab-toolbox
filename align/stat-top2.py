#!/usr/bin/env python3
import sys

filename_top2 = sys.argv[1]

ratio_list = []
f_top2 = open(filename_top2, 'r')
for line in f_top2:
    if line.startswith('#'):
        continue
    tokens = line.strip().split("\t")
    match_ratio = float(tokens[4])
    ratio_list.append(match_ratio)
f_top2.close()

total_count = len(ratio_list)
print("Total count: %d" % len(ratio_list))
perfect_hit_count = len([x for x in ratio_list if x >= 1.0])
print("Hits with match_ratio 1.0: %d (%.2f pct)" % (perfect_hit_count, perfect_hit_count/total_count*100.0))
pct90_hit_count = len([x for x in ratio_list if x >= 0.9])
print("Hits with match_ratio >= 0.9: %d (%.2f pct)" % (pct90_hit_count, pct90_hit_count/total_count*100.0))
