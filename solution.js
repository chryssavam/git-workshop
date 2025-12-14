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
    // Key constraint: Each warehouse stores deliveries from ONE log only
    // Strategy: Use a min-heap approach, adding each log to smallest warehouse
    // If we have fewer logs than warehouses, split the largest logs

    const warehouses = [];

    for (const log of deliveryLogs) {
        if (warehouses.length < k) {
            // We have available warehouse slots
            warehouses.push(log);
        } else {
            // All k warehouses occupied, add to smallest
            warehouses.sort((a, b) => a - b);
            warehouses[0] += log;
        }
    }

    // If we have fewer logs than k warehouses, split largest logs to balance
    while (warehouses.length < k) {
        warehouses.sort((a, b) => b - a); // Sort descending
        const largest = warehouses[0];

        if (largest > 0) {
            // Split the largest warehouse
            warehouses[0] = Math.floor(largest / 2);
            warehouses.push(Math.ceil(largest / 2));
        } else {
            // All zeros, just add a zero
            warehouses.push(0);
        }
    }

    // Sort and sum the k/2 smallest (safe) warehouses
    warehouses.sort((a, b) => a - b);

    let secureDeliveries = 0;
    for (let i = 0; i < k / 2; i++) {
        secureDeliveries += warehouses[i];
    }

    return secureDeliveries;
}

// Test cases
console.log("Test Case 1:");
console.log("Input: deliveryLogs = [3, 6, 9, 6], k = 4");
console.log("Output:", secureMaximumDeliveries([3, 6, 9, 6], 4));
console.log("Expected: 9\n");

console.log("Test Case 2:");
console.log("Input: deliveryLogs = [6], k = 2");
console.log("Output:", secureMaximumDeliveries([6], 2));
console.log("Expected: 3\n");

console.log("Test Case 3:");
console.log("Input: deliveryLogs = [10, 10, 10, 10], k = 4");
console.log("Output:", secureMaximumDeliveries([10, 10, 10, 10], 4));
console.log("Expected: 20\n");

module.exports = { secureMaximumDeliveries };
