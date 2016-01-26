'use strict';

angular.module('inforugby')
  .controller('MatchController', ['$scope', '$modal', 'resolvedMatch', 'Match',
    function ($scope, $modal, resolvedMatch, Match) {

      $scope.matches = resolvedMatch;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.match = Match.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Match.delete({id: id},
          function () {
            $scope.matches = Match.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Match.update({id: id}, $scope.match,
            function () {
              $scope.matches = Match.query();
              $scope.clear();
            });
        } else {
          Match.save($scope.match,
            function () {
              $scope.matches = Match.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.match = {
          
          "competition_id": "",
          
          "home_match_team_id": "",
          
          "away_match_team_id": "",
          
          "match_text": "",
          
          "ground_id": "",
          
          "home_score": "",
          
          "away_score": "",
          
          "img_location": "",
          
          "match_date": "",
          
          "match_outcome": "",
          
          "match_type": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var matchSave = $modal.open({
          templateUrl: 'match-save.html',
          controller: 'MatchSaveController',
          resolve: {
            match: function () {
              return $scope.match;
            }
          }
        });

        matchSave.result.then(function (entity) {
          $scope.match = entity;
          $scope.save(id);
        });
      };
    }])
  .controller('MatchSaveController', ['$scope', '$modalInstance', 'match',
    function ($scope, $modalInstance, match) {
      $scope.match = match;

      
      $scope.match_dateDateOptions = {
        dateFormat: 'yy-mm-dd',
        
        
      };

      $scope.ok = function () {
        $modalInstance.close($scope.match);
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    }]);
