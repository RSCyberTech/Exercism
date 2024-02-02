// @ts-check

/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
export function twoSum(array1, array2) {
    let total1 = ''
    for (let a of array1) {
        total1 += a
    }
    let total2 = ''
    for (let a of array2) {
        total2 += a
    }
    return parseInt(total1) + parseInt(total2)
}

/**
 * Checks whether a number is a palindrome.
 *
 * @param {number} value
 * @returns {boolean} whether the number is a palindrome or not
 */
export function luckyNumber(value) {
    value = value.toString()
    let reverse = value.split('').reverse().join('')
    return value === reverse
}

/**
 * Determines the error message that should be shown to the user
 * for the given input value.
 *
 * @param {string|null|undefined} input
 * @returns {string} error message
 */
export function errorMessage(input) {
    if (!input && input !== 0) {
        return "Required field"
    }
    else if (input > 0 || input < 0) {
        return ''
    }
    else {
        return 'Must be a number besides 0'
    }
}