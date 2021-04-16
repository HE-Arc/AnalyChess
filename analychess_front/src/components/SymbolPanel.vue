<template>
    <div class="container d-flex justify-content-center">
        <div class="row justify-content-md-center d-inline-flex">
            <div class="col p-0">
                <ul class="list-group" id="movUl">
                    <li class="list-group-item"><button mov-id="0" type="button" class="btn btn-sm" v-on:click="addMove">!</button>Good move</li>
                    <li class="list-group-item"><button mov-id="1" type="button" class="btn btn-sm" v-on:click="addMove">?</button>Mistake</li>
                    <li class="list-group-item"><button mov-id="2" type="button" class="btn btn-sm" v-on:click="addMove">!!</button>Brillant move</li>
                    <li class="list-group-item"><button mov-id="3" type="button" class="btn btn-sm" v-on:click="addMove">??</button>Blunder</li>
                    <li class="list-group-item"><button mov-id="4" type="button" class="btn btn-sm" v-on:click="addMove">!?</button>Interestiong move</li>
                    <li class="list-group-item"><button mov-id="5" type="button" class="btn btn-sm" v-on:click="addMove">?!</button>Dubious move</li>
                    <li class="list-group-item"><button mov-id="6" type="button" class="btn btn-sm" v-on:click="addMove">□</button>Only move</li>
                    <li class="list-group-item"><button mov-id="7" type="button" class="btn btn-sm" v-on:click="addMove">⨀</button>Zugzwang</li>
                </ul>
            </div>
            <div class="col p-0">
                <ul class="list-group" id="posUl">
                    <li class="list-group-item"><button pos-id="0" type="button" class="btn btn-sm" v-on:click="addPos">=</button>Equal position</li>
                    <li class="list-group-item"><button pos-id="1" type="button" class="btn btn-sm" v-on:click="addPos">∞</button>Unclear position</li>
                    <li class="list-group-item"><button pos-id="2" type="button" class="btn btn-sm" v-on:click="addPos">⩲</button>White is slightly better</li>
                    <li class="list-group-item"><button pos-id="3" type="button" class="btn btn-sm" v-on:click="addPos">⩱</button>Black is slightly better</li>
                    <li class="list-group-item"><button pos-id="4" type="button" class="btn btn-sm" v-on:click="addPos">±</button>White is better</li>
                    <li class="list-group-item"><button pos-id="5" type="button" class="btn btn-sm" v-on:click="addPos">∓</button>Black is better</li>
                    <li class="list-group-item"><button pos-id="6" type="button" class="btn btn-sm" v-on:click="addPos">+-</button>White is winning</li>
                    <li class="list-group-item"><button pos-id="7" type="button" class="btn btn-sm" v-on:click="addPos">-+</button>Black is winning</li>
                </ul>
            </div>
            <div class="col p-0">
                <ul class="list-group" id="tagUl">
                    <li class="list-group-item"><button tag-id="0" type="button" class="btn btn-sm" v-on:click="addTag">N</button>Novelty</li>
                    <li class="list-group-item"><button tag-id="1" type="button" class="btn btn-sm" v-on:click="addTag">↑↑</button>Development</li>
                    <li class="list-group-item"><button tag-id="2" type="button" class="btn btn-sm" v-on:click="addTag">↑↑</button>Initiative</li>
                    <li class="list-group-item"><button tag-id="3" type="button" class="btn btn-sm" v-on:click="addTag">→</button>Attack</li>
                    <li class="list-group-item"><button tag-id="4" type="button" class="btn btn-sm" v-on:click="addTag">⇆</button>Counterplay</li>
                    <li class="list-group-item"><button tag-id="5" type="button" class="btn btn-sm" v-on:click="addTag">⊕</button>Time trouble</li>
                    <li class="list-group-item"><button tag-id="6" type="button" class="btn btn-sm" v-on:click="addTag">=∞</button>With compensation</li>
                    <li class="list-group-item"><button tag-id="7" type="button" class="btn btn-sm" v-on:click="addTag">∆</button>With the idea</li>

                </ul>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "SymbolPanel",
    mounted()
    {
        this.read(0)
    },
    data()
    {
        return{
            index: 0
        }
    },
    props:
    {
        game: null,
    },
    methods:
    {
        // Worst code of my life no time to do better
        addMove(e)
        {
            // remove last one selected
            let id = parseInt(e.target.getAttribute("mov-id"));
            if(this.game.moves[this.index].moveStrength == id)
            {
                e.target.parentElement.setAttribute("class", "list-group-item")
                this.game.moves[this.index].moveStrength = -1;
            }
            else{
            this.remove("movUl")
                this.game.moves[this.index].moveStrength = id;
                e.target.parentElement.classList.add("selected")
            }
            
        },
        addPos(e)
        {
            let id = parseInt(e.target.getAttribute("pos-id"));
            if(this.game.moves[this.index].PosEvaluation == id)
            {
                e.target.parentElement.setAttribute("class", "list-group-item")
                this.game.moves[this.index].PosEvaluation = -1;
            }
            else
            {
            this.remove("posUl")
    
                this.game.moves[this.index].PosEvaluation = id;
                e.target.parentElement.classList.add("selected")
            }
            
            
        },
        addTag(e)
        {
            let id = parseInt(e.target.getAttribute("tag-id"));
            if(this.game.moves[this.index].tags.indexOf(id) == -1)
            {
                console.log(id)
                this.game.moves[this.index].tags.push(id);
                e.target.parentElement.classList.add("selected")
            }
            else{
                e.target.parentElement.setAttribute("class", "list-group-item")
                let i = this.game.moves[this.index].tags.indexOf(id)
                this.game.moves[this.index].tags.splice(i, 1)
            }
        },
        read(index)
        {
            this.index = index
            this.remove("movUl")
            this.remove("posUl");
            this.remove("tagUl")
            if(this.game.moves[this.index].moveStrength != -1)
            {
                document.getElementById("movUl").children[this.game.moves[this.index].moveStrength].classList.add("selected")
            }
            if(this.game.moves[this.index].PosEvaluation != -1)
            {
                document.getElementById("posUl").children[this.game.moves[this.index].PosEvaluation].classList.add("selected")
            }
            for(let i of this.game.moves[this.index].tags)
            {
                console.log(i)
                document.getElementById("tagUl").children[i].classList.add("selected")
            }

        },
        remove(ul)
        {
            for(let li of document.getElementById(ul).children)
                {
                    li.setAttribute("class", "list-group-item")
                }
        } 
    }
};
</script>
<style >
.list-group-item{
    width: 250px;
}

.selected{
    background-color: teal;
}

</style>