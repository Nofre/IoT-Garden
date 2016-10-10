var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var gardenSchema = new Schema({
	ownerId: String,
	
	/* Metadata */
    createdAt: Date,
    updatedAt: Date
});

//Trigger before save
gardenSchema.pre('save', function(next) {
    this.updatedAt = new Date();
    if (!this.createdAt) this.createdAt = this.updatedAt;
    next();
});

//Create & export the model
var Garden = mongoose.model('Garden', gardenSchema);

module.exports = Garden;
