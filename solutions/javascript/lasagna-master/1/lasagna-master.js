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
export function cookingStatus(timeLeft) {
  if (timeLeft === undefined) {
    return 'You forgot to set the timer.';
  } else if (timeLeft === 0) {
    return 'Lasagna is done.';
  } else {
    return 'Not done, please wait.';
  }
}

export function preparationTime(layers, averageTime = 2) {
  return layers.length * averageTime;
}

export function quantities(layers) {
  let quant = {
    noodles: 0,
    sauce: 0,
  };
  for (let i = 0; i < layers.length; i++) {
    if (layers[i] === 'noodles') {
      quant.noodles += 50;
    } else if (layers[i] === 'sauce') {
      quant.sauce += 0.2;
    }
  }
  return quant;
}

export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList[friendsList.length - 1]);
}

export function scaleRecipe(recipe, portions) {
  const mult = portions/2;
  const newRecipe = {};
  for (const ingredient in recipe) {
    newRecipe[ingredient] = recipe[ingredient] * mult;
  }
  return newRecipe;
}