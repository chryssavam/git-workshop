def teamSize(talent, talentsCount):
    n = len(talent)
    result = []
    freq = {}
    have = 0  # distinct talents 1..talentsCount in current window
    end = 0

    for start in range(n):
        # Expand right until the window contains all talents
        while end < n and have < talentsCount:
            t = talent[end]
            if 1 <= t <= talentsCount:
                freq[t] = freq.get(t, 0) + 1
                if freq[t] == 1:
                    have += 1
            end += 1

        if have == talentsCount:
            result.append(end - start)
        else:
            result.append(-1)

        # Shrink window from the left
        t = talent[start]
        if 1 <= t <= talentsCount:
            freq[t] -= 1
            if freq[t] == 0:
                have -= 1

    return result
