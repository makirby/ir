'use strict';

angular.module('inforugby')
  .factory('Match', ['$resource', function ($resource) {
    return $resource('inforugby/matches/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
