<template>
<div class="arrow-drawing-zone">
    <template v-for="rowIndex in BOARD_SIZE">
        <div
            class="arrow-drawing-zone-cell"
            v-for="fileIndex in BOARD_SIZE"
            @dragstart="startArrow(fileIndex - 1, rowIndex - 1)"
            @dragover="updateArrow(fileIndex - 1, rowIndex - 1)"
            @dragend="endArrow(fileIndex - 1, rowIndex - 1)"
            @click="toggleArrow(fileIndex - 1, rowIndex - 1)"
            :key="rowIndex + '' + fileIndex"
            :style="`left: calc(12.5% * ${fileIndex - 1});bottom: calc(12.5% * ${rowIndex - 1})`"
        ></div>
    </template>
</div>
</template>

<script>

const BOARD_SIZE = 8;

export default {
    name: 'ArrowDrowingZone',
    data() {
        return {
            BOARD_SIZE
        }
    },
    methods: {
        toggleArrow(fileIndex, rowIndex){
            this.$emit("arrowStart", fileIndex, rowIndex);
            this.$emit("arrowEnd", fileIndex, rowIndex);
        },
        startArrow(fileIndex, rowIndex){
            this.$emit("arrowStart", fileIndex, rowIndex);
        },
        updateArrow(fileIndex, rowIndex){
            this.$emit("arrowUpdate", fileIndex, rowIndex);
        },
        endArrow(fileIndex, rowIndex){
            this.$emit("arrowEnd", fileIndex, rowIndex);
        },
    }
}
</script>


<style>

.arrow-drawing-zone
{
    position: absolute;
    z-index: 1000;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
}

.arrow-drawing-zone-cell
{
    position: absolute;
    width: 12.5%;
    height: 12.5%;
}

</style>

