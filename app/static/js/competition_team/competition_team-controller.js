'use strict';

angular.module('inforugby')
  .controller('Competition_teamController', ['$scope', '$modal', 'resolvedCompetition_team', 'Competition_team',
    function ($scope, $modal, resolvedCompetition_team, Competition_team) {

      $scope.competition_teams = resolvedCompetition_team;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.competition_team = Competition_team.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Competition_team.delete({id: id},
          function () {
            $scope.competition_teams = Competition_team.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Competition_team.update({id: id}, $scope.competition_team,
            function () {
              $scope.competition_teams = Competition_team.query();
              $scope.clear();
            });
        } else {
          Competition_team.save($scope.competition_team,
            function () {
              $scope.competition_teams = Competition_team.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.competition_team = {
          
          "competition_id": "",
          
          "team_id": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var competition_teamSave = $modal.open({
          templateUrl: 'competition_team-save.html',
          controller: 'Competition_teamSaveController',
          resolve: {
            competition_team: function () {
              return $scope.competition_team;
            }
          }
        });

        competition_teamSave.result.then(function (entity) {
          $scope.competition_team = entity;
          $scope.save(id);
        });
      };
    }])
  .controller('Competition_teamSaveController', ['$scope', '$modalInstance', 'competition_team',
    function ($scope, $modalInstance, competition_team) {
      $scope.competition_team = competition_team;

      

      $scope.ok = function () {
        $modalInstance.close($scope.competition_team);
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    }]);
