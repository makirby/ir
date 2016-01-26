'use strict';

angular.module('inforugby')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/teams', {
        templateUrl: 'views/team/teams.html',
        controller: 'TeamController',
        resolve:{
          resolvedTeam: ['Team', function (Team) {
            return Team.query();
          }]
        }
      })
    }]);
