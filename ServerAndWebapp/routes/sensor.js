var router = require('express').Router();
var response = require('../utils').response;
var services = require('../services');

/* Create a sensor */
// router.post('/', function(req, res) {
// 	services.sensor.createSensor(req.body)
// 	.then(function(sensor){
// 		res.json(response.success(sensor));
// 	})
// 	.catch(function(err) {
// 		res.json(response.error(err));
// 	});
// });

router.post('/addSample', function(req, res) {
	services.sensor.addSample(req.body)
	.then(function(sensor){
		res.json(response.success());
	})
	.catch(function(err) {
		res.json(response.error(err));
	});
});

module.exports = router;