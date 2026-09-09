//
// This is only a SKELETON file for the 'Triangle' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Triangle {
  constructor(...sides) {
    this.sides = sides;
    this.isValid =
      this.sides.every((side) => side > 0) &&
      this.sides[0] + this.sides[1] > this.sides[2] &&
      this.sides[1] + this.sides[2] > this.sides[0] &&
      this.sides[2] + this.sides[0] > this.sides[1];
  }

  get isEquilateral() {
    if (!this.isValid) {
      return false;
    }
    return this.sides.every((side) => side === this.sides[0]);
  }

  get isIsosceles() {
    if (!this.isValid) {
      return false;
    }
    return (
      this.sides[0] === this.sides[1] ||
      this.sides[1] === this.sides[2] ||
      this.sides[2] === this.sides[0]
    );
  }

  get isScalene() {
    if (!this.isValid) {
      return false;
    }
    return (
      this.sides[0] !== this.sides[1] &&
      this.sides[1] !== this.sides[2] &&
      this.sides[2] !== this.sides[0]
    );
  }
}
