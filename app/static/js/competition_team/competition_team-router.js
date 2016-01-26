'use strict';

angular.module('inforugby')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/competition_teams', {
        templateUrl: 'views/competition_team/competition_teams.html',
        controller: 'Competition_teamController',
        resolve:{
          resolvedCompetition_team: ['Competition_team', function (Competition_team) {
            return Competition_team.query();
          }]
        }
      })
    }]);
