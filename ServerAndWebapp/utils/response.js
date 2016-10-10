exports.errorTypes = errorTypes();
exports.IOTGardenError = IOTGardenError;

exports.success = function(data) {
	var response = newResponse();
	response.code = 200;
	response.data = data;
	return response;
};

exports.error = function(err) {
	var response = newResponse();
	response.code = err.code || 500;
	response.message = err.message || 'Internal server error.';
	return response;
};

function newResponse() {
	return {
		"code": null,
	    "message": null,
	    "data": {}
	};
}

function errorTypes() {
	return {
		incorrectParameters : {
			code : 400,
			message : 'Incorrect or missing parameters.'
		},
		accessDenied : {
			code : 403,
			message : 'Access denied.'
		},
		internalServerError : {
			code : 500,
			message : 'Internal server error. Fancy trying again in a minute or so?'
		},
		databaseError : {
			code : 502,
			message : 'Database connection error'
		}
	};
}

function IOTGardenError(err) {
	this.code = err.code;
    this.message = err.message;
	Error.captureStackTrace(this, IOTGardenError);
}
IOTGardenError.prototype = Object.create(Error.prototype);
IOTGardenError.prototype.constructor = IOTGardenError;
