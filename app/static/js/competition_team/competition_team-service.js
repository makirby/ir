'use strict';

angular.module('inforugby')
  .factory('Competition_team', ['$resource', function ($resource) {
    return $resource('inforugby/competition_teams/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
