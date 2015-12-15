! function($) {
	$(document).on("click", "ul.nav li.parent > a > span.icon", function() {
		$(this).find('em:first').toggleClass("glyphicon-minus");
	});
	$(".sidebar span.icon").find('em:first').addClass("glyphicon-plus");
}(window.jQuery);

$(window).on('resize', function() {
	if ($(window).width() > 768) $('#sidebar-collapse').collapse('show')
})
$(window).on('resize', function() {
	if ($(window).width() <= 767) $('#sidebar-collapse').collapse('hide')
})



function loginAction() {

	var account = document.getElementById('email');
	var password = document.getElementById('password');

	var isEmail = testEmail(account.value);

	//	if (!isEmail) {
	//		alert("请输入正确的邮箱")
	//		return;
	//	}
	//	
	//	if (password.length < 6) {
	//		alert("密码不能少于6位")
	//		return;
	//	}

	//	document.location.href = "/index";

	var postParams="";
	postParams += 'account='+account.value
	postParams += '&password='+password.value
	postParams += '&type=web'
	send("/login", postParams, callBackLogin);
}

function testEmail(str) {
	var reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
	if (reg.test(str)) {
		return true
	} else {
		return false
	}
}

function callBackLogin(result) {
	eval("alert('" + result + "')")
	if (result == ("success")) {
		document.location.href = "/index";
	}
}
