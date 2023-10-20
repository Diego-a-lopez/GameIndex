
//PRIMERA PARTE: Búsqueda por ID o nombre

function selectImage (tipo,imagen){
	
	imagen.alt='Tipo ' + tipo;
		
	switch (tipo){
		case 'normal': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/3/32/latest/20170114100442/Tipo_normal.gif";
		break;	
		case 'fighting': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/b/b7/latest/20170114100336/Tipo_lucha.gif";
		break;
		case 'flying': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/e/e1/latest/20191118232224/Tipo_volador.gif";
		break;
		case 'poison': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/1/10/latest/20191118232220/Tipo_veneno.gif";
		break;
		case 'ground': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/1/1d/latest/20191118232216/Tipo_tierra.gif";
		break;
		case 'rock': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/e/e0/latest/20170114100446/Tipo_roca.gif";
		break;
		case 'bug': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/f/fe/latest/20191118232226/Tipo_bicho.gif";
		break;
		case 'ghost': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/4/47/latest/20170114100329/Tipo_fantasma.gif";
		break;
		case 'steel': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/d/d9/latest/20191118232245/Tipo_acero.gif";
		break;
		case 'fire': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/c/ce/latest/20170114100331/Tipo_fuego.gif";
		break;
		case 'water': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/9/94/latest/20191118232235/Tipo_agua.gif";
		break;
		case 'grass': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/d/d6/latest/20170114100444/Tipo_planta.gif";
		break;
		case 'electric': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/1/1b/latest/20170114100155/Tipo_el%C3%A9ctrico.gif";
		break;
		case 'psychic': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/1/15/latest/20170114100445/Tipo_ps%C3%ADquico.gif";
		break;
		case 'ice': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/4/40/latest/20170114100333/Tipo_hielo.gif";
		break;
		case 'dragon': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/0/01/latest/20170114100154/Tipo_drag%C3%B3n.gif";
		break;
		case 'dark': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/8/82/latest/20191118232327/Tipo_siniestro.gif";
		break;
		case 'fairy': imagen.src = "https://images.wikidexcdn.net/mwuploads/wikidex/b/bc/latest/20170114100332/Tipo_hada.gif";
		break;
	}
}



function traducirHabilidad(habilidadIngles,habilidadCastellano){
	
	var urlHabilidad= "https://pokeapi.co/api/v2/ability/"+habilidadIngles;
	
	fetch(urlHabilidad)
    .then(response => {
		if (response.ok){
			return response.json();
			
		}else{
			throw Error('Error');
		}
	})	
    .then(response => habilidadCastellano.textContent = response.names[5].name)
    .catch(error => M.toast({html: error.message}));
	
}

function traducirMovimiento(moveIngles, nuevoMove){
	
	var urlMove = "https://pokeapi.co/api/v2/move/"+moveIngles;
	
	fetch(urlMove)
    .then(response => {
		if (response.ok){
			return response.json();
			
		}else{
			throw Error('Error');
		}
	})	
    .then(response => nuevoMove.textContent = response.names[5].name)
    .catch(error => M.toast({html: error.message}));
	
}



