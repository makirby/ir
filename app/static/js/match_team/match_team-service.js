'use strict';

angular.module('inforugby')
  .factory('Match_team', ['$resource', function ($resource) {
    return $resource('inforugby/match_teams/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
