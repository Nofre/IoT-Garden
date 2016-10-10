var Promise = require("bluebird");
var User = require('../../models/User');
var aux = require('../../utils').auxMethods;

exports.createUser = createUser;
exports.getUser = getUser;
exports.login = login;

function createUser(params) {
	var user = new User();
	aux.mergeParams(user, params);
	return user.save();
}

function getUser(params) {
	var query = User.find({ _id : params.userId});
	if (params.select) query.select(params.select.join(' '));
	return query.exec();
}

function login(params) {
	var query = User.findOne({ email : params.email, password : params.password });
	if (params.select) query.select(params.select.join(' '));
	return query.exec();
}