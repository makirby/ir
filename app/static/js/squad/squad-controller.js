'use strict';

angular.module('inforugby')
  .controller('SquadController', ['$scope', '$modal', 'resolvedSquad', 'Squad',
    function ($scope, $modal, resolvedSquad, Squad) {

      $scope.squads = resolvedSquad;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.squad = Squad.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Squad.delete({id: id},
          function () {
            $scope.squads = Squad.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Squad.update({id: id}, $scope.squad,
            function () {
              $scope.squads = Squad.query();
              $scope.clear();
            });
        } else {
          Squad.save($scope.squad,
            function () {
              $scope.squads = Squad.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.squad = {
          
          "tighthead_id": "",
          
          "loosehead_id": "",
          
          "hooker_id": "",
          
          "lock_4_id": "",
          
          "lock_5_id": "",
          
          "flanker_6_id": "",
          
          "flanker_7_id": "",
          
          "number_8_id": "",
          
          "scrum_half_id": "",
          
          "fly_half_id": "",
          
          "wing_11_id": "",
          
          "inside_centre_id": "",
          
          "outside_centre_id": "",
          
          "wing_14_id": "",
          
          "full_back_id": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var squadSave = $modal.open({
          templateUrl: 'squad-save.html',
          controller: 'SquadSaveController',
          resolve: {
            squad: function () {
              return $scope.squad;
            }
          }
        });

        squadSave.result.then(function (entity) {
          $scope.squad = entity;
          $scope.save(id);
        });
      };
    }])
  .controller('SquadSaveController', ['$scope', '$modalInstance', 'squad',
    function ($scope, $modalInstance, squad) {
      $scope.squad = squad;

      

      $scope.ok = function () {
        $modalInstance.close($scope.squad);
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    }]);
