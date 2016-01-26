'use strict';

angular.module('inforugby')
  .controller('CompetitionController', ['$scope', '$modal', 'resolvedCompetition', 'Competition',
    function ($scope, $modal, resolvedCompetition, Competition) {

      $scope.competitions = resolvedCompetition;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.competition = Competition.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Competition.delete({id: id},
          function () {
            $scope.competitions = Competition.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Competition.update({id: id}, $scope.competition,
            function () {
              $scope.competitions = Competition.query();
              $scope.clear();
            });
        } else {
          Competition.save($scope.competition,
            function () {
              $scope.competitions = Competition.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.competition = {
          
          "name": "",
          
          "competition_text": "",
          
          "img_location": "",
          
          "icon_location": "",
          
          "competition_type": "",
          
          "created": "",
          
          "user_created": "",
          
          "season_id": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var competitionSave = $modal.open({
          templateUrl: 'competition-save.html',
          controller: 'CompetitionSaveController',
          resolve: {
            competition: function () {
              return $scope.competition;
            }
          }
        });

        competitionSave.result.then(function (entity) {
          $scope.competition = entity;
          $scope.save(id);
        });
      };
    }])
  .controller('CompetitionSaveController', ['$scope', '$modalInstance', 'competition',
    function ($scope, $modalInstance, competition) {
      $scope.competition = competition;

      
      $scope.createdDateOptions = {
        dateFormat: 'yy-mm-dd',
        
        
      };

      $scope.ok = function () {
        $modalInstance.close($scope.competition);
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    }]);
