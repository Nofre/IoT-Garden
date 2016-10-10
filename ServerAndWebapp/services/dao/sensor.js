var Promise = require("bluebird");
var Sensor = require('../../models/Sensor');
var aux = require('../../utils').auxMethods;

exports.createSensor = createSensor;
exports.getAllSensors = getAllSensors;
exports.getSensorByIds = getSensorByIds;
exports.updateSensor = updateSensor;

function createSensor(params) {
	var sensor = new Sensor();
	aux.mergeParams(sensor, params);
	return sensor.save();
}

function getAllSensors(params) {
	var query = Sensor.find({ gardenId : params.gardenId });
	if (params.select) query.select(params.select.join(' '));
	return query.exec();
}

function getSensorByIds(sensorId, gardenId) {
	var query = Sensor.findOne({ _id : sensorId, 'gardenId': gardenId });
	return query.exec();
}

function updateSensor(params) {
	var sensor = new Sensor();
	aux.mergeParams(sensor, params);
	return sensor.save();
}