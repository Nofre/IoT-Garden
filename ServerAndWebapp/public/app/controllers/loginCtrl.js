'use strict';
var app = angular.module('iotGarden');

app.controller('loginController', function($scope, $state, MainService) {
  $scope.login = function() {
    MainService.login($scope.user.email, $scope.user.password,
        function(data) {
          $scope.user.email = "";
          $scope.user.password = "";
          $scope.main.isLogged = true;
          $state.go('dashboard');
        },
        function(message) {
          console.log(message);
        }
    );
  }
});
