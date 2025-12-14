#!/usr/bin/env python3
"""
Solution for AWS Security Groups Problem

Problem: Given servers with security grades, group them such that:
- Servers in same group have same security grade
- All groups have sizes differing by at most 1
- Minimize total number of groups

Time Complexity: O(n) where n is length of security array
Space Complexity: O(k) where k is number of unique security grades
"""

from collections import Counter
import math
import sys


def findMinimumGroups(security):
    """
    Find minimum number of security groups needed.

    All groups must have sizes differing by at most 1, meaning all groups
    are size m or m+1 for some minimum group size m.

    Strategy: Try all possible values of m and find the largest m where
    all frequencies can be validly partitioned.

    Args:
        security: List of integers representing security grades

    Returns:
        Minimum number of groups required
    """
    if not security:
        return 0

    # Count frequency of each security grade
    freq_map = Counter(security)
    frequencies = list(freq_map.values())

    if not frequencies:
        return 0

    # Try all possible minimum group sizes from largest to smallest
    # Larger m generally means fewer total groups
    max_freq = max(frequencies)

    for m in range(max_freq, 0, -1):
        valid = True
        total_groups = 0

        for f in frequencies:
            # Minimum number of groups needed to partition f into groups of size m or m+1
            k = math.ceil(f / (m + 1))

            # Verify this partition is actually valid
            # We need: k * m <= f <= k * (m + 1)
            if k * m > f:
                # Can't partition this frequency with this m
                valid = False
                break

            total_groups += k

        if valid:
            # Found the largest valid m - return total groups
            return total_groups

    # Fallback (should not reach here)
    return len(security)


def main_with_stdin():
    """Version for online judge with STDIN input"""
    lines = sys.stdin.read().strip().split('\n')

    if not lines or not lines[0]:
        print(0)
        return

    n = int(lines[0])

    if n == 0:
        print(0)
        return

    security = []
    for i in range(1, n + 1):
        if i < len(lines):
            security.append(int(lines[i]))

    result = findMinimumGroups(security)
    print(result)


def main_test():
    """Version for local testing"""
    # Test case 1 from problem description
    security1 = [2, 3, 3, 3, 2, 1]
    result1 = findMinimumGroups(security1)
    print(f"Test 1: security = {security1}")
    print(f"Result: {result1}")
    print(f"Expected: 4\n")

    # Test case 2 from problem description
    security2 = [1, 7, 7, 7, 1]
    result2 = findMinimumGroups(security2)
    print(f"Test 2: security = {security2}")
    print(f"Result: {result2}")
    print(f"Expected: 2\n")

    # Additional test cases
    security3 = [1, 1, 1, 1, 1]
    result3 = findMinimumGroups(security3)
    print(f"Test 3: security = {security3}")
    print(f"Result: {result3}")
    print(f"Expected: 1 (all same grade)\n")

    security4 = [1, 2, 3, 4, 5]
    result4 = findMinimumGroups(security4)
    print(f"Test 4: security = {security4}")
    print(f"Result: {result4}")
    print(f"Expected: 5 (all different grades)\n")

    # Edge cases
    security5 = [1]
    result5 = findMinimumGroups(security5)
    print(f"Test 5: security = {security5}")
    print(f"Result: {result5}")
    print(f"Expected: 1\n")

    security6 = [1, 1, 2]
    result6 = findMinimumGroups(security6)
    print(f"Test 6: security = {security6}")
    print(f"Result: {result6}\n")


if __name__ == "__main__":
    # Uncomment the version you need:

    # For online judge (reads from STDIN):
    # main_with_stdin()

    # For local testing:
    main_test()
