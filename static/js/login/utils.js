
function send(urlPath, postParams, callback) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", urlPath, true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhr.onreadystatechange = function() {
		var XMLHttpReq = xhr;
		if (XMLHttpReq.readyState == 4) {
			if (XMLHttpReq.status == 200) {
				var text = XMLHttpReq.responseText;
				console.log(text);
				callback(text)
			}
		}
	};
	xhr.send(postParams)
}
