'use strict';

angular.module('inforugby')
  .controller('Match_teamController', ['$scope', '$modal', 'resolvedMatch_team', 'Match_team',
    function ($scope, $modal, resolvedMatch_team, Match_team) {

      $scope.match_teams = resolvedMatch_team;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.match_team = Match_team.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Match_team.delete({id: id},
          function () {
            $scope.match_teams = Match_team.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Match_team.update({id: id}, $scope.match_team,
            function () {
              $scope.match_teams = Match_team.query();
              $scope.clear();
            });
        } else {
          Match_team.save($scope.match_team,
            function () {
              $scope.match_teams = Match_team.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.match_team = {
          
          "match_id": "",
          
          "team_id": "",
          
          "squad_id": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var match_teamSave = $modal.open({
          templateUrl: 'match_team-save.html',
          controller: 'Match_teamSaveController',
          resolve: {
            match_team: function () {
              return $scope.match_team;
            }
          }
        });

        match_teamSave.result.then(function (entity) {
          $scope.match_team = entity;
          $scope.save(id);
        });
      };
    }])
  .controller('Match_teamSaveController', ['$scope', '$modalInstance', 'match_team',
    function ($scope, $modalInstance, match_team) {
      $scope.match_team = match_team;

      

      $scope.ok = function () {
        $modalInstance.close($scope.match_team);
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    }]);
