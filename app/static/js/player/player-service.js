'use strict';

angular.module('inforugby')
  .factory('Player', ['$resource', function ($resource) {
    return $resource('inforugby/players/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
