'use strict';
var app = angular.module('iotGarden');

app.controller('generalController', function($scope, $state, MainService) {
  $scope.main = {
    isLogged : MainService.isLoggedIn()
  };

  $scope.logout = function() {
    $scope.main.isLogged = false;
    $scope.user = undefined;
    MainService.logout();
    if (!$scope.$$phase) $scope.$apply();
    $state.go('login');
  }

});
