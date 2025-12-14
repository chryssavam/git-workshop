# AWS Security Groups - Solution Explanation

## Problem Summary

Given `n` servers with security grades `security[i]`, group them to minimize the number of groups where:
- Servers in the same group must have the same security grade
- All group sizes must differ by at most 1

## Algorithm Explanation

### Step 1: Count Frequencies
Count how many servers have each security grade.

Example: `[2, 3, 3, 3, 2, 1]`
- Grade 1: 1 server
- Grade 2: 2 servers
- Grade 3: 3 servers

### Step 2: Find Minimum Frequency
The minimum frequency across all security grades determines the maximum possible minimum group size.

If `min_freq = 1`, all groups must be size 1 or 2.
If `min_freq = 2`, all groups must be size 2 or 3.

**Why?** If we have a security grade with only 1 server, we can't make a group larger than 1 from it. So the smallest group will be size 1, meaning all groups must be size 1 or 2.

### Step 3: Calculate Groups Needed
For each security grade with frequency `f`, we partition it into groups of size `m` or `m+1` (where `m = min_freq`).

To minimize groups, use as many size `(m+1)` groups as possible:
- Groups needed = `ceil(f / (m+1))`

### Step 4: Sum Total Groups
Add up groups needed for all security grades.

## Example Walkthrough

### Example 1: `[2, 3, 3, 3, 2, 1]`

**Frequencies:** {1→1, 2→2, 3→3}
**Min frequency:** 1
**Group sizes:** 1 or 2

**Partitioning:**
- Grade 1 (1 server): ceil(1/2) = 1 group of size 1
- Grade 2 (2 servers): ceil(2/2) = 1 group of size 2
- Grade 3 (3 servers): ceil(3/2) = 2 groups (one size 2, one size 1)

**Total:** 4 groups with sizes [1, 2, 2, 1] ✓

### Example 2: `[1, 7, 7, 7, 1]`

**Frequencies:** {1→2, 7→3}
**Min frequency:** 2
**Group sizes:** 2 or 3

**Partitioning:**
- Grade 1 (2 servers): ceil(2/3) = 1 group of size 2
- Grade 7 (3 servers): ceil(3/3) = 1 group of size 3

**Total:** 2 groups with sizes [2, 3] ✓

## Complexity Analysis

- **Time Complexity:** O(n) where n = length of security array
  - O(n) to count frequencies
  - O(k) to calculate groups where k = unique security grades

- **Space Complexity:** O(k) where k = unique security grades
  - HashMap to store frequencies

## Key Insight

The problem is essentially asking: "What's the optimal way to partition frequencies into groups such that all groups are size `m` or `m+1`?"

The answer: Make `m` as large as possible (= minimum frequency), then greedily use size `(m+1)` groups.
