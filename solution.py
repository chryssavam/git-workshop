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
    # Key constraint: Each warehouse stores deliveries from ONE log only
    # Strategy: Use a min-heap approach, adding each log to smallest warehouse
    # If we have fewer logs than warehouses, split the largest logs

    warehouses = []

    for log in deliveryLogs:
        if len(warehouses) < k:
            # We have available warehouse slots
            warehouses.append(log)
        else:
            # All k warehouses occupied, add to smallest
            warehouses.sort()
            warehouses[0] += log

    # If we have fewer logs than k warehouses, split largest logs to balance
    while len(warehouses) < k:
        warehouses.sort(reverse=True)  # Sort descending
        largest = warehouses[0]

        if largest > 0:
            # Split the largest warehouse
            warehouses[0] = largest // 2
            warehouses.append(largest - largest // 2)
        else:
            # All zeros, just add a zero
            warehouses.append(0)

    # Sort and sum the k/2 smallest (safe) warehouses
    warehouses.sort()

    secure_deliveries = sum(warehouses[:k // 2])

    return secure_deliveries


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
