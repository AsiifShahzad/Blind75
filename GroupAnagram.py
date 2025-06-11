def groupAnagram(strs: List[str]) -> List[List[str]]:
    groupanagrams = dict()
    for word in strs:
        key = tuple(sorted(word))
        if key not in groupanagrams:
            groupanagrams[key] = []
        groupanagrams[key].append(word)
    return list(groupanagrams.values())