function showPokemon(jsonObj) {

	var pokemon = jsonObj;
       
    var divNombreID = document.createElement('div');
    var idPoke = document.createElement('B');
    var nombrePoke = document.createElement('p');
          
    var divImagen = document.createElement('div');
    var imagenPoke = document.createElement('img');
    
    var divTipos = document.createElement('div');
    var tiposPoke = document.createElement('B');
    var firstTypeImage = document.createElement('img');
    var secondTypeImage = document.createElement('img');
    
    var divAP = document.createElement('div');
	var alturaypesoPoke = document.createElement('b');
	
    var divAbilities = document.createElement('div');
    var tituloHabilidades = document.createElement('b');
    var habilidadesPoke = document.createElement('ul');
    
    var divStats = document.createElement('div');
    var tituloStats = document.createElement('b');
    var statsPoke = document.createElement('ul'); 
    
    var divMoves = document.createElement('div');
    var tituloMoves = document.createElement('b');
    var movesPoke = document.createElement('ul');
     
    
    divNombreID.id= "nombreID";
    divImagen.id= "imagenPoke";
    divTipos.id = "tiposPoke";
    divAP.id = "alturaypeso";
    divAbilities.id = "habilidadesPoke";
    divStats.id = "statsPoke";
    divMoves.id = "movesPoke";
    
    
    //Nombre e ID
    idPoke.id= 'idPoke';
    idPoke.textContent = pokemon['id']; //+ ': ';
    
    nombrePoke.id='nombrePoke';
    nombrePoke.textContent = pokemon['name'];
    
    divNombreID.appendChild(idPoke);
    divNombreID.appendChild(nombrePoke);
    
    
    
    //Imagen
    imagenPoke.id = 'imagenPokemon';
    imagenPoke.alt = 'Imagen de ' + pokemon['name'];
    imagenPoke.src = pokemon['sprites']['other']['official-artwork']['front_default'];
    
    divImagen.appendChild(imagenPoke);
    
 
    //Tipos del pokémon
    var nTipos = pokemon.types.length;
    
    firstTypeImage.id='imagenTipo1';
    selectImage(pokemon['types'][0]['type']['name'], firstTypeImage);
    
    tiposPoke.textContent = 'Tipo: ';
    
    tiposPoke.appendChild(firstTypeImage);
		
	if (nTipos == 2){//En caso de que tenga dos tipos
		
		secondTypeImage.id='imagenTipo2';
		selectImage(pokemon['types'][1]['type']['name'], secondTypeImage);
		
		tiposPoke.appendChild(secondTypeImage);	
	}
    
    divTipos.appendChild(tiposPoke);
    
 
	//altura y peso
    alturaypesoPoke.textContent = "Altura: " + pokemon['height'] + "dm" 
								+ " Peso: " + pokemon['weight'] + "hg" ;
    
    divAP.appendChild(alturaypesoPoke);
    
    
    //Habilidades  
    var nHabilidades = pokemon.abilities.length;
    
    for (var i = 0; i < nHabilidades; i++) {
      var habilidad = document.createElement('li');
      traducirHabilidad(pokemon.abilities[i].ability.name, habilidad);   
      habilidadesPoke.appendChild(habilidad);
    }
    
    tituloHabilidades.textContent = 'Habilidades:';
    divAbilities.appendChild(tituloHabilidades);
    
    divAbilities.appendChild(habilidadesPoke);
    
    
 
    //Estadísticas:
    var PS = document.createElement('li');
    PS.textContent='PS: ' + pokemon.stats[0].base_stat;
    
    var ATQ = document.createElement('li');
    ATQ.textContent='Ataque: ' + pokemon.stats[1].base_stat;
    
    var DEF = document.createElement('li');
    DEF.textContent='Defensa: ' + pokemon.stats[2].base_stat;
    
    var ATQ_ESP = document.createElement('li');
    ATQ_ESP.textContent='Ataque especial: ' + pokemon.stats[3].base_stat;
    
    var DEF_ESP = document.createElement('li');
    DEF_ESP.textContent='Defensa especial: ' + pokemon.stats[4].base_stat;
    
    var VEL = document.createElement('li');
    VEL.textContent='Velocidad: ' + pokemon.stats[5].base_stat;
    
    
    statsPoke.appendChild(PS);
    statsPoke.appendChild(ATQ);
    statsPoke.appendChild(DEF);
    statsPoke.appendChild(ATQ_ESP);
    statsPoke.appendChild(DEF_ESP);
    statsPoke.appendChild(VEL);
    
    tituloStats.textContent = 'Estadísticas:';
    divStats.appendChild(tituloStats);
      
    divStats.appendChild(statsPoke);
    

    //Movimientos
    var nMoves = pokemon.moves.length;
    for (var j = 0; j < nMoves; j++) {
      var move = document.createElement('li');
      traducirMovimiento(pokemon.moves[j].move.name,move)
      movesPoke.appendChild(move);
    }
    
    movesPoke.id = 'listaMoves';
    
    tituloMoves.textContent = 'Movimientos que puede aprender: ' + '('+ nMoves +')';
    divMoves.appendChild(tituloMoves);

    
    divMoves.appendChild(movesPoke);
    
    
    
    //Mostrar resultado 
    document.querySelector('#error-buscar').innerHTML = '';
        
    var resultado = document.getElementById("resultado-busqueda");
    resultado.innerHTML=""; 
      
    resultado.appendChild(divNombreID);
    resultado.appendChild(divImagen);
    resultado.appendChild(divTipos);
    resultado.appendChild(divAP);
    resultado.appendChild(divAbilities);
    resultado.appendChild(divStats);
    resultado.appendChild(divMoves); 
}



document.querySelector('#boton_buscar').addEventListener('click',event  => {
   
   var pokemon = document.querySelector('input#lector').value;
   var stringDate= "https://pokeapi.co/api/v2/pokemon/"+pokemon.toLowerCase();

   fetch(stringDate)
   .then(response => {   
	  
	   status = response.status;
	   
	   if (response.ok){
			return response.json();
	  } else {
			throw Error('Error');
			
		}
	})	
    .then(response =>showPokemon(response))
    .catch(error => {
		 if (pokemon == ''){ //Error: No se ha introducido nada
			document.querySelector('#error-buscar').innerHTML = 
			'Por favor: Introduzca un Pokemon o un ID correctamente';
			
		} else if (status == 404){//No se encontro o se introduce mal los datos
			document.querySelector('#error-buscar').innerHTML = 
			'Error: Por favor, introduzca correctamente el ID o el nombre del Pokemon';
			
		} else { //No existe conexion
			document.querySelector('#error-buscar').innerHTML = 
			"Error: No existe ninguna conexión a internet. Se precisa conexión para realizar la búsqueda";
		}
		
	});
});



