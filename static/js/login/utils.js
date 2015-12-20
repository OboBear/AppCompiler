
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

function testEmail(str) {
	var reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
	if (reg.test(str)) {
		return true
	} else {
		return false
	}
}

function testMobile(str) {
    var re = /^1\d{10}$/
    if (re.test(str)) {
        return true
    } else {
        return false
    }
}