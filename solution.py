#!/usr/bin/env python3
"""
Solution for AWS Security Groups Problem

Problem: Given servers with security grades, group them such that:
- Servers in same group have same security grade
- All groups have sizes differing by at most 1
- Minimize total number of groups
"""

from collections import Counter
import math


def findMinimumGroups(security):
    """
    Find minimum number of security groups needed.

    Args:
        security: List of integers representing security grades

    Returns:
        Minimum number of groups required

    Time Complexity: O(n) where n is length of security array
    Space Complexity: O(k) where k is number of unique security grades
    """
    # Count frequency of each security grade
    freq_map = Counter(security)
    frequencies = list(freq_map.values())

    # Edge case: empty array
    if not frequencies:
        return 0

    # The minimum frequency determines the maximum possible minimum group size
    # All groups must be size m or m+1, so m <= min(frequencies)
    min_freq = min(frequencies)

    # For each frequency f, partition into groups of size min_freq or min_freq+1
    # Minimum groups needed for frequency f is ceil(f / (min_freq + 1))
    total_groups = sum(math.ceil(f / (min_freq + 1)) for f in frequencies)

    return total_groups


def main():
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


if __name__ == "__main__":
    main()
