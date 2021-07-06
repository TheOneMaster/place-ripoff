const { QMainWindow, QFrame} = require("@nodegui/nodegui");
const { Pixel } = require('./pixel');

const win = new QMainWindow();
win.resize(width=512, height=512);
win.setWindowTitle("/r/Place ripoff");


function createPixelGrid(parent, number, parent_size){

    let pixel_size = parent_size/number;
    let pixel_grid = [];

    for (let i=0; i < number**2; i++){

        row = Math.trunc(i / number) * pixel_size;
        column = (i % number) * pixel_size;
        pixel = new Pixel(parent, pixel_size, [row, column], 'white');
    }

    return pixel_grid;
}

const pixelGrid = createPixelGrid(win, 32, 512);

win.show();
// global.win = win;

