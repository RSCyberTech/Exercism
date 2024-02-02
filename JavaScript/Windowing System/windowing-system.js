// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */

export class Size {
    constructor(width = 80, height = 60) {
        this.width = width
        this.height = height
    }
    resize(newWidth, newHeight) {
        this.width = newWidth
        this.height = newHeight
    }
}

export function Position(x = 0, y = 0) {
    this.x = x
    this.y = y
    this.move = function (x, y) {
        this.x = x
        this.y = y
    }
}

export class ProgramWindow {
    constructor() {
        this.screenSize = new Size(800, 600)
        this.size = new Size()
        this.position = new Position()
    }

    resize(x) {
        if (x.width < 1) {
            x.width = 1
        }
        else if (x.width > this.screenSize.width) {
            x.width = (this.screenSize.width - this.position.x)
        }
        if (x.height < 1) {
            x.height = 1
        }
        else if (x.height > this.screenSize.height) {
            x.height = (this.screenSize.height - this.position.y)
        }
        this.size.resize(x.width, x.height)
    }

    move(x) {
        if (x.x < 0) {
            x.x = 0
        }
        else if (x.x > (this.screenSize.width - this.size.width)) {
            x.x = (this.screenSize.width - this.size.width)
        }
        if (x.y < 0) {
            x.y = 0
        }
        else if (x.y > (this.screenSize.height - this.size.height)) {
            x.y = (this.screenSize.height - this.size.height)
        }
        this.position.move(x.x, x.y)
    }
}

export function changeWindow(x) {
    x.resize({ width: 400, height: 300 })
    x.move({ x: 100, y: 150 })
    return x
}