    function readCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for(var i=0;i < ca.length;i++) {
            var c = ca[i];
            while (c.charAt(0)==' ') c = c.substring(1,c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
        }
        return null;
    }
    var zrealty = angular.module('zrealty', ['ng.django.forms' ,'ngCookies',
                                             'djangoRESTResources','ngLoad',
                                             'angular-form-ui','ngRoute',
                                             'ngTouch','mobile-angular-ui',
                                             'angularUtils.directives.dirPagination',
                                             'ngMessages','angular-flash.service',
                                             'angular-flash.flash-alert-directive','ngTasty','restful']).

                          config(['$httpProvider','$interpolateProvider', function($httpProvider, $interpolateProvider) {
                                                                                   $interpolateProvider.startSymbol('{$');
                                                                                   $interpolateProvider.endSymbol('$}');
                                                                                   $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
                                                                                   $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
                          }]).
                          run(['$http',
                               '$cookies',
                               function($http, $cookies) {
                                     $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
                               }]);

                          zrealty.filter('offset', function() {
                               return function(input, start) {
                                   start = parseInt(start, 10);
                                   return input.slice(start);
                               };
     });

