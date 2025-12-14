"""
Secure Maximum Deliveries - LeetCode Style Problem

Given:
- deliveryLogs: array where deliveryLogs[i] = number of parts in log i
- k: number of secure warehouses (even integer)

Constraints:
- Each warehouse can only store deliveries from a single log
- A log can be split across multiple warehouses
- After storing, k/2 warehouses with most deliveries are compromised
- k/2 warehouses with least deliveries are safe

Return: Maximum number of secure deliveries possible
"""

def secureMaximumDeliveries(deliveryLogs, k):
    """
    Main solution function using greedy algorithm.

    Args:
        deliveryLogs: List[int] - number of deliveries in each log
        k: int - number of secure warehouses (even)

    Returns:
        int - maximum number of secure deliveries
    """
    # Key constraint: Each warehouse stores from ONE log only
    # A log CAN be split across multiple warehouses
    # Greedy approach: Repeatedly split the largest warehouse value
    # until we have k warehouses, which balances the load

    logs = sorted(deliveryLogs, reverse=True)

    # Start with each log in one warehouse (up to min(n, k) logs)
    warehouses = logs[:min(len(logs), k)]

    # If we have fewer warehouses than k, keep splitting the largest
    while len(warehouses) < k:
        # Find the largest warehouse value
        max_idx = warehouses.index(max(warehouses))

        # Split it in half
        val = warehouses[max_idx]
        warehouses[max_idx] = val / 2
        warehouses.append(val / 2)

    # Sort and sum the k/2 smallest warehouses
    warehouses.sort()

    secure_deliveries = sum(warehouses[:k // 2])

    return int(secure_deliveries)


if __name__ == "__main__":
    # Test cases
    print("Test Case 1:")
    print("Input: deliveryLogs = [3, 6, 9, 6], k = 4")
    result1 = secureMaximumDeliveries([3, 6, 9, 6], 4)
    print(f"Output: {result1}")
    print(f"Expected: 9")
    print(f"Status: {'✓ PASS' if result1 == 9 else '✗ FAIL'}\n")

    print("Test Case 2:")
    print("Input: deliveryLogs = [6], k = 2")
    result2 = secureMaximumDeliveries([6], 2)
    print(f"Output: {result2}")
    print(f"Expected: 3")
    print(f"Status: {'✓ PASS' if result2 == 3 else '✗ FAIL'}\n")

    print("Test Case 3:")
    print("Input: deliveryLogs = [10, 10, 10, 10], k = 4")
    result3 = secureMaximumDeliveries([10, 10, 10, 10], 4)
    print(f"Output: {result3}")
    print(f"Expected: 20")
    print(f"Status: {'✓ PASS' if result3 == 20 else '✗ FAIL'}\n")
