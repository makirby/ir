'use strict';

angular.module('inforugby')
  .factory('Competition', ['$resource', function ($resource) {
    return $resource('inforugby/competitions/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
