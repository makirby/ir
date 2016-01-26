'use strict';

angular.module('inforugby')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/events', {
        templateUrl: 'views/event/events.html',
        controller: 'EventController',
        resolve:{
          resolvedEvent: ['Event', function (Event) {
            return Event.query();
          }]
        }
      })
    }]);
