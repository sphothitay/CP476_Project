function getCookie(name){
    var pattern = RegExp(name + "=.[^;]*")
    var matched = document.cookie.match(pattern)
    if(matched){
        var cookie = matched[0].split('=')
        return cookie[1]
    }
    return false
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
	
	var newMsg = document.createElement( "div" );
	var inner = document.createElement( "div" );
	var textP = document.createElement( "p" );
	
	textP.appendChild( document.createTextNode( message.value ) );
	inner.appendChild( textP );
	newMsg.appendChild( inner );
	inner.classList.add( "chatMessage" ); // TODO: sent/recvd
	newMsg.classList.add( "messagehack" );
	
	messages.appendChild( newMsg );
	message.value = "";
}
