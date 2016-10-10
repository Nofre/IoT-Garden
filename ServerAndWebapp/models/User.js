var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var userSchema = new Schema({
	/* Auth Data */
	name: String,
	email: String,
	password: String,

	/* Metadata */
    createdAt: Date,
    updatedAt: Date
});

//Trigger before save
userSchema.pre('save', function(next) {
    this.updatedAt = new Date();
    if (!this.createdAt) this.createdAt = this.updatedAt;
    next();
});

//Create & export the model
var User = mongoose.model('User', userSchema);

module.exports = User;
