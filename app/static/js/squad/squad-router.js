'use strict';

angular.module('inforugby')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/squads', {
        templateUrl: 'views/squad/squads.html',
        controller: 'SquadController',
        resolve:{
          resolvedSquad: ['Squad', function (Squad) {
            return Squad.query();
          }]
        }
      })
    }]);
