<template>
<div class="arrow" :style="style"></div>
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
        style() {
            const arrowLength = Math.sqrt(Math.pow(this.sFile - this.eFile, 2) + Math.pow(this.sRow - this.eRow, 2));
            const rotation = Math.atan2(this.eRow - this.sRow, this.eFile - this.sFile);

            console.log(rotation);

            return  `
                width: ${100. / BOARD_SIZE * arrowLength}%;
                bottom: ${100. / BOARD_SIZE * (this.sRow) + 50. / BOARD_SIZE - ARROW_PERCENT_SIZE / 2}%;
                left: ${100. / BOARD_SIZE * (this.sFile) + 50. / BOARD_SIZE}%;
                transform: rotate(${-rotation}rad);
                background:${this.color};
                border-color:${this.color};
            `;
        }
    }
}
</script>

<style>

.arrow
{
    position: absolute;
    height: calc(100% / 40);
    opacity: .5;
    transform-origin: center left;
    transition: width 100ms linear, transform 100ms linear, color 100ms;
}

.arrow::after
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

</style>

