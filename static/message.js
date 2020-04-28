function getCookie(name){
    var pattern = RegExp(name + "=.[^;]*");
    var matched = document.cookie.match(pattern);
    if(matched){
        var cookie = matched[0].split('=');
        return cookie[1];
    }
    return false;
}

function getPostId() {
	if(!window.location.pathname.startsWith('/post/')) return null;
	var parts = window.location.pathname.split('/');
	if(parts.length < 3) return;
	return id = parts[2];
}

function loadNewMessages(latestID, finishedCallback) {
	var userid = getCookie('arguserid');
	var id = getPostId();
	post(
		'/post/' + id + '/' + latestID + '/getRecent',
		'',
		function() {
			res = JSON.parse(this.responseText);
			other = null;
			for(var i = 0; i < res.length; i++) {
				sent = res[i]['UserID'] == userid || (res[i]['UserID'] != other && other != null);
				other = res[i]['UserID'];
				addMessage(res[i]['MessageContent'], res[i]['MessageID'], sent);
			}
			finishedCallback();
		}
	);
}

function sendMessage() {
	var user = getCookie("arguserinfo");
	if(! user) {
		alert("You must be logged in to perform this action.");
		return;
	}

	var message = document.getElementById( "message" );
	var messages = document.getElementById( "messages" );
	
	if( message.value.trim() == "" ) {
		return;
	}

	post('/post/' + getPostId() + '/send', {'text' : message.value}, function() {;
		if(this.responseText == "false") {
			alert("Oops! You can't do that.");
			return;
		}
		addMessage(message.value, this.responseText, true);
		message.value = "";
	});
}

function addMessage(content, id, sent) {
	var newMsg = document.createElement( "div" );
	var inner = document.createElement( "div" );
	var textP = document.createElement( "p" );

	textP.appendChild( document.createTextNode( content ) );
	inner.appendChild( textP );
	newMsg.appendChild( inner );
	inner.classList.add( "chatMessage" );
	inner.classList.add( sent ? "sentchat" : "recvchat" );
	newMsg.classList.add( "messagehack" );
	newMsg.id = id;

	messages.appendChild( newMsg );
}

function post(url, data, responseHandler) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send(JSON.stringify(data));
	xhr.onload = responseHandler;
}
