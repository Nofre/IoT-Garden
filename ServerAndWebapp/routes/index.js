var router = require('express').Router();

router.use(function(req, res, next) {
	res.header("Access-Control-Allow-Origin", "*");
	res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
	next();
});

// REST API METHODS
router.use('/api/user', require('./user.js'));
router.use('/api/garden', require('./garden.js'));
router.use('/api/sensor', require('./sensor.js'));

// /* ANGULAR WEBAPP */
router.get('/', function(req, res, next) {
  res.render('index');
});

module.exports = router;
