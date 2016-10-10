var router = require('express').Router();
var response = require('../utils').response;
var services = require('../services');

/* Get garden info */
router.get('/:ownerId', function(req, res) {
	services.garden.getGardenInfo(req.params)
	.then(function(garden) {
		res.json(response.success(garden));
	})
	.catch(function(err) {
		res.json(response.error(err));
	});
});

/* Create a garden */
router.post('/', function(req, res) {
	services.garden.createGarden(req.body)
	.then(function(garden){
		res.json(response.success(garden));
	})
	.catch(function(err) {
		res.json(response.error(err));
	});
});

module.exports = router;