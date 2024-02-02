/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(remTime) {
    switch (remTime) {
        case 0:
            return 'Lasagna is done.'
            break
        case undefined:
            return 'You forgot to set the timer.'
            break
        default:
            return 'Not done, please wait.'
    }
}

export function preparationTime(layers, average = 2) {
    return layers.length * average
}

export function quantities(layers) {
    let sauce = 0
    let noodles = 0
    for (let l of layers) {
        if (l === 'sauce') {
            sauce += 1
        }
        else if (l === "noodles") {
            noodles += 1
        }
    }
    return { 'noodles': noodles * 50, 'sauce': sauce * 0.2 }
}

export function addSecretIngredient(array1, array2) {
    array2.push(array1[array1.length - 1])
}

export function scaleRecipe(recipe, portions) {
    let newRecipe = {}
    for (let r in recipe) {
        newRecipe[r] = (recipe[r] / 2) * portions
    }
    return newRecipe
}