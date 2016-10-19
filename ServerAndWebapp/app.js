var express = require('express'),
	app = express(),
	path = require('path'),
	bodyParser = require('body-parser');


// view engine setup
app.set('views', './views');
app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(require('./controllers'));


app.use(function(req, res, next){
  res.render('error');
});

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
  app.use(function(err, req, res, next) {
    res.status(500).json({ message : 'Internal Server Error' });
  });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
  res.status(500).json({ message : 'Internal Server Error' });
});


module.exports = app;
