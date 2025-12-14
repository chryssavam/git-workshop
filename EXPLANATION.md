# AWS Security Groups - Solution Explanation

## Problem Summary

Given `n` servers with security grades `security[i]`, group them to minimize the number of groups where:
- Servers in the same group must have the same security grade
- All group sizes must differ by at most 1 (i.e., all groups are size `m` or `m+1` for some minimum size `m`)

## Algorithm Explanation

### Step 1: Count Frequencies
Count how many servers have each security grade.

Example: `[2, 3, 3, 3, 2, 1]`
- Grade 1: 1 server
- Grade 2: 2 servers
- Grade 3: 3 servers

### Step 2: Try All Possible Minimum Group Sizes (m)
For each possible value of `m` (from largest to smallest), check if ALL frequencies can be validly partitioned into groups of size `m` or `m+1`.

**Key constraint:** For frequency `f` with `k` groups of size `m` or `m+1`, we need:
- `k * m <= f <= k * (m+1)`

This ensures we can actually distribute `f` servers across `k` groups where each group is size `m` or `m+1`.

### Step 3: Validate and Calculate
For a given `m`:
1. For each frequency `f`, calculate minimum groups needed: `k = ceil(f / (m+1))`
2. **Verify validity:** Check if `k * m <= f` (the left side of our constraint)
3. If ANY frequency fails validation, try smaller `m`
4. If ALL frequencies pass, this `m` is valid - calculate total groups

### Step 4: Return First Valid Solution
The largest valid `m` gives us the minimum total number of groups.

**Why try from largest to smallest?** Larger `m` generally means fewer total groups, so we want the largest valid `m`.

## Example Walkthrough

### Example 1: `[2, 3, 3, 3, 2, 1]`

**Frequencies:** [1, 2, 3]

**Try m=3:**
- f=1: k=ceil(1/4)=1, check: 1*3=3 ≤ 1? NO! ✗ Invalid

**Try m=2:**
- f=1: k=ceil(1/3)=1, check: 1*2=2 ≤ 1? NO! ✗ Invalid

**Try m=1:**
- f=1: k=ceil(1/2)=1, check: 1*1=1 ≤ 1? YES ✓
- f=2: k=ceil(2/2)=1, check: 1*1=1 ≤ 2? YES ✓
- f=3: k=ceil(3/2)=2, check: 2*1=2 ≤ 3? YES ✓
- Total: 1+1+2 = **4 groups** ✓

**Actual partition:** Groups of size 1 or 2: [1, 2, 2, 1]

### Example 2: `[1, 7, 7, 7, 1]`

**Frequencies:** [2, 3]

**Try m=3:**
- f=2: k=ceil(2/4)=1, check: 1*3=3 ≤ 2? NO! ✗ Invalid

**Try m=2:**
- f=2: k=ceil(2/3)=1, check: 1*2=2 ≤ 2? YES ✓
- f=3: k=ceil(3/3)=1, check: 1*2=2 ≤ 3? YES ✓
- Total: 1+1 = **2 groups** ✓

**Actual partition:** Groups of size 2 or 3: [2, 3]

### Example 3 (Bug Case): `[1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2]`

**Frequencies:** [5, 7]

**Try m=7:**
- f=5: k=ceil(5/8)=1, check: 1*7=7 ≤ 5? NO! ✗ Invalid

**Try m=5, m=4, m=3:** All invalid (similar to above)

**Try m=2:**
- f=5: k=ceil(5/3)=2, check: 2*2=4 ≤ 5? YES ✓
- f=7: k=ceil(7/3)=3, check: 3*2=6 ≤ 7? YES ✓
- Total: 2+3 = **5 groups** ✓

**Actual partition:** Groups of size 2 or 3: [2, 3, 2, 3, 3] or similar

## Complexity Analysis

- **Time Complexity:** O(n * max_freq) where n = length of security array
  - O(n) to count frequencies
  - O(max_freq) to try different values of m
  - For each m, O(k) to validate all frequencies where k = unique security grades
  - Overall: O(n + max_freq * k), which is O(n * max_freq) in worst case
  - In practice, this is still very efficient as max_freq ≤ n

- **Space Complexity:** O(k) where k = unique security grades
  - HashMap to store frequencies

## Key Insight

The problem is essentially asking: "What's the optimal way to partition frequencies into groups such that all groups are size `m` or `m+1`?"

The answer: Make `m` as large as possible (= minimum frequency), then greedily use size `(m+1)` groups.

## Input/Output Format

For online judge submissions:

**Input:**
```
Line 1: n (number of servers)
Lines 2 to n+1: security grade of each server (one per line)
```

**Output:**
```
Single integer: minimum number of groups
```

**Example:**
```
Input:
5
1
7
7
7
1

Output:
2
```

## Implementation Notes

The solution provides two versions:
1. **main_with_stdin()** - For online judge platforms that read from STDIN
2. **main_test()** - For local testing with predefined test cases

Switch between them by uncommenting the appropriate function call in the `if __name__ == "__main__"` block.
