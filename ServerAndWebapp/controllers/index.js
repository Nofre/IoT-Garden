var router = require('express').Router();

router.use('/api', require('./api'))

router.get('/', function(req, res) {
	res.render('index');
});

module.exports = router;
