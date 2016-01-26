'use strict';

angular.module('inforugby')
  .factory('Team', ['$resource', function ($resource) {
    return $resource('inforugby/teams/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
