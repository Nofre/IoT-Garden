var router = require('express').Router(),
	fs = require("fs"),
	sqlite3 = require("sqlite3").verbose();


var file = "data.db";
var exists = fs.existsSync(file);
var db = new sqlite3.Database(file);

db.serialize(function() {
	if(!exists) {
		db.run("CREATE TABLE data (thing TEXT)");
	}
});
db.close();


router.post('/data', function(req, res) {
	console.log(req.body);

	db = new sqlite3.Database(file);

	var stmt = db.prepare("INSERT INTO data VALUES (?)");
	stmt.run("Thing #" + rnd);
	stmt.finalize();

	db.close();

	res.send({ msg: 'ok' });
});


router.get('/data', function(req, res) {

	db = new sqlite3.Database(file);
	var data = {};

	db.each("SELECT * FROM data", function(err, row) {
		data.add([row.s1, row.s2, row.s3, row.s4, row.s5, row.s6, row.s7, row.s8]);
	});

	db.close();

	res.send({ msg: 'ok' });
});

module.exports = router
