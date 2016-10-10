var Promise = require('bluebird');
var _ = require('underscore');
var dao = require('./dao');
var response = require('../utils').response;
var errorTypes = response.errorTypes;
var IOTGardenError = response.IOTGardenError;

exports.createSensor = createSensor;
exports.addSample = addSample;

function createSensor(params) {
	return new Promise(function(resolve, reject) {
		if(params._id && params.gardenId && params.unitMeasure && params.name) {
			params.select = ['_id'];
			dao.garden.getGardenById(params)
			.then(function(garden) {
				if(garden) return dao.sensor.createSensor(params);
				else reject(new IOTGardenError(errorTypes.incorrectParameters));
			})
			.then(function(sensor) {
				resolve(sensor);
			})
			.catch(function(err) {
				reject(err);
			});
		}
		else reject(new IOTGardenError(errorTypes.incorrectParameters));
	});
}

function addSample(params) {
	return new Promise(function(resolve, reject) {
		if(params._id && params.gardenId && params.value && params.date) {
			params.select = ['_id'];
			dao.sensor.getSensorByIds(params._id, params.gardenId)
			.then(function(sensor) {
				if(sensor) {
					var samples = sensor.samples;
					samples.push({'value': params.value, 'date': params.date});
					if(samples.length > 10) samples.slice(1, 11);
					sensor.samples = samples;
					return dao.sensor.updateSensor(sensor);
				}
				else reject(new IOTGardenError(errorTypes.incorrectParameters));
			})
			.then(function(sensor) {
				resolve();
			})
			.catch(function(err) {
				reject(err);
			});
		}
		else reject(new IOTGardenError(errorTypes.incorrectParameters));
	});
}