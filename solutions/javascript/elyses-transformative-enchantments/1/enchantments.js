// @ts-check

/**
 * Double every card in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with every card doubled
 */
export function seeingDouble(deck) {
  let doubleNum = [];
  for(const num of deck){
    doubleNum.push(num*2)
  }
  return doubleNum;
}

/**
 *  Creates triplicates of every 3 found in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with triplicate 3s
 */
export function threeOfEachThree(deck) {
  let trippleThree = [];
  for(const num of deck){
    if(num === 3){
      for(let i=0; i < 3; i++){
        trippleThree.push(3);
      }
    }else {
      trippleThree.push(num);
    }
  }
  return trippleThree;
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
  const middle = deck.length / 2;
  return [deck[middle - 1], deck[middle]];
}

/**
 * Moves the outside two cards to the middle.
 *
 * @param {number[]} deck with even number of cards
 *
 * @returns {number[]} transformed deck
 */

export function sandwichTrick(deck) {
  const outside = [ deck[deck.length - 1], deck[0]];
  deck.pop();
  deck.shift();
  const middle = deck.length / 2;
  deck.splice(middle, 0, ...outside);
  return deck;
}

/**
 * Removes every card from the deck except 2s.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with only 2s
 */
export function twoIsSpecial(deck) {
  let twos  = [];
  for(const card of deck){
    if(card === 2){
      twos.push(card);
    }
  }
  return twos;
}

/**
 * Returns a perfectly order deck from lowest to highest.
 *
 * @param {number[]} deck shuffled deck
 *
 * @returns {number[]} ordered deck
 */
export function perfectlyOrdered(deck) {
  const result =  deck.sort((a, b) => a - b);
  return result;
}

/**
 * Reorders the deck so that the top card ends up at the bottom.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} reordered deck
 */
export function reorder(deck) {
  return deck.reverse();
}
