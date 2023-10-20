
var pics = [
	"imgs/Pokemon_logo.png",
	"imgs/722.png"
];

var btn = document.querySelectorAll("button");

var img = document.querySelector("img");

var counter = 1;

btn[0].addEventListener("click", function(){


if (document.getElementsByName("pokemon") != null){
	window.location.href = "PokeList.html?staticUrl=" + "https://pokeapi.co/api/v2/pokemon/" + document.getElementsByName("pokemon");
	}
window.location.href = "PokeList.html?staticUrl=" + "https://pokeapi.co/api/v2/pokemon";
});
