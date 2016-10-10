var _ = require('underscore');

exports.mergeParams = function(object, params) {
    var paramNames = Object.getOwnPropertyNames(params);
	_.each(paramNames, function(param) {
		object[param] = params[param];
	});
};
