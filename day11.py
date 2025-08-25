def string_permutations(s: str):
    res = []
    chars = sorted(list(s))   # sort to handle duplicates
    used = [False] * len(chars)

    def backtrack(path):
        if len(path) == len(chars):
            res.append("".join(path))
            return
        for i in range(len(chars)):
            # Skip already used characters
            if used[i]:
                continue
            # Skip duplicates (only if previous identical char was not used)
            if i > 0 and chars[i] == chars[i-1] and not used[i-1]:
                continue
            
            used[i] = True
            path.append(chars[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return res


# ✅ Example
print(string_permutations("abc"))  
print(string_permutations("aab"))
