// aspetta che la pagina venga caricata
$(document).ready(function () {
	//viene chiamata questa funzione quando l'oggetto dropanni viene cambiato
    $('#dropanni').on('change', function() {
    	//prendo l'url della pagina vuoto e ci aggiungo l'anno che è stato selezionato
  		var url = window.location.origin + window.location.pathname;
  		var anno = $('#dropanni').val();
		url = url + '?dropanni=' + anno;
		window.location.href = url;
	});
});