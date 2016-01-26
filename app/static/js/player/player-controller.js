'use strict';

angular.module('inforugby')
  .controller('PlayerController', ['$scope', '$modal', 'resolvedPlayer', 'Player',
    function ($scope, $modal, resolvedPlayer, Player) {

      $scope.players = resolvedPlayer;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.player = Player.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Player.delete({id: id},
          function () {
            $scope.players = Player.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Player.update({id: id}, $scope.player,
            function () {
              $scope.players = Player.query();
              $scope.clear();
            });
        } else {
          Player.save($scope.player,
            function () {
              $scope.players = Player.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.player = {
          
          "name": "",
          
          "date_of_birth": "",
          
          "height": "",
          
          "weight": "",
          
          "player_text": "",
          
          "retired": "",
          
          "user_created": "",
          
          "image_location": "",
          
          "icon_location": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var playerSave = $modal.open({
          templateUrl: 'player-save.html',
          controller: 'PlayerSaveController',
          resolve: {
            player: function () {
              return $scope.player;
            }
          }
        });

        playerSave.result.then(function (entity) {
          $scope.player = entity;
          $scope.save(id);
        });
      };
    }])
  .controller('PlayerSaveController', ['$scope', '$modalInstance', 'player',
    function ($scope, $modalInstance, player) {
      $scope.player = player;

      
      $scope.date_of_birthDateOptions = {
        dateFormat: 'yy-mm-dd',
        
        
      };

      $scope.ok = function () {
        $modalInstance.close($scope.player);
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    }]);
