'use strict';

angular.module('inforugby')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/competitions', {
        templateUrl: 'views/competition/competitions.html',
        controller: 'CompetitionController',
        resolve:{
          resolvedCompetition: ['Competition', function (Competition) {
            return Competition.query();
          }]
        }
      })
    }]);
