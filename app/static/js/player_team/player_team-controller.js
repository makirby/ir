'use strict';

angular.module('inforugby')
  .controller('Player_teamController', ['$scope', '$modal', 'resolvedPlayer_team', 'Player_team',
    function ($scope, $modal, resolvedPlayer_team, Player_team) {

      $scope.player_teams = resolvedPlayer_team;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.player_team = Player_team.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Player_team.delete({id: id},
          function () {
            $scope.player_teams = Player_team.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Player_team.update({id: id}, $scope.player_team,
            function () {
              $scope.player_teams = Player_team.query();
              $scope.clear();
            });
        } else {
          Player_team.save($scope.player_team,
            function () {
              $scope.player_teams = Player_team.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.player_team = {
          
          "player_id": "",
          
          "team_id": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var player_teamSave = $modal.open({
          templateUrl: 'player_team-save.html',
          controller: 'Player_teamSaveController',
          resolve: {
            player_team: function () {
              return $scope.player_team;
            }
          }
        });

        player_teamSave.result.then(function (entity) {
          $scope.player_team = entity;
          $scope.save(id);
        });
      };
    }])
  .controller('Player_teamSaveController', ['$scope', '$modalInstance', 'player_team',
    function ($scope, $modalInstance, player_team) {
      $scope.player_team = player_team;

      

      $scope.ok = function () {
        $modalInstance.close($scope.player_team);
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    }]);
