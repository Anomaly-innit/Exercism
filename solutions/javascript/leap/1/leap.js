//
// This is only a SKELETON file for the 'Leap' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isLeap = (number) => {
  if(number % 4 === 0 && number % 100 !== 0){
    return true;
  }else if(number % 400 === 0 && number % 100 === 0){
    return true;
  }else{
    return false;
  }
};
