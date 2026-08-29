//
// This is only a SKELETON file for the 'RNA Transcription' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const toRna = (DNA) => {
  let RNA = '';
  for (let i = 0; i < DNA.length; i++) {
    if (DNA[i] === 'G'){
      RNA += 'C';
    }else if (DNA[i] === 'C'){
      RNA += 'G';
    }else if (DNA[i] === 'T'){
      RNA += 'A';
    }else if (DNA[i] === 'A'){
      RNA += 'U';
    }
    
  }
  return RNA;
};
