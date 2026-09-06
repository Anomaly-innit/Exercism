//
// This is only a SKELETON file for the 'Reverse String' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const reverseString = (word) => {
  const splitString = word.split("");
  const revSplitString = splitString.reverse();
  const connectRevSplitString = revSplitString.join("");
  return connectRevSplitString;
  
};
