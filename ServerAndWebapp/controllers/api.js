var router = require('express').Router(),
	fs = require('fs'),
	sqlite3 = require('sqlite3').verbose(),
	file = 'data.db';

router.post('/data', function(req, res) {

	var date = req.body.date;
	var values = req.body.values;
	var query = 'INSERT INTO data VALUES ("'+date+'", '+values['exth1']+', '+values['exth2']+', '+values['h1']+', '+values['h2']+', '+values['extt1']+', '+values['extt2']+', '+values['t1']+', '+values['t2']+', '+values['light']+')'

	db = new sqlite3.Database(file);
	db.run(query);
	db.close();

	res.send({ 'msg' : 'ok' });
});


router.get('/data', function(req, res) {

	var data = [];

	db = new sqlite3.Database(file);
	db.all('SELECT * FROM data LIMIT 10 OFFSET (SELECT COUNT(*) FROM data)-10', function(err, rows) {
		res.send({ 'msg' : 'ok', 'data' : rows });
	});
	db.close();
});

module.exports = router
