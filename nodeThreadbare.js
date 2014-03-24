 var session = sessions.lookupOrCreate(request,{
   lifetime:604800
 });

  response.setHeader('Set-Cookie', session.getSetCookieHeaderValue());

 function( request, response, callback) {

   // perform some logic on the request or response objects
   console.log(request.url);


   // then fire our callback, and pass the request 
   // and response objects down the chain
   callback(request, response, function(){

   });

 }

var http = require('http'), 
    session = require('./lib/core').session;

// let's create a basic http server!
http.createServer(function (request, response) {

  // before we process any part of the request, let's use the session middle-ware!
  session(request, response, function(request, response){

    // now we can access request.session

    // after the session middleware has executed, let's finish processing the request
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.write('request.session: \n' + JSON.stringify(request.session, 2, true));
    response.end();

  });

}).listen(8080);

/* server started */  
console.log('> hello world running on port 8080');
