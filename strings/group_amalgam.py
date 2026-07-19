from collections import defaultdict
def groupAnalgams(strs):
  groups = defaultdict(list)
  for word in strs:
    key = "".join(sorted(word))
    groups[key].append(word)
  return list(groups.values())