//SEGUNDA PARTE: Filtrado por tipos
function listarUnTipo(tipoPoke){
	
	var newListPokes = [];
	var nPokesLista = tipoPoke.pokemon.length;
	
	for(i=0;i<nPokesLista;i++){
		newListPokes.push(tipoPoke['pokemon'][i]['pokemon']);
	}
	mostrarListaPokes(newListPokes);	
}


function listarDosTipos(tipoPoke1,tipoPoke2){
	
	var newListPokes = [];
	var nPokesLista1 = tipoPoke1.pokemon.length;
	var nPokesLista2 = tipoPoke2.pokemon.length;
	
	for(i=0;i<nPokesLista1;i++){
		for(j=0;j<nPokesLista2;j++){
			if(tipoPoke1.pokemon[i].pokemon.name == tipoPoke2.pokemon[j].pokemon.name){
				newListPokes.push(tipoPoke2.pokemon[j].pokemon);			
				break;
			}
		}
	}
		
	if (newListPokes.length == 0){
		document.querySelector('#error-filtro').innerHTML = 'No existen pokemons con estos dos tipos';
	} else {
		mostrarListaPokes(newListPokes);
	}
}


function mostrarListaPokes(ListaPokes){
	
	document.querySelector('#error-filtro').innerHTML= ''; 
	var resultadoFiltro = document.getElementById("resultado-filtro");
	resultadoFiltro.innerHTML="";		
		
	var texto = document.createElement('h3');
	var listaFinal = document.createElement('ul');
	
	texto.textContent = 'Seleccione el pokemon que desee buscar';
	listaFinal.id = 'listaFiltro'; 	

	for(i=0;i<ListaPokes.length;i++){
		var pkmn = document.createElement('li');
		var newlink = document.createElement('a');
		newlink.id= 'linkPoke';
		var nombrePoke;
		
		nombrePoke = ListaPokes[i]['name'];
		newlink.textContent = nombrePoke;
		
		urlPoke = ListaPokes[i]['url'];

		newlink.setAttribute('href', '#');
		newlink.setAttribute('aria-controls', 'resultado-busqueda');
		newlink.setAttribute('onclick', 'mostrarPokemon("https://pokeapi.co/api/v2/pokemon/'+newlink.textContent+'"'+')');

		pkmn.appendChild(newlink);
		listaFinal.appendChild(pkmn);
	}  
	
	resultadoFiltro.appendChild(texto);
	resultadoFiltro.appendChild(listaFinal);	
}


function mostrarPokemon(urlPoke){
	
    fetch(urlPoke)
    .then(response => {
		if (response.ok){
			return response.json();
		}else{
			throw Error('Error');
		}
	})
		
    .then(response =>showPokemon(response))
        
    .catch(error => document.querySelector('#error-filtro').innerHTML = 
			"Error: No existe ninguna conexión a internet. Se precisa conexión para realizar la búsqueda");

}

//Funcion para contar el numero de checkbox seleccionados
function countTypesSelected(){
  var count=0;
  for(i=0;i<document.ftipos.tipo.length;i++){
    if(document.ftipos.tipo[i].checked)
      count++;
  }
  return count;
}


document.querySelector('#boton_tipo').addEventListener('click',event  => {
	
	var nTiposSelected= countTypesSelected();
	var primerTipo;
	var segundoTipo;
	var listaPokes;
	
	if ((nTiposSelected > 2) || (nTiposSelected <= 0)){
		
		document.querySelector('#error-filtro').innerHTML = 'Error: Por favor, seleccione 1 o 2 tipos';
		
	} else { //En caso de que haya al menos un tipo seleccionado
		
		for(i=0;i<document.ftipos.tipo.length;i++){
			if(document.ftipos.tipo[i].checked){
				primerTipo = document.ftipos.tipo[i].value;
				break;
			}
		}
	
		fetch("https://pokeapi.co/api/v2/type/"+primerTipo)
		.then(response => {
			if (response.ok){
				return response.json();
			}else{
				throw Error('Error');
			}
		})
				
		.then(response => {
					
			if(nTiposSelected == 2){// Si hay un segundo tipo seleccionado se hace un segundo fetch
			
				for(j=i+1;j<document.ftipos.tipo.length;j++){
					if(document.ftipos.tipo[j].checked){
						segundoTipo = document.ftipos.tipo[j].value;
						break;
					}
				}

				fetch("https://pokeapi.co/api/v2/type/"+segundoTipo)
				.then(response2 => {
					if (response2.ok){
						return response2.json();
					}else{
						throw Error('Error');
					}
				})

				.then(response2 =>listarDosTipos(response, response2))			
				.catch(error => M.toast({html: error.message}));
				
			} else {
				listarUnTipo(response);
			}})

		.catch(error => document.querySelector('#error-filtro').innerHTML = 
			"Error: No existe ninguna conexión a internet. Se precisa conexión para realizar la búsqueda");
					
	}
			
});
