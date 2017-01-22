var express = require('express'),
	app = express(),
	path = require('path'),
	bodyParser = require('body-parser'),
	fs = require('fs'),
	sqlite3 = require('sqlite3').verbose();


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


var file = 'data.db';
var exists = fs.existsSync(file);
var db = new sqlite3.Database(file);

db.serialize(function() {
	if(!exists) {
		db.run('CREATE TABLE data(date TEXT, exth1 REAL, exth2 REAL, h1 REAL, h2 REAL, extt1 REAL, extt2 REAL, t1 REAL, t2 REAL, light REAL);');
	}
});
db.close();

module.exports = app;
