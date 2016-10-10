var Promise = require('bluebird');
var _ = require('underscore');
var dao = require('./dao');
var response = require('../utils').response;
var errorTypes = response.errorTypes;
var IOTGardenError = response.IOTGardenError;

exports.getUser = getUser;
exports.createUser = createUser;
exports.loginUser = loginUser;

function getUser(params) {
	return new Promise(function(resolve, reject) {
		if(params.userId) {
			params.select = ['_id', 'name'];
			dao.user.getUser(params)
			.then(function(user) {
				resolve(user);
			})
			.catch(function(err) {
				reject(err);
			});
		}
		else reject(new IOTGardenError(errorTypes.incorrectParameters));
	});
}

function createUser(params) {
	return new Promise(function(resolve, reject) {
		if(params.name && params.email && params.password) {
			dao.user.createUser(params)
			.then(function(user) {
				resolve(user);
			})
			.catch(function(err) {
				reject(err);
			});
		}
		else reject(new IOTGardenError(errorTypes.incorrectParameters));
	});
}

function loginUser(params) {
	return new Promise(function(resolve, reject) {
		if(params.email && params.password) {
			params.select = ['_id', 'name'];
			dao.user.login(params)
			.then(function(user) {
				return Promise.join(user, dao.garden.getGardenInfo({ ownerId: user._id }));
			})
			.then(function(info) {
				var res = {
					userId: info[0]._id,
					name: info[0].name,
					gardenId: info[1][0]._id
				}
				resolve(res);
			})
			.catch(function(err) {
				reject(err);
			});
		}
		else reject(new IOTGardenError(errorTypes.incorrectParameters));
	});
}