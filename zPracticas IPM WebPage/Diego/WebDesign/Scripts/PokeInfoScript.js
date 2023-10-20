var staticUrl ='https://pokeapi.co/api/v2/pokemon/1/'
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
if (urlParams.get('pokemon') != null){
var staticUrl = 'https://pokeapi.co/api/v2/pokemon/' +	urlParams.get('pokemon')
}

var pics = [
	"imgs/Pokemon_logo.png",
	"imgs/722.png"
];

var btn = document.querySelectorAll("button");

var img = document.querySelector("img");



var getJSON = function(url, callback, z) {	
	var xhr = new XMLHttpRequest();
	xhr.open('GET', url, true);
	xhr.responseType = 'json';
	xhr.onload = function() {
		var status = xhr.status;
		if (status === 200) {
			callback(null, xhr.response, z);
		} else {
			window.location.href = "Error.html?errorCode=" + xhr.status;
		}
	};
	xhr.send();
};

var retrieve = function(err, data, z) {
	var frame = document.getElementById('main_frame')
	if (err !== null) {
		alert('Something went wrong: ' + err);
	} else {
		var row = `
			<div class= "row"><div class= "column" id="sprite"><img src=${data.sprites.front_default}></div>
			<div class= "column" id = "NameType"><p>Name: ${data.species.name}</p>`
			//frame.innerHTML += row
			 row += `<p>Types:</p><p>` 
		for (var i = 0; i < data.types.length; i++){
			row += `
			<button id=textButton>${data.types[i].type.name}</button>  
			
			`
		}
		row += `</p></div></div>`
		frame.innerHTML += row
		var row = `
		<div class= "row">
		<div class= "column">
			<p id= "bar1">${data.stats[0].stat.name} :	  [${data.stats[0].base_stat}/714]<progress id="statBar" value=${data.stats[0].base_stat} max="714"></progress></p>
			<p id= "bar1">${data.stats[1].stat.name} :	  [${data.stats[1].base_stat}/504]<progress id="statBar" value=${data.stats[1].base_stat} max="504"></progress></p>
			<p id= "bar1">${data.stats[2].stat.name} :	  [${data.stats[2].base_stat}/614]<progress id="statBar" value=${data.stats[2].base_stat} max="614"></progress></p>
		</div><div class= "column">
			<p id= "bar1">${data.stats[3].stat.name} :	  [${data.stats[3].base_stat}/504]<progress id="statBar" value=${data.stats[3].base_stat} max="504"></progress></p>
			<p id= "bar1">${data.stats[4].stat.name} :	  [${data.stats[4].base_stat}/614]<progress id="statBar" value=${data.stats[4].base_stat} max="614"></progress></p>
			<p id= "bar1">${data.stats[5].stat.name} :	  [${data.stats[5].base_stat}/504] <progress id="statBar" value=${data.stats[5].base_stat} max="504"></progress></p>
		</div></div>		`
		frame.innerHTML += row
		frame.innerHTML += `<p id="text">Abilities</p>`
		var row = `<p>`
		for (var i = 0; i < data.abilities.length; i++){
			row += `
			   <button id=textButton>${data.abilities[i].ability.name}</button>   
			`
			
		}
		row += `</p>`
		frame.innerHTML += row
		frame.innerHTML += `<p id="text">Moves:</p>`
		for (var i = 0; i < data.moves.length; i+=4){
			var row =`<p>`
			for (var j = 0; ((j + i) < data.moves.length) &&  j < 4; j++){
				row += `
				<button id=textButton>${data.moves[j+i].move.name}</button>
				`
			}
			row +=`</p>`
			frame.innerHTML += row
		}
		console.log(data)
	}
};

getJSON(staticUrl, retrieve, 0);

