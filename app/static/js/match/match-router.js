'use strict';

angular.module('inforugby')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/matches', {
        templateUrl: 'views/match/matches.html',
        controller: 'MatchController',
        resolve:{
          resolvedMatch: ['Match', function (Match) {
            return Match.query();
          }]
        }
      })
    }]);
