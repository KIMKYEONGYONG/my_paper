/*!
* Start Bootstrap - Bare v5.0.7 (https://startbootstrap.com/template/bare)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

var filter = "win16|win32|win64|mac";
var mobile = "mobile";
if(navigator.platform){
	if(0 > filter.indexOf(navigator.platform.toLowerCase())){
		 if ( !window.location.href.includes(mobile) ) {
			 location.href= "https://jbit.bufs.ac.kr/~rlaruddyd1/jlv/mobile";
		}
	}else{
		if (  window.location.href.includes(mobile)  ) {
			location.href= "https://jbit.bufs.ac.kr/~rlaruddyd1/jlv/";
			}
	}
}