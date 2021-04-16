<template>
  <div class="container d-flex justify-content-center">
    <div class="row justify-content-md-center d-inline-flex">
      <div class="col p-0">
        <ul class="list-group">
          <li class="list-group-item">Good move</li>
          <li class="list-group-item">Mistake</li>
          <li class="list-group-item">Brillant move</li>
          <li class="list-group-item">Blunder</li>
          <li class="list-group-item">Interestiong move</li>
          <li class="list-group-item">Dubious move</li>
          <li class="list-group-item">Only move</li>
          <li class="list-group-item">Zugzwang</li>
        </ul>
      </div>
      <div class="col p-0">
        <ul class="list-group">
          <li class="list-group-item">Equal position</li>
          <li class="list-group-item">Unclear position</li>
          <li class="list-group-item">White is slightly better</li>
          <li class="list-group-item">Black is slightly better</li>
          <li class="list-group-item">White is better</li>
          <li class="list-group-item">Black is better</li>
          <li class="list-group-item">White is winning</li>
          <li class="list-group-item">Black is winning</li>
        </ul>
      </div>
      <div class="col p-0">
        <ul class="list-group">
          <li class="list-group-item">Novelty</li>
          <li class="list-group-item">Development</li>
          <li class="list-group-item">Initiative</li>
          <li class="list-group-item">Attack</li>
          <li class="list-group-item">Counterplay</li>
          <li class="list-group-item">Time trouble</li>
          <li class="list-group-item">With compensation</li>
          <li class="list-group-item">With the idea</li>

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