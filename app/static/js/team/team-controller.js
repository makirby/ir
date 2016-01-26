'use strict';

angular.module('inforugby')
  .controller('TeamController', ['$scope', '$modal', 'resolvedTeam', 'Team',
    function ($scope, $modal, resolvedTeam, Team) {

      $scope.teams = resolvedTeam;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.team = Team.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Team.delete({id: id},
          function () {
            $scope.teams = Team.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Team.update({id: id}, $scope.team,
            function () {
              $scope.teams = Team.query();
              $scope.clear();
            });
        } else {
          Team.save($scope.team,
            function () {
              $scope.teams = Team.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.team = {
          
          "name": "",
          
          "img_location": "",
          
          "icon_location": "",
          
          "team_text": "",
          
          "ground_id": "",
          
          "team_type": "",
          
          "established": "",
          
          "season_id": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var teamSave = $modal.open({
          templateUrl: 'team-save.html',
          controller: 'TeamSaveController',
          resolve: {
            team: function () {
              return $scope.team;
            }
          }
        });

        teamSave.result.then(function (entity) {
          $scope.team = entity;
          $scope.save(id);
        });
      };
    }])
  .controller('TeamSaveController', ['$scope', '$modalInstance', 'team',
    function ($scope, $modalInstance, team) {
      $scope.team = team;

      
      $scope.establishedDateOptions = {
        dateFormat: 'yy-mm-dd',
        
        
      };

      $scope.ok = function () {
        $modalInstance.close($scope.team);
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    }]);
