import re

splitters = r"[, ]+"

long = input()
short= re.split(splitters, long)
print(short)