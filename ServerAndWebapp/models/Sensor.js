var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var sensorSchema = new Schema({
	_id: Number,
	gardenId: String,
	samples: [{ value: Number, date: Date }],
	unitMeasure: String,
	name: String,

	/* Metadata */
    createdAt: Date,
    updatedAt: Date
});

//Trigger before save
sensorSchema.pre('save', function(next) {
    this.updatedAt = new Date();
    if (!this.createdAt) {
    	this.createdAt = this.updatedAt;
    	this.samples = [];
    }
    var length = this.samples.length;
    if (length > 10) {
        var newSamples = [];
        for(var i = length-10; i < length; ++i) newSamples.push(this.samples[i]);
        this.samples = [];
        for (var i = 0; i < 10; ++i) this.samples.push(newSamples[i]);
    }
    next();
});

//Create & export the model
var Sensor = mongoose.model('Sensor', sensorSchema);

module.exports = Sensor;
