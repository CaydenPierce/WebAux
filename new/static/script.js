window.onload = function(){
    main();
}

function main() {
    var songForm = document.getElementById("song")
    songForm.addEventListener("submit", play);
}

function play(event) {
	event.preventDefault();
	var form = document.getElementById("song");
	var songname = form['songname'].value
	console.log(songname);
	fetch('/', {
		method: 'POST',
		headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json'
		},
		body: JSON.stringify({ "songname" : songname })
		}).then((response) => response.json())
		.then((data) => {
			console.log('Success:', data);
			})

}


