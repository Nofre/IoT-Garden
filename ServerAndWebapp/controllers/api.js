var router = require('express').Router(),
	fs = require('fs'),
	sqlite3 = require('sqlite3').verbose(),
	file = 'data.db';

router.post('/data', function(req, res) {

	var data = req.body;

	db = new sqlite3.Database(file);
	db.run('INSERT INTO data VALUES ('+data['exth1']+', '+data['exth2']+', '+data['h1']+', '+data['h2']+', '+data['extt1']+', '+data['extt2']+', '+data['t1']+', '+data['t2']+', '+data['light']+')');
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
