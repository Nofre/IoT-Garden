'use strict';
var app = angular.module('iotGarden');

app.service('GardenService', function() {

  // Internal variables
  var urlServer = '';

  function getGardenInfo(ownerId, success, error) {
		var settings = {
      "async": true,
      "crossDomain": true,
      "url": urlServer + '/' + ownerId,
      "method": "GET",
      "headers": {
        "content-type": "application/x-www-form-urlencoded"
	    }
	  };
    $.ajax(settings).done(function(response) {
      if (response.code === 200) success(response.data);
      else error(response.message);
    });
	};

  return {
    getGardenInfo: function(ownerId, success, error) {
			return getGardenInfo(ownerId, success, error);
    }
  };
});
