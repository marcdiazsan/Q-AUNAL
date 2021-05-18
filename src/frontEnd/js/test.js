function myFunction(){
  var h1 = document.createElement('h1');
  h1.textContent = "New Heading!!!";
  h1.setAttribute('class', 'note');
  document.body.appendChild(h1);
}

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var xhr = new XMLHttpRequest();

xhr.open("GET", "http://0.0.0.0:5000/preguntas");
xhr.send();
xhr.onload = function() {
    var myObject = xhr.responseText;
    var json = JSON.parse(xhr.responseText);
    var count = Object.keys(json).length;
    console.log(count);
};
  
  xhr.onerror = function() { // solo se activa si la solicitud no se puede realizar
    console.log("request error");
  };
  
  xhr.onprogress = function(event) { // se dispara periódicamente
    console.log("Recibido"+event.loaded+"of" +event.total);
  };

