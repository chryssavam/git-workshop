/**
 * Secure Maximum Deliveries - LeetCode Style Problem
 *
 * Given:
 * - deliveryLogs: array where deliveryLogs[i] = number of parts in log i
 * - k: number of secure warehouses (even integer)
 *
 * Constraints:
 * - Each warehouse can only store deliveries from a single log
 * - A log can be split across multiple warehouses
 * - After storing, k/2 warehouses with most deliveries are compromised
 * - k/2 warehouses with least deliveries are safe
 *
 * Return: Maximum number of secure deliveries possible
 */

function secureMaximumDeliveries(deliveryLogs, k) {
    // Key constraint: Each warehouse stores from ONE log only
    // A log CAN be split across multiple warehouses
    //
    // Greedy approach: Repeatedly split the largest warehouse value
    // until we have k warehouses, which balances the load

    const logs = [...deliveryLogs].sort((a, b) => b - a);

    // Start with each log in one warehouse (up to min(n, k) logs)
    const warehouses = [];
    for (let i = 0; i < Math.min(logs.length, k); i++) {
        warehouses.push(logs[i]);
    }

    // If we have fewer warehouses than k, keep splitting the largest
    while (warehouses.length < k) {
        // Find the largest warehouse value
        let maxIdx = 0;
        for (let i = 1; i < warehouses.length; i++) {
            if (warehouses[i] > warehouses[maxIdx]) {
                maxIdx = i;
            }
        }

        // Split it in half
        const val = warehouses[maxIdx];
        warehouses[maxIdx] = val / 2;
        warehouses.push(val / 2);
    }

    // Sort and sum the k/2 smallest warehouses
    warehouses.sort((a, b) => a - b);

    let sum = 0;
    for (let i = 0; i < k / 2; i++) {
        sum += warehouses[i];
    }

    return sum;
}

// Test cases
const testCases = [
    { input: [[3, 6, 9, 6], 4], expected: 9, name: "Example 1" },
    { input: [[6], 2], expected: 3, name: "Example 2" },
    { input: [[10, 10, 10, 10], 4], expected: 20, name: "Equal logs" },
    { input: [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 4], expected: null, name: "More logs than warehouses" },
    { input: [[100], 4], expected: null, name: "Single large log, multiple warehouses" },
    { input: [[1, 2, 3, 4, 5], 4], expected: null, name: "More logs than k" },
    { input: [[5, 5, 5, 5], 6], expected: null, name: "More warehouses than logs" },
];

testCases.forEach((tc, idx) => {
    const result = secureMaximumDeliveries(...tc.input);
    console.log(`Test ${idx + 1}: ${tc.name}`);
    console.log(`  Input: deliveryLogs = [${tc.input[0]}], k = ${tc.input[1]}`);
    console.log(`  Output: ${result}`);
    if (tc.expected !== null) {
        console.log(`  Expected: ${tc.expected}`);
        console.log(`  Status: ${result === tc.expected ? '✓ PASS' : '✗ FAIL'}`);
    }
    console.log();
});

module.exports = { secureMaximumDeliveries };
