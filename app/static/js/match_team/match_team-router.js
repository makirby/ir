'use strict';

angular.module('inforugby')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/match_teams', {
        templateUrl: 'views/match_team/match_teams.html',
        controller: 'Match_teamController',
        resolve:{
          resolvedMatch_team: ['Match_team', function (Match_team) {
            return Match_team.query();
          }]
        }
      })
    }]);
