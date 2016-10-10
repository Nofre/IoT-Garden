var mongoose = require('mongoose');

module.exports = function() {
    mongoose.Promise = require('bluebird');
    var db = mongoose.connect('', function(err) {
        if (err) console.log(err);
    });
    require('../models/User');
    require('../models/Garden');
    require('../models/Sensor');
};
