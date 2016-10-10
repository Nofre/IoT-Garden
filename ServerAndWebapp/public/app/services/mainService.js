'use strict';
var app = angular.module('iotGarden');

app.factory('MainService', function($cookies) {

  // Internal variables
  var url = '';

  function login(email, password) {
		var settings = {
      "async": true,
      "crossDomain": true,
      "url": url,
      "method": "POST",
      "headers": {
        "content-type": "application/x-www-form-urlencoded"
      },
      "data": {
        "email" : email,
        "password" : password
      }
    };
    return $.ajax(settings);
	};

  return {
    login: function(email, password, success, error) {
      login(email, password).done(function(response) {
        if(response.code === 200) {
          $cookies.put('userId', response.data.userId);
          $cookies.put('gardenId', response.data.gardenId);
          success(response.data);
        }
        else error(null);
      });
    },
    getToken: function() {
      var userId = $cookies.get('userId');
      var gardenId = $cookies.get('gardenId');
      if (userId && gardenId) return {
        "userId": userId,
        "gardenId": gardenId
      };
      logout();
      return null;
    },
    isLoggedIn: function() {
      if ($cookies.get('userId') && $cookies.get('gardenId')) return true;
      else return false;
    },
    logout: function() {
      $cookies.remove('userId');
      $cookies.remove('gardenId');
    }
  };
});
