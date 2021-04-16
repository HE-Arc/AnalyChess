<template>
<div :class="{arrow: true, arrowline: !isCell, arrowcell: isCell}" :style="style"></div>
</template>

<script>

const BOARD_SIZE = 8;
const ARROW_PERCENT_SIZE = 4;

export default {
    name: 'Arrow',
    props: {
        color: {
            type: String,
            required: true
        },
        sFile: {
            type: Number,
            require: true
        },
        sRow: {
            type: Number,
            require: true
        },
        eFile: {
            type: Number,
            require: true
        },
        eRow: {
            type: Number,
            require: true
        },
    },
    computed: {
        isCell() {
            return this.sFile == this.eFile && this.sRow == this.eRow;
        },
        style() {
            const arrowLength = Math.sqrt(Math.pow(this.sFile - this.eFile, 2) + Math.pow(this.sRow - this.eRow, 2));
            const rotation = Math.atan2(this.eRow - this.sRow, this.eFile - this.sFile);

            let style = `background:${this.color};`
            if(!this.isCell)
            {
                style += `width: ${100. / BOARD_SIZE * arrowLength}%;`;
                style += `transform: rotate(${-rotation}rad);`;
                style += `bottom: ${100. / BOARD_SIZE * (this.sRow) + 50. / BOARD_SIZE - ARROW_PERCENT_SIZE / 2}%;`;
                style += `left: ${100. / BOARD_SIZE * (this.sFile) + 50. / BOARD_SIZE}%;`;
                style += `border-color:${this.color};`;
            }
            else
            {
                console.log("what");
                style += `bottom: ${100. / BOARD_SIZE * this.sRow}%;`;
                style += `left: ${100. / BOARD_SIZE * this.sFile}%;`;
            }

            console.log(style)

            return style;
        }
    }
}
</script>

<style>


.arrow
{
    position: absolute;
    opacity: 0.7;
}
.arrow.arrowline
{
    z-index: 3; /* In top of the piece */
    height: calc(100% / 40);
    transform-origin: center left;
    transition: width 100ms linear, transform 100ms linear, color 100ms;
}

.arrow.arrowline::after
{
    position: absolute;
    box-sizing: border-box;
    content: "";
    right: 0;
    top: 50%;
    transform: translateY(-50%) rotate(45deg);
    border-color: inherit;
    border-width: 15px;
    border-style: solid;
    border-bottom-color: transparent;
    border-left-color: transparent;
}

.arrow.arrowcell
{
    z-index: 1; /* Bellow the piece */
    width: calc(100% / 8); 
    height: calc(100% / 8); 
}

</style>

