'use strict';

angular.module('inforugby')
  .factory('Event', ['$resource', function ($resource) {
    return $resource('inforugby/events/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
