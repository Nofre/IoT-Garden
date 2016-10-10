var Promise = require('bluebird');
var _ = require('underscore');
var dao = require('./dao');
var response = require('../utils').response;
var errorTypes = response.errorTypes;
var IOTGardenError = response.IOTGardenError;

exports.getGardenInfo = getGardenInfo;
exports.createGarden = createGarden;

function getGardenInfo(params) {
	return new Promise(function(resolve, reject) {
		if(params.ownerId) {
			console.log(params);
			params.select = ['_id', 'ownerId'];
			console.log(params);
			dao.garden.getGardenInfo(params)
			.then(function(garden) {
				params.gardenId = garden[0]._id;
				params.select = ['name', 'samples', 'unitMeasure'];
				return dao.sensor.getAllSensors(params);
			})
			.then(function(gardenSensors) {
				return _.sortBy(gardenSensors, '_id');
			})
			.then(function(gardenSensors) {
				resolve(gardenSensors);
			})
			.catch(function(err) {
				reject(err);
			});
		}
		else reject(new IOTGardenError(errorTypes.incorrectParameters));
	});
}

function createGarden(params) {
	return new Promise(function(resolve, reject) {
		if(params.ownerId) {
			params.select = ['_id'];
			dao.user.getUser(params)
			.then(function(user) {
				if(user) return dao.garden.createGarden(params);
				else reject(new IOTGardenError(errorTypes.incorrectParameters));
			})
			.then(function(garden) {
				resolve(garden);
			})
			.catch(function(err) {
				reject(err);
			});
		}
		else reject(new IOTGardenError(errorTypes.incorrectParameters));
	});
}
