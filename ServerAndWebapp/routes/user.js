var router = require('express').Router();
var response = require('../utils').response;
var services = require('../services');

/* Get user info */
router.get('/:userId', function(req, res) {
	services.user.getUser(req.params)
	.then(function(user) {
		res.json(response.success(user));
	})
	.catch(function(err) {
		res.json(response.error(err));
	});
});

/* Create a new user */
router.post('/', function(req, res) {
	services.user.createUser(req.body)
	.then(function(user) {
		res.json(response.success(user));
	})
	.catch(function(err) {
		res.json(response.error(err));
	});
});

/* Login user */
router.post('/login', function(req, res) {
	services.user.loginUser(req.body)
	.then(function(user) {
		res.json(response.success(user));
	})
	.catch(function(err) {
		res.json(response.error(err));
	});
});

module.exports = router;
