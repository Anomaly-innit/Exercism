// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */
export function changeWindow(programWindow) {
  programWindow.resize(new Size(400, 300));
  programWindow.move(new Position(100, 150));
  return programWindow;
}

export function Size(width = 80, height = 60) {
  this.width = width;
  this.height = height;
}

Size.prototype.resize = function (newWidth, newHeight) {
  this.width = newWidth;
  this.height = newHeight;
};

export function Position(x=0,y=0){
  this.x = x;
  this.y = y;
}

Position.prototype.move = function (newX, newY) {
  this.x = newX;
  this.y = newY;
};

export class ProgramWindow {
  constructor() {
    this.screenSize = new Size(800, 600);
    this.size = new Size();
    this.position = new Position();
  }
  resize(newSize) {
    let width = newSize.width;
    let height = newSize.height;

    const maxWidth = this.screenSize.width - this.position.x;
    const maxHeight = this.screenSize.height - this.position.y;

    if (width < 1) {
      width = 1;
    } else if (width > maxWidth) {
      width = maxWidth;
    }

    if (height < 1) {
      height = 1;
    } else if (height > maxHeight) {
      height = maxHeight;
    }

    this.size.width = width;
    this.size.height = height;
  }
  move(newPosition) {
  let x = newPosition.x;
  let y = newPosition.y;

  const maxX = this.screenSize.width - this.size.width;
  const maxY = this.screenSize.height - this.size.height;

  if (x < 0) {
    x = 0;
  } else if (x > maxX) {
    x = maxX;
  }

  if (y < 0) {
    y = 0;
  } else if (y > maxY) {
    y = maxY;
  }

  this.position.x = x;
  this.position.y = y;
  }

}