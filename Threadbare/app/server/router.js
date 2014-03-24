module.exports = function(app){
	app.get('/', function(req, res){
		res.render('index');
	});
	app.get('/chat', function(req, res){
		res.render('chat');
	});
	app.get('*', function(req, res){
		res.render('404');
	});
};