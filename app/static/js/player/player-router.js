'use strict';

angular.module('inforugby')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/players', {
        templateUrl: 'views/player/players.html',
        controller: 'PlayerController',
        resolve:{
          resolvedPlayer: ['Player', function (Player) {
            return Player.query();
          }]
        }
      })
    }]);
