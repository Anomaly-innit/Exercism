//
// This is only a SKELETON file for the 'Bob' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const hey = (message) => {
  const trimmed = message.trim();
  const isSilence = trimmed === '';
  const isQuestion = trimmed.endsWith('?');
  const isYelling = trimmed === trimmed.toUpperCase() && trimmed !== trimmed.toLowerCase();

  if (isSilence) {
    return "Fine. Be that way!";
  } else if (isYelling && isQuestion) {
    return "Calm down, I know what I'm doing!";
  } else if (isYelling) {
    return "Whoa, chill out!";
  } else if (isQuestion) {
    return "Sure.";
  } else {
    return "Whatever.";
  }
};
