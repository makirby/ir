'use strict';

angular.module('inforugby')
  .factory('Squad', ['$resource', function ($resource) {
    return $resource('inforugby/squads/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
