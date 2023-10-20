var staticUrl ='https://pokeapi.co/api/v2/pokemon'
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
if (urlParams.get('staticUrl') != null){
var staticUrl =	urlParams.get('staticUrl')
}


var getJSON = function(url, callback, z) {	
	var xhr = new XMLHttpRequest();
	xhr.open('GET', url, true);
	xhr.responseType = 'json';
	xhr.onload = function() {
		var status = xhr.status;
		console.log(status)
		if (status == 200) {
			callback(null, xhr.response, z);
		} 
		else {
			window.location.href = "Error.html?errorCode=" + xhr.status;
		}
	};
	xhr.send();
};

function addlistener(btn, num){
	
	btn[num].addEventListener("click", function(){
		window.location.href = "PokeInfo.html?pokemon=" + btn[num].name;
	});
	
}

var retrieve = function(err, data, z) {
	var table = document.getElementById('myTable')
	var nexButton = document.getElementById('nextpoke')
	
	if(nexButton != null){
		nexButton.remove();
		z = z - 1;
	}
	
	if (err !== null) {
		alert('Something went wrong: ' + err);
	} else {
		for (var i = 0; i < data.results.length; i++){
			//console.log(data)
			var row = `<tr id = "pokebody${i}">
				<td><img src="imgs/pokeball.png" alt="pokeball"></td>
				<td><button name="${data.results[i].name}" id = "text">${data.results[i].name}</button></td>
				</tr>`
			table.innerHTML += row
		}
	}

	table.innerHTML += `<tr id = "nextpoke">
			<td><img src="imgs/pokeball.png" alt="Pokeball"></td>
			<td><button id = "text">Next Pokemons</button></td>
		</tr>`
	var btn = document.querySelectorAll("button");
	for (var c = 0; c < data.results.length + z; c++){
		console.log(data.results.length)
		addlistener(btn, c)
	}

	z+=i;

	//console.log(data.results.length)
	//console.log(z);

	btn[z].addEventListener("click", function(){

		getJSON(data.next, retrieve, (z+1));

	});

	};

getJSON(staticUrl, retrieve, 0);
