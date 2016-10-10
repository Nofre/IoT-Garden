var Promise = require("bluebird");
var Garden = require('../../models/Garden');
var aux = require('../../utils').auxMethods;

exports.createGarden = createGarden;
exports.getGardenById = getGardenById;
exports.getGardenInfo = getGardenInfo;

function createGarden(params) {
	var garden = new Garden();
	aux.mergeParams(garden, params);
	return garden.save();
}

function getGardenById(params) {
	var query = Garden.find({ _id : params.gardenId });
	if (params.select) query.select(params.select.join(' '));
	return query.exec();
}

function getGardenInfo(params) {
	var query = Garden.find({ ownerId : params.ownerId});
	if (params.select) query.select(params.select.join(' '));
	return query.exec();
}