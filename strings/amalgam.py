def isAnagram(s, t):

    if len(s) != len(t):
        return False

    hashmap = {}

    # Count letters in s
    for ch in s:
        hashmap[ch] = hashmap.get(ch, 0) + 1

    # Remove letters using t
    for ch in t:
        if ch not in hashmap:
            return False

        hashmap[ch] -= 1

        if hashmap[ch] < 0:
            return False

    return True
