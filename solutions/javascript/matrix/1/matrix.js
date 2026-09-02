//
// This is only a SKELETON file for the 'Matrix' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Matrix {
  constructor(givenString) {
    this.myMatrix = givenString.split('\n').map((row) => row.split(' ').map(Number));
  }

  get rows() {
    return this.myMatrix;
  }

  get columns() {
    return this.myMatrix[0].map((_, colIndex) =>
      this.myMatrix.map((row) => row[colIndex])
    );
  }
}
