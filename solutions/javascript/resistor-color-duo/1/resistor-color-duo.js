//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//


export const decodedValue = (set) => {
  const COLORS = [
    'black', 'brown', 'red', 'orange', 'yellow',
    'green', 'blue', 'violet', 'grey', 'white',
  ];
  return COLORS.indexOf(set[0]) * 10 + COLORS.indexOf(set[1]);
};