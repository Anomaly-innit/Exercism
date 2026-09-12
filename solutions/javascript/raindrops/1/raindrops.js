//
// This is only a SKELETON file for the 'Raindrops' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const convert = (num) => {
  let word = '';
  if(num % 3 === 0){
    word = word + 'Pling';
  }if(num % 5 === 0){
    word = word + 'Plang';
  }if(num % 7 === 0){
    word = word + 'Plong';
  }
  if(word === ''){
    return String(num);
  }else{
  return word;
  }
};
