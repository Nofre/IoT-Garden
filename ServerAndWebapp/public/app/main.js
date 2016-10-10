// Create module
angular.module('iotGarden', ['ui.router', 'ngCookies'])

// Routes configuration
.value('$anchorScroll', angular.noop)
.config(['$stateProvider', '$urlRouterProvider', '$locationProvider', '$anchorScrollProvider',
    function($stateProvider, $urlRouterProvider, $locationProvider, $anchorScrollProvider) {
      $urlRouterProvider.otherwise('/');
      $stateProvider
      .state('login', {
          url: '/login',
          templateUrl: 'app/views/login.html',
          controller: 'loginController'
      })
      .state('dashboard', {
          url: '/',
          templateUrl: 'app/views/dashboard.html',
          controller: 'dashboardController'
      });
    }
])
.run(['$rootScope', '$state', '$stateParams', 'MainService',
  function($rootScope,   $state,   $stateParams, MainService) {
    $rootScope.$on('$stateChangeStart', function(ev, toState, toParams, from, fromParams) {
      var loggedIn = MainService.isLoggedIn();
      if (!loggedIn  && toState.name !== 'login') {
        ev.preventDefault();
        $state.go('login');
      }
      else if (loggedIn && toState.name === 'login') {
        ev.preventDefault();
        $state.go('dashboard');
      }
    });
  }
]);
