//
// This is only a SKELETON file for the 'Line Up' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const format = (name, number) => {
  const lastTwo = number % 100;
  const lastOne = number % 10;

  let suffix = "th";
  if ( lastTwo < 11 || lastTwo > 13){
    if (lastOne === 1) suffix = 'st';
    else if (lastOne === 2) suffix = 'nd';
    else if (lastOne === 3) suffix = 'rd';
  }
  return `${name}, you are the ${number}${suffix} customer we serve today. Thank you!`;
};
