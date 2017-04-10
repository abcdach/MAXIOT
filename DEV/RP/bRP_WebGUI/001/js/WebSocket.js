

var websocket;
var websocket_auto_connect = 1;
var websocket_device = 1000;
var websocket_ip    = "";
var websocket_port  = "";

var websocket_ip_0     = "127.0.0.1";
var websocket_port_0   = "3002";
var websocket_ip_1     = "127.0.0.1";
var websocket_port_1   = "3002";


var websocket_ip_port = 0;
var websocket_Text = 0;
var websocket_NAME  = "";
var websocket_ERROR = "";
function doConnect() {
    websocket = new WebSocket("ws://"+websocket_ip+":"+websocket_port+"/");
    websocket.onopen    = function(evt){WS_STEP = 3;};
    websocket.onclose   = function(evt){WS_STEP = 0;};
    websocket.onmessage = function(evt){onMessage(evt);};
    websocket.onerror   = function(evt){WS_STEP = 0;};
}
function doSend(message){websocket.send(message);}
function doDisconnect(){websocket.close();}
function websocket_send(Msg){websocket.send(Msg);}
//#############################################################################
//#
//#############################################################################
var WS_STEP = 0;
var WS_TimeOUT = 0;
var WS_TimeOUT = 0;
var WS_Connection_Status = 0;
function websocket_START() {
	//Print_WS_Status("websocket_START");
	WS_Connection_Status = 0;
	WS_STEP = 1;
	setTimeout(websocket_STATE, 100);
}
function websocket_STATE() {
	switch (WS_STEP) {
	case 0:
		if(websocket_auto_connect === 1) WS_STEP = 1; else WS_STEP = 0;
		break;			
	case 1:
		if(websocket_ip_port === 0)
		{
			websocket_ip_port = 1;
			websocket_ip      = websocket_ip_0;
			websocket_port    = websocket_port_0;
		}
		else if(websocket_ip_port === 1)
		{
			websocket_ip_port = 0;
			websocket_ip   	  = websocket_ip_1;
			websocket_port    = websocket_port_1;
		}	
		Print_WS_Status ("Connecting : "+ websocket_ip +" ");
		WS_TimeOUT = 2;
		WS_STEP = 11;
		break;
	case 11: // "Connecting"
		WS_TimeOUT --;
		if (WS_TimeOUT === 0){	
			doConnect();
			WS_Connection_Status = 0;
			WS_TimeOUT = 10;
			WS_STEP = 2;
		}
		break;
	case 2: // "Connecting"
		WS_TimeOUT --;
		if (WS_TimeOUT === 0){	
			websocket.close();
			if(websocket_auto_connect === 1) WS_STEP = 1; else WS_STEP = 0;			
		}
		break;	
	case 3: // "Welcome"
		WS_TimeOUT --;
		if (WS_TimeOUT === 0){	
			websocket.close();
			if(websocket_auto_connect === 1) WS_STEP = 1; else WS_STEP = 0;			
		}
		break;	
	case 4: // "OK"
		break;
	case 5: // "ERROR"
		WS_TimeOUT --;
		if (WS_TimeOUT === 0){	
			websocket.close();
			if(websocket_auto_connect === 1) WS_STEP = 1; else WS_STEP = 0;			
		}
		break;
	default: 
		break;
	}
	setTimeout(websocket_STATE, 1000);	
}

//Print_WS_Status("Connected...  "+ WS_TimeOUT + "s");
//WS_TimeOUT ++;
//var Msg = "{\"N\":\"0\",\"S\":\"0\",\"T\":\"0\",\"V\":\""+WS_TimeOUT+"\"}"; websocket_send(Msg);



function Print_WS_Status(DATA){
	$('#WS_STATUS').text(DATA);
		//MyHeader_wText(DATA);
	}
//#############################################################################
//#
//#############################################################################
var JSON_VALUE;
var JSON_PARSE;
var JSON_DATA = [];
function onMessage(evt) {
	JSON_PARSE = JSON.parse(evt.data);  
	JSON_VALUE = JSON_PARSE.N;
	if (typeof JSON_VALUE !== "undefined") {
		var N_VALUE = Number(JSON_VALUE);
    	if (typeof JSON_VALUE !== "undefined") {
			switch (N_VALUE){
				case 0://"DATA STREAM"
				//#--------------------------------------------------------------	   	  
					var  S_Value = ""; var  T_Value = ""; var  V_Value = "";
				//#--------------------------------------------------------------	  
					JSON_VALUE = JSON_PARSE.S;
					if (typeof JSON_VALUE === "undefined") return 1; S_Value = Number(JSON_VALUE);
					JSON_VALUE = JSON_PARSE.V;
					if (typeof JSON_VALUE === "undefined") return 1; V_Value = JSON_VALUE;
			   //#--------------------------------------------------------------	
					JSON_VALUE = JSON_PARSE.T;
					if (typeof JSON_VALUE !== "undefined"){
						T_Value = JSON_VALUE;
						if(T_Value == "1"){ var DEC = Base64.decode(V_Value); V_Value = DEC;}
					} else T_Value = "0";
			  //#--------------------------------------------------------------			  
					switch (S_Value) {
						case 0: if (typeof Process_Stream_0 !== "undefined") Process_Stream_0(V_Value);break;
						case 1: if (typeof Process_Stream_1 !== "undefined") Process_Stream_1(V_Value);break;
						case 2: if (typeof Process_Stream_2 !== "undefined") Process_Stream_2(V_Value);break;
						case 3: if (typeof Process_Stream_3 !== "undefined") Process_Stream_3(V_Value);break;
						case 4: if (typeof Process_Stream_4 !== "undefined") Process_Stream_4(V_Value);break;
						case 5: if (typeof Process_Stream_5 !== "undefined") Process_Stream_5(V_Value);break;
						case 6: if (typeof Process_Stream_6 !== "undefined") Process_Stream_6(V_Value);break;
						case 7: if (typeof Process_Stream_7 !== "undefined") Process_Stream_7(V_Value);break;
						default: return;
					}	
    	          break;
    	      case 1://"Welcome"
					Print_WS_Status("Device : " + websocket_device);
					var Msg = "{\"N\":\"1\",\"D\":\""+websocket_device+"\"}"; websocket_send(Msg);
					WS_TimeOUT = 10;
					WS_STEP = 3;
					break;
    	      case 2://"OK"
    	    	  	Print_WS_Status("OK");
    	    	  	websocket_NAME = "undefined";
					JSON_VALUE = JSON_PARSE.V;
					if (typeof JSON_VALUE !== "undefined"){
						websocket_NAME = JSON_VALUE;
					} 
					Print_WS_Status(websocket_NAME + " : " + websocket_device);
					WS_STEP = 4;
					break;
    	      case 9://"Error"
	  	    	  	websocket_ERROR = "Error";
					JSON_VALUE = JSON_PARSE.i;
					if (typeof JSON_VALUE !== "undefined"){
						websocket_ERROR = JSON_VALUE;
					} 
					Print_WS_Status(websocket_ERROR);
					WS_TimeOUT = 2;
					WS_STEP = 5;
    	          break;
    	      default:
    	          break;
			}
		}		
	}return 1;
}






