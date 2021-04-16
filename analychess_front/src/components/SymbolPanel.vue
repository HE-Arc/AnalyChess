<template>
	<div class="container d-flex justify-content-center">
		<div class="row justify-content-md-center d-inline-flex">
			<div class="col p-0">
				<ul class="list-group">
					<li class="list-group-item"><button type="button" class="btn btn-sm">!</button>Good move</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">?</button>Mistake</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">!!</button>Brillant move</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">??</button>Blunder</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">!?</button>Interestiong move</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">?!</button>Dubious move</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">□</button>Only move</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">⨀</button>Zugzwang</li>
				</ul>
			</div>
			<div class="col p-0">
				<ul class="list-group">
					<li class="list-group-item"><button type="button" class="btn btn-sm">=</button>Equal position</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">∞</button>Unclear position</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">⩲</button>White is slightly better</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">⩱</button>Black is slightly better</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">±</button>White is better</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">∓</button>Black is better</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">+-</button>White is winning</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">-+</button>Black is winning</li>
				</ul>
			</div>
			<div class="col p-0">
				<ul class="list-group">
					<li class="list-group-item"><button type="button" class="btn btn-sm">N</button>Novelty</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">↑↑</button>Development</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">↑</button>Initiative</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">→</button>Attack</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">⇆</button>Counterplay</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">⊕</button>Time trouble</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">=∞</button>With compensation</li>
					<li class="list-group-item"><button type="button" class="btn btn-sm">∆</button>With the idea</li>

				</ul>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "SymbolPanel",
};
</script>
<style >
.list-group-item{
	width: 250px;
}

</style>
