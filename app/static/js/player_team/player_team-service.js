'use strict';

angular.module('inforugby')
  .factory('Player_team', ['$resource', function ($resource) {
    return $resource('inforugby/player_teams/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
