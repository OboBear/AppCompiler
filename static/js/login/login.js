//! function($) {
//	$(document).on("click", "ul.nav li.parent > a > span.icon", function() {
//		$(this).find('em:first').toggleClass("glyphicon-minus");
//	});
//	$(".sidebar span.icon").find('em:first').addClass("glyphicon-plus");
//}(window.jQuery);
//
//$(window).on('resize', function() {
//	if ($(window).width() > 768) $('#sidebar-collapse').collapse('show')
//})
//$(window).on('resize', function() {
//	if ($(window).width() <= 767) $('#sidebar-collapse').collapse('hide')
//})
function loginAction() {
	var account = document.getElementById('email');
	var password = document.getElementById('password');
//	alert("accutnL"+account.value+password.value)
	var isEmail = testEmail(account.value);
	var isPhone = testMobile(account.value);
	if (!isEmail && !isPhone) {
		alert("请输入正确的账号")
		return;
	}	
	if (password.value.length < 6) {
		alert("密码不能少于6位")
		return;
	}
	var postParams="";
	if (isEmail)
		postParams += 'userEmail='+account.value
	else if(isPhone)
		postParams += 'userPhoneNum='+account.value
	postParams += '&password='+password.value
	postParams += '&type=web'
	send("/login", postParams, callBackLogin);
}

function callBackLogin(result) {
	var jsonResult = eval("("+result+")");
	if (jsonResult.errorCode == 0) {
		document.location.href = "/index"
	}
	else {
		alert(jsonResult.errorMsg)
	}
}

function registerAction() {
	document.location.href = "/register"
}
