// @ts-check

/**
 * Double every card in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with every card doubled
 */
export function seeingDouble(deck) {
    let newDeck = []
    for (let a = 0; a < deck.length; a++) {
        newDeck.push(deck[a] * 2)
    }
    console.log(deck)
    return newDeck
}

/**
 *  Creates triplicates of every 3 found in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with triplicate 3s
 */
export function threeOfEachThree(deck) {
    let newArray = []
    for (let d = 0; d < deck.length; d++) {
        if (deck[d] === 3) {
            newArray.push(deck[d])
            newArray.push(deck[d])
        }
        newArray.push(deck[d])
    }
    return newArray
}

/**
 * Extracts the middle two cards from a deck.
 * Assumes a deck is always 10 cards.
 *
 * @param {number[]} deck of 10 cards
 *
 * @returns {number[]} deck with only two middle cards
 */
export function middleTwo(deck) {
    let m = (deck.length / 2) - 1
    return [deck[m], deck[m + 1]]
}

/**
 * Moves the outside two cards to the middle.
 *
 * @param {number[]} deck with even number of cards
 *
 * @returns {number[]} transformed deck
 */

export function sandwichTrick(deck) {
    let newArray = []
    for (let i = 1; i < deck.length - 1; i++) {
        newArray.push(deck[i])
    }
    newArray.splice((deck.length - 2) / 2, 0, deck[deck.length - 1], deck[0])
    return newArray
}

/**
 * Removes every card from the deck except 2s.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with only 2s
 */
export function twoIsSpecial(deck) {
    let newArray = []
    for (let d of deck) {
        if (d === 2) {
            newArray.push(d)
        }
    }
    return newArray
}

/**
 * Returns a perfectly order deck from lowest to highest.
 *
 * @param {number[]} deck shuffled deck
 *
 * @returns {number[]} ordered deck
 */
export function perfectlyOrdered(deck) {
    return [...deck.sort(function (a, b) { return a - b })]
}

/**
 * Reorders the deck so that the top card ends up at the bottom.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} reordered deck
 */
export function reorder(deck) {
    return [...deck.reverse()]
}