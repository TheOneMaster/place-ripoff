const {QFrame, WidgetEventTypes} = require("@nodegui/nodegui");

class Pixel extends QFrame{
    /*
    Params:

    parent: parent window
    color: color (either string or rgb code)
    */
    static _COLORS = ['white', 'blue'];
    
    constructor(parent, size, location, color='white'){
        super(parent);
        
        // Instance Variables
        this.color = color;
        this.parent = parent;
        this.size = size;

        // Configuring the frame
        this.resize(size, size);
        this.setInlineStyle(`background-color: ${color}`);

        row = location[0];
        column = location[1];

        this.move(column, row);


        const events = [WidgetEventTypes.MouseButtonPress, WidgetEventTypes.MouseButtonDblClick];

        for (let i of events) {
            this.addEventListener(i, (nativeEvt) => this.changeColor());
        };
    }

    changeColor(new_color=null){
        if (new_color === null){
            let current_index = Pixel._COLORS.indexOf(this.color);
            let new_index = (current_index + 1) % 2;
            let new_color = Pixel._COLORS[new_index];
            this.color = new_color;
        }
        this.setInlineStyle(`background-color: ${this.color}`);
    }


}



exports.Pixel = Pixel;