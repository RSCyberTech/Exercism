// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Calculates the total bird count.
 *
 * @param {number[]} birdsPerDay
 * @returns {number} total bird count
 */
export function totalBirdCount(birdsPerDay) {
    let total = 0
    for (let c = 0; c < birdsPerDay.length; c++) {
        total += birdsPerDay[c]
    }
    return total
}

/**
 * Calculates the total number of birds seen in a specific week.
 *
 * @param {number[]} birdsPerDay
 * @param {number} week
 * @returns {number} birds counted in the given week
 */
export function birdsInWeek(birdsPerDay, week) {
    return totalBirdCount(birdsPerDay.slice((week - 1) * 7, ((week - 1) * 7) + 7))
}

/**
 * Fixes the counting mistake by increasing the bird count
 * by one for every second day.
 *
 * @param {number[]} birdsPerDay
 * @returns {number[]} corrected bird count data
 */
export function fixBirdCountLog(birdsPerDay) {
    for (let c = 0; c < birdsPerDay.length; c++) {
        if (c % 2 === 0) {
            birdsPerDay[c]++
        }
    }
    return birdsPerDay
}