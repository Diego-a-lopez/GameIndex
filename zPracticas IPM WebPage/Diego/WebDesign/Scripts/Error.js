const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
if (urlParams.get('errorCode') != null){
var error =	urlParams.get('errorCode')
}

var pics = [
	"imgs/722.png"
];

var btn = document.querySelectorAll("button");

var img = document.querySelector("img");

var counter = 1;

btn[0].addEventListener("click", function(){

window.location.href = "PokePage.html";

});

function response(){
		var frame = document.getElementById('error_frame')
	if (error == 404){
		var row =`
		<p id = "text">Error : ${error}<p>
		<p id = "text">It seems we could not find what you were looking for</p>
		`
		frame.innerHTML += row
	}
	else if (error == 410){
		var row =`
		<p id = "text">Error : ${error}<p>
		<p id = "text">Item deleted</p>
		`
		frame.innerHTML += row
	}
	else if ((error >= 300)&& (error <= 399)){
		var row =`
		<p id = "text">Error : ${error}<p>
		<p id = "text">redirection issue</p>
		`
		frame.innerHTML += row
	}
	else if ((error >= 500)&& (error <= 599)){
		var row =`
		<p id = "text">Error : ${error}<p>
		<p id = "text">Internal server error</p>
		`
		frame.innerHTML += row
	}
	else{
		var row =`
		<p id = "text">Error : ${error}<p>
		<p id = "text">Unexpected error</p>
		`
		frame.innerHTML += row
	}
}

response()
console.log(error)

