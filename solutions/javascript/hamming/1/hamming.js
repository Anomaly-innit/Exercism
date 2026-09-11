//
// This is only a SKELETON file for the 'Hamming' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const compute = (RNA, DNA) => {
  if(RNA.length !== DNA.length){
    throw new Error('strands must be of equal length');
  }
  let distance = 0;
  for(let i = 0; i < RNA.length; i++){
    if(RNA[i] !== DNA[i]){
      distance++;
    }
  }
  return distance;
};
