<!-- Frontendでの処理ロジックを記述 -->
<script>
  let title = "Data Get";
  let income;
  let rooms; 
  let age;
  let data = []; // htmlタグの方の{datalist}の部分と同じ変数

  async function findData() {
    // APIにアクセスする定型文
    const response = await fetch("http://localhost:5000/calc/" + income + "/" + rooms + "/" + age);
    // 表示用変数にデータを入れると、画面も再描画される。
    data = await response.json();
  }
</script>

<main>
  <h1 class="title">This is sample page. {title}</h1>
  <table>
  <tr>
	<td>Income</td>
  	<td><input bind:value={income} /></td>
  </tr>
  <tr>
  	<td>Rooms</td>
	<td><input bind:value={rooms} /></td>
  </tr>
  <tr>
  	<td>House Age</td>
	<td><input bind:value={age} /></td>
  </tr>
  </table>
  <button on:click={findData}>Get Data.</button>
  <div />
  <hr />
  <table>
  <tr>
  	<td>Price</td>
        <td>{data.price}</td>
  </tr>
  </table>
  <hr />
  <a href="/">Top</a>
</main>

<!-- 画面の装飾をする -->
<style>
  /* class=titleとなっている箇所を装飾する */
  .title {
    color: snow;
    background-color: teal;
  }
</style>
