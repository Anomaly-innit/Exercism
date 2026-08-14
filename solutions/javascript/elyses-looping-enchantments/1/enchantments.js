// @ts-check

/**
 * Determine how many cards of a certain type there are in the deck
 *
 * @param {number[]} stack
 * @param {number} card
 *
 * @returns {number} number of cards of a single type there are in the deck
 */
export function cardTypeCheck(stack, card) {
  let num = 0;
  for(const i of stack){
    if(i===card){
      num +=1
    }
  }
  return num;
}

/**
 * Determine how many cards are odd or even
 *
 * @param {number[]} stack
 * @param {boolean} type the type of value to check for - odd or even
 * @returns {number} number of cards that are either odd or even (depending on `type`)
 */
export function determineOddEvenCards(stack, type) {
  // 🚨 Use a `for...of` loop
  let odd = 0;
  let even = 0;
  for(const i of stack){
    if(i%2 === 0){
      even +=1
    }else{
      odd +=1
    }
  }
  if(type === true){
    return even;
  }else{
    return odd;
  }
}