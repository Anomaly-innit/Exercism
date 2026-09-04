//
// This is only a SKELETON file for the 'BookStore' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const cost = (books) => {
  const order = {
    one: 0,
    two: 0,
    three: 0,
    four: 0,
    five: 0,
  };
  for (let i = 0; i < books.length; i++) {
    if (books[i] === 1) {
      order.one++;
    } else if (books[i] === 2) {
      order.two++;
    } else if (books[i] === 3) {
      order.three++;
    } else if (books[i] === 4) {
      order.four++;
    } else if (books[i] === 5) {
      order.five++;
    }
  }

  const counts = Object.values(order);
  const groups = [];

  while (counts.some((c) => c > 0)) {
    let groupSize = 0;
    for (let i = 0; i < counts.length; i++) {
      if (counts[i] > 0) {
        counts[i]--;
        groupSize++;
      }
    }
    groups.push(groupSize);
  }

  while (groups.includes(5) && groups.includes(3)) {
    groups.splice(groups.indexOf(5), 1);
    groups.splice(groups.indexOf(3), 1);
    groups.push(4, 4);
  }

  const GROUP_PRICE = {
    1: 800,
    2: 800 * 2 * 0.95,
    3: 800 * 3 * 0.9,
    4: 800 * 4 * 0.8,
    5: 800 * 5 * 0.75,
  };

  return groups.reduce((total, size) => total + GROUP_PRICE[size], 0);
};