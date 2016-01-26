'use strict';

angular.module('inforugby')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/player_teams', {
        templateUrl: 'views/player_team/player_teams.html',
        controller: 'Player_teamController',
        resolve:{
          resolvedPlayer_team: ['Player_team', function (Player_team) {
            return Player_team.query();
          }]
        }
      })
    }]);
