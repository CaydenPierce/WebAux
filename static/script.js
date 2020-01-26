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
    updater = document.getElementById("updater");
    updater.innerHTML = "Loading song...";
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
            if (data['success'] == 1) {
                updater.innerHTML = "Playing song";
            } else {
                alert("There was an error.");
                updater.innerHTML = "There was an error.";
            }

			})

}


