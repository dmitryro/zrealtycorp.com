/**
 * ZRealty Corp 2014
 * All rights reserved. 
 */

/**
 * Dashboard Controller - we use it for user operations
 */

function DashboardCtrl($scope,$http) {
    $scope.toggleheader = true;
    $scope.togglenotfound = false;
    $scope.memberprofile = false;
    $scope.memberpanel = true; 
 
    $scope.postToBlog = function(user) {
        $scope.posttoblog = true;
        $scope.memberprofile = false;
        $scope.posttoproperties = false;
        $scope.privatemessage = false;  
        $scope.posttodiary = false;
        $scope.memberpanel = false;
    };

    $scope.editProfile = function(user) {
        $scope.posttoblog = false;
        $scope.memberprofile = true;
        $scope.posttoproperties = false;
        $scope.privatemessage = false;
        $scope.posttodiary = false;
        $scope.memberpanel = false;
    };
    
    $scope.postToProperties = function(user) {
        $scope.posttoblog = false;
        $scope.memberprofile = false;
        $scope.posttoproperties = true;
        $scope.privatemessage = false;
        $scope.posttodiary = false;
        $scope.memberpanel = false;
    };

    $scope.sendPrivateMessage = function(user) {
        $scope.posttoblog = false;
        $scope.memberprofile = false;
        $scope.posttoproperties = false;
        $scope.privatemessage = true;
        $scope.posttodiary = false;
        $scope.memberpanel = false; 
    };

   
    $scope.writeNoteToDiary = function(user) {
        $scope.posttoblog = false;
        $scope.memberprofile = false;
        $scope.posttoproperties = false;
        $scope.privatemessage = false;
        $scope.posttodiary = true;
        $scope.memberpanel = false;
    };


}

function AuthCtrl($scope,$http) {
    $scope.toggleheader = true;
    $scope.togglenotfound = false;

    $scope.loginMember = function(login) {

        if  (login.password==undefined || login.username==undefined) {
            $scope.authenticated = false;
            $scope.unauthenticated = true;
        }
        else {
                var url = 'http://zrealtycorp.com/rest/login/';
                
                 var values = 'username='+login.username+'&password='+login.password;
	        $http({
        	     method: 'POST',
          	     url: url,
        	     data: values,
        	     headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    	        }).success(function(data) {
                     $scope.authenticated = true;
                     $scope.unauthenticated = false;
                     window.location='http://zrealtycorp.com/dashboard/';
                }).error(function(data) {
                     $scope.authenticated = false;
                     $scope.unauthenticated = true;
                });

        } 
 
    };

    /**
     * Register a new member
     */
    $scope.registerMember = function(member) {

        $scope.registered = false;
        $scope.unregistered = false;
        $scope.nonequalpass = false;
        $scope.valid = true;
        $scope.duplicate = false;

        if  (member.username==undefined) {
            $scope.unregistered = true;
            $scope.valid = false;
        }
        
        if  (member.password==undefined)  {
            $scope.unregistered = true;
            $scope.valid = false;
        }

        if  (member.confirm_password==undefined)  {
            $scope.unregistered = true;
            $scope.valid = false;
        }


        if  (member.email==undefined)  {
            $scope.unregistered = true;
            $scope.valid = false;
        }

        if  (member.confirm_password!=member.password)  {
            $scope.unregistered = false;
            $scope.nonequalpass = true;
            $scope.valid = false;
        }
  
        else {
            var users_url = 'http://zrealtycorp.com/profiles';
            $http.get(users_url).
               error(function(data) {
                  $scope.usenrmame = undefined;
                  $scope.duplicate = false;
                  $scope.valid = false;
                  $scope.unregistered = false;
               }).
               success(function(data) {
                  profiles = data.results;
                  angular.forEach(profiles, function (profile) {
                         if  (member.username==profile.username)   {
                             $scope.unregistered = false;
                             $scope.duplicate = true;
                             $scope.valid = false;
                         }
                  });
               });

             
        }

        if($scope.valid == true) {
                var url = 'http://zrealtycorp.com/accounts_api/register/';
                var nurl = 'http://zrealtycorp.com/notifynew/';
                var values = 'username='+member.username+'&password='+member.password+'&email='+member.email;
                var activate_url = 'http://zrealtycorp.com/activatenew?'+values;

                $http({ // The actual registration happens here
                     method: 'POST',
                     url: url,
                     data: values,
                     headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                }).success(function(data) {
                     $scope.registered = true;
                     $scope.duplicate = false;
                     $scope.unregistered = false;
                }).error(function(data) {
                     $scope.registered = false;
                     $scope.duplicate = false;
                     $scope.unregistered = true;
                });

                $http.get(activate_url).success(function(data) {
                }).error(function(data) {
                });

        }
    };

    $scope.logoutMember = function() {
    };
}

function ContactCtrl($scope,$http) {
     $scope.contactvalid=false; 
     $scope.toggle = false;
     $scope.gridsterOpts = {
        columns: 6, // the width of the grid, in columns
        pushing: true, // whether to push other items out of the way on move or resize
        floating: true, // whether to automatically float items up so they stack (you can temporarily disable if you are adding unsorted items with ng-repeat)
        width: 'auto', // can be an integer or 'auto'. 'auto' scales gridster to be the full width of its containing element
        colWidth: 'auto', // can be an integer or 'auto'.  'auto' uses the pixel width of the element divided by 'columns'
        rowHeight: 'match', // can be an integer or 'match'.  Match uses the colWidth, giving you square widgets.
        margins: [10, 10], // the pixel distance between each widget
        outerMargin: true, // whether margins apply to outer edges of the grid
        isMobile: false, // stacks the grid items if true
        mobileBreakPoint: 600, // if the screen is not wider that this, remove the grid layout and stack the items
        mobileModeEnabled: true, // whether or not to toggle mobile mode when screen width is less than mobileBreakPoint
        minColumns: 1, // the minimum columns the grid must have
        minRows: 2, // the minimum height of the grid, in rows
        maxRows: 100,
        defaultSizeX: 2, // the default width of a gridster item, if not specifed
        defaultSizeY: 1, // the default height of a gridster item, if not specified
        resizable: {
           enabled: true,
           handles: 'n, e, s, w, ne, se, sw, nw',
           start: function(event, uiWidget, $element) {}, // optional callback fired when resize is started,
           resize: function(event, uiWidget, $element) {}, // optional callback fired when item is resized,
           stop: function(event, uiWidget, $element) {} // optional callback fired when item is finished resizing
        },
        draggable: {
           enabled: true, // whether dragging items is supported
           handle: '.contact-form', // optional selector for resize handle
           start: function(event, uiWidget, $element) {}, // optional callback fired when drag is started,
           drag: function(event, uiWidget, $element) {}, // optional callback fired when item is moved,
           stop: function(event, uiWidget, $element) {} // optional callback fired when item is finished dragging
        }
      };

      $scope.$on('gridster-resized', function(newSizes){
         var newWidth = sizes[0];
         var newHeight = sizes[1];
      });

      $scope.data = {success:false, show: true};

      $scope.getObjectAsText = function () {
             $scope.inquiry.message = JSON.stringify($scope.containerObject);
      };

      $scope.reset = function() {
           alert('changing');
      };
      $scope.submitInquiry = function(inquiry) {
         $scope.data = {show: true};   
         $http.get('http://zrealtycorp.com/post?id='+inquiry.property_id+
                   "&name="+inquiry.name+"&email="+inquiry.email+
                   "&phone="+inquiry.phone+
                   "&message="+inquiry.message+"&title="+inquiry.title).
            error(function(data) {
                $scope.data = {success:false,show: true, mustclean: false};
               alert('error:'+data);
            }).
            success(function(data) {
               $scope.data = {success: true, show: false, mustclean: false};
          
               $scope.greeting = data;
         });

      }

      $scope.sendMessage = function() {
         $scope.data = {show: true};
          $scope.invalid=false;

          if($scope.subject==undefined){
              $scope.invalid=true;
              $scope.sent=false;
          }

          if($scope.name==undefined || $scope.name.length<=0){
              $scope.invalid=true;
              $scope.sent=false;
          }

          if($scope.name==undefined || $scope.name.length<=0){
              $scope.invalid=true;
              $scope.sent=false;
          }

          if($scope.message==undefined || $scope.message.length<=0){
              $scope.invalid=true;
              scope.sent=false;
          }

          if($scope.email==undefined || $scope.email.length<=0){
              $scope.invalid=true;
              $scope.sent=false;
          }

          if  (!$scope.invalid) {
              $http.get('http://zrealtycorp.com/contactus?subject='+$scope.subject+
                       "&name="+$scope.name+"&email="+$scope.email+"&phone="+$scope.phone+
                       "&message="+$scope.message).
               error(function(data) {
                    $scope.sent=false;
                    $scope.data = {success:false,show: true, mustclean: false};
                    alert('error:'+data);
               }).
               success(function(data) {
                    $scope.contactvalid=true;
                    $scope.data = {success: true, show: false, mustclean: false};
                    $scope.subject=undefined;
                    $scope.name=undefined;
                    $scope.message=undefined; 
                    $scope.email=undefined;
                    $scope.sent=true;
                    $scope.invalid=false;
                    $scope.greeting = data;
              });
         }

      }


      $scope.fetchSimilar = function() {
         $scope.items = [];
      }


      $scope.cleanForm = function(inquiry) {
           scope.data = {success:true, show: false, mustclean: true};
      }

      $scope.openContact = function() {
           scope.data = {success:false, show: true, mustclean: true};
      }
}

/**
 * Search the property
 */


function SearchCtrl($scope,$http) {

    $scope.itemsPerPage = 10;
    $scope.currentPage = 0;
    $scope.toggle = false;
    $scope.sent = false;
    $scope.displayPets = function(property) {
             if  (property.pets==true) {
                              $scope.property.pets=true;
                              $scope.property.petsallowed = 'Yes';
             }
             if  (property.pets==false) {
                              $scope.property.pets=false;
                              $scope.property.petsallowed = 'No';
             }


    }
    

    $scope.searchProperty = function() {
    //     alert(property.type);
         $scope.items = [];
         var rooms = $scope.rooms;
         var type = $scope.type;
         var category = $scope.category;
         var borough = $scope.borough;
         var neighborhood = $scope.neighborhood;         
         var pets_allowed = $scope.pets_allowed; 
         var min_price = $scope.min_price;
         var max_price = $scope.max_price;
          

         var url = 'http://zrealtycorp.com/properties/';
         var rooms_url = 'http://zrealtycorp.com/rooms/'+rooms+'/';
         var type_url = 'http://zrealtycorp.com/types/'+type+'/';
         var category_url = 'http://zrealtycorp.com/categories/'+category+'/';
         var borough_url = 'http://zrealtycorp.com/boroughs/'+borough+'/';
         var neighborhood_url = 'http://zrealtycorp.com/neighborhoods/'+neighborhood+'/';
         
         // A helper container object
         function Property(rooms,type,category,borough,neighborhood,pets_allowed,min_price,max_price) {
                 this.rooms = rooms;
                 this.type = type;
                 this.category  = category;
                 this.borough = borough;
                 this.neighborhood = neighborhood;
                 this.pets = pets_allowed;
                 this.min_price = min_price;
                 this.max_price = max_price;
         }

         Property.prototype.rooms = function() {
             return this.rooms;                        
         }

         Property.prototype.type = function() {
             return this.type;
         }

         Property.prototype.category = function() {
             return this.category;
         }

         Property.prototype.borough = function() {
             return this.borough;
         }

         Property.prototype.neighborhood = function() {
             return this.neighborhood;
         }

         Property.prototype.pets = function() {
             return this.pets;
         }

         Property.prototype.min_price = function() {
             return this.min_price;
         }

         Property.prototype.max_price = function() {
             return this.max_price;
         }


         if  ($scope.category!=undefined) {
            $http.get(category_url).
               error(function(data) {
                  $scope.category_name = undefined;
               }).
               success(function(data) {
                  categories = data.results;
                  angular.forEach(categories, function (cat) {
                         if  (category==cat.id)   {
                             $scope.category_name = cat.category;
                         }
                  });
               });

          }  else {
             $scope.category_name = undefined;
          }
  

         if  ($scope.rooms!=undefined) {

             $http.get(rooms_url).
                error(function(data) {
                $scope.rooms_name = undefined;   
             }).
             success(function(data) {
                  rooms = data.results;
                  $scope.rooms_name = data.rooms;
             });

          } else {
             $scope.rooms_name = undefined; 
          }


         if  ($scope.borough!=undefined) {

            $http.get(borough_url).
               error(function(data) {
                   $scope.borough_name = undefined;
               }).
              success(function(data) {
                  boroughs = data.results;
                  $scope.borough_name = data.borough;

            });

         } else {
            $scope.borough_name = undefined;
         }

         if  ($scope.neighborhood!=undefined) {

            $http.get(neighborhood_url).
               error(function(data) {
                   $scope.neighborhood_name =  undefined;
               }).
               success(function(data) {

                   $scope.neighborhood_name =  data.neighborhood;
               });
         }  else {
              $scope.neighborhood_name = undefined;
         }

         if  ($scope.type!=undefined) {
             $http.get(type_url).
             error(function(data) {
                $scope.type_name = undefined;
             }).
             success(function(data) {
                    $scope.type_name=data.type;
             });
         } 
         else {
              $scope.type_name = undefined;
         }

           /**
            * A helper object to keep the searched datat
            */
         var prop = new Property($scope.rooms_name,
                                   $scope.type_name,
                                   $scope.category_name,
                                   $scope.borough_name,
                                   $scope.neighborhood_name,
                                   pets_allowed,
                                   min_price,
                                   max_price);

         $http.get(url).
            error(function(data) {
         }).
         success(function(data) {  // We got some items - lets process them
            $scope.properties = data;
              //  alert($scope.properties.results[0].property_id);
            angular.forEach($scope.properties.results, function (property) {
                        if  (property.rooms==$scope.rooms_name) {
                            if  (property.type == $scope.type_name)  {
                                 if  (property.category == $scope.category_name)  {
                                      if  (property.borough == $scope.borough_name)  {
                                             if  (property.neighborhood == $scope.neighborhood_name) {
                                                 if  (property.pets_allowed==true)  {
                                                        property.pets_allowed='Yes';
                                                 }
                                                 else  {
                                                        property.pets_allowed='No';
                                                 }
                                                 $scope.items.push(property);
                                             }
                                      }
                                 }
                             }  
                        }  
                       if  ($scope.items.length>10) {
                            $scope.toggle=true;
                       }
                       else {
                            $scope.toggle=false;
                       }
                       if ($scope.items.length==0) {
                            $scope.toggleheader = false;
                            $scope.togglenotfound = true;
                       }
                       else {
                            $scope.toggleheader = true;
                            $scope.togglenotfound = false;
                       }

                }, $scope.items);
                if(!all_set(prop) &&  all_empty(prop,1)) {
                    angular.forEach($scope.properties.results, function (property) {
 
                        if  (property.pets_allowed)  {
                          property.pets_allowed='Yes';
                        }
                        else  {
                              property.pets_allowed='No';
                        }
                        if  (property.rooms==$scope.rooms_name) {
                                                 $scope.items.push(property);
                        }
                       if  ($scope.items.length>10) {
                            $scope.toggle=true;
                       }
                       else {
                            $scope.toggle=false;
                       }
                       if ($scope.items.length==0) {
                            $scope.toggleheader = false;
                            $scope.togglenotfound = true;
                       }
                       else {
                            $scope.toggleheader = true;
                            $scope.togglenotfound = false;
                       }

                    }, $scope.items);

                }
                else
                if(!all_set(prop) &&  all_empty(prop,2)) {
                    angular.forEach($scope.properties.results, function (property) {

                        if  (property.pets_allowed)  {
                          property.pets_allowed='Yes';
                        }
                        else  {
                              property.pets_allowed='No';
                        }
                        if  (property.type==$scope.type_name) {
                                                 $scope.items.push(property);
                        }
                       if  ($scope.items.length>10) {
                            $scope.toggle=true;
                       }
                       else {
                            $scope.toggle=false;
                       }
                       if ($scope.items.length==0) {
                            $scope.toggleheader = false;
                            $scope.togglenotfound = true;
                       }
                       else {
                            $scope.toggleheader = true;
                            $scope.togglenotfound = false;
                       }

                    }, $scope.items);

                }
                else 
                if(!all_set(prop) && $scope.category_name!=undefined) {
                             if($scope.neighborhood_name!=undefined) {
                                    angular.forEach($scope.properties.results, function (property) {

                                        if  (property.pets_allowed)  {
                                          property.pets_allowed='Yes';
                                        }
                                        else  {
                                          property.pets_allowed='No';
                                        }
                                        if  (property.category==$scope.category_name && 
                                             property.neighborhood==$scope.neighborhood_name) {
                                                 $scope.items.push(property);
                                        }
                                        if  ($scope.items.length>10) {
                                           $scope.toggle=true;
                                        }
                                        else {
                                           $scope.toggle=false;
                                        }
                                        if ($scope.items.length==0) {
                                             $scope.toggleheader = false;
                                             $scope.togglenotfound = true;
                                        }
                                        else {
                                            $scope.toggleheader = true;
                                            $scope.togglenotfound = false;
                                       }
                                      }, $scope.items);

                             } else
                             if($scope.borough_name!=undefined) {
                                    angular.forEach($scope.properties.results, function (property) {

                                        if  (property.pets_allowed)  {
                                          property.pets_allowed='Yes';
                                        }
                                        else  {
                                          property.pets_allowed='No';
                                        }
                                        if  (property.category==$scope.category_name && 
                                             property.borough==$scope.borough_name) {
                                                 $scope.items.push(property);
                                        }
                                        if  ($scope.items.length>10) {
                                           $scope.toggle=true;
                                        }
                                        else {
                                           $scope.toggle=false;
                                        }
                                        if ($scope.items.length==0) {
                                             $scope.toggleheader = false;
                                             $scope.togglenotfound = true;
                                        }
                                        else {
                                            $scope.toggleheader = true;
                                            $scope.togglenotfound = false;
                                       }
                                      }, $scope.items);

                             } else 
                             if($scope.pets_allowed!=undefined) {
                                    angular.forEach($scope.properties.results, function (property) {

                                        if  (property.category==$scope.category_name && 
                                             property.pets_allowed==$scope.pets_allowed) {
                                                 if  (property.pets_allowed)  {
                                                        property.pets_allowed='Yes';
                                                 }
                                                 else  {
                                                        property.pets_allowed='No';
                                                 }
                                                 $scope.items.push(property);
                                        }
                                        if  ($scope.items.length>10) {
                                           $scope.toggle=true;
                                        }
                                        else {
                                           $scope.toggle=false;
                                        }
                                        if ($scope.items.length==0) {
                                             $scope.toggleheader = false;
                                             $scope.togglenotfound = true;
                                        }
                                        else {
                                            $scope.toggleheader = true;
                                            $scope.togglenotfound = false;
                                       }
                                      }, $scope.items);

                             }

                }      
                
                else
                if  (!all_set(prop) && $scope.type_name!=undefined) {
                             if($scope.neighborhood_name!=undefined) {
                                    angular.forEach($scope.properties.results, function (property) {

                                        if  (property.pets_allowed)  {
                                          property.pets_allowed='Yes';
                                        }
                                        else  {
                                          property.pets_allowed='No';
                                        }
                                        if  (property.type==$scope.type_name && property.neighborhood==$scope.neighborhood_name) {
                                                 $scope.items.push(property);
                                        }
                                        if  ($scope.items.length>10) {
                                           $scope.toggle=true;
                                        }
                                        else {
                                           $scope.toggle=false;
                                        }
                                        if ($scope.items.length==0) {
                                             $scope.toggleheader = false;
                                             $scope.togglenotfound = true;
                                        }
                                        else {
                                            $scope.toggleheader = true;
                                            $scope.togglenotfound = false;
                                       }
                                      }, $scope.items);

                             } else
                             if($scope.borough_name!=undefined) {
                                    angular.forEach($scope.properties.results, function (property) {

                                        if  (property.pets_allowed)  {
                                          property.pets_allowed='Yes';
                                        }
                                        else  {
                                          property.pets_allowed='No';
                                        }
                                        if  (property.type==$scope.type_name && property.borough==$scope.borough_name) {
                                                 $scope.items.push(property);
                                        }
                                        if  ($scope.items.length>10) {
                                           $scope.toggle=true;
                                        }
                                        else {
                                           $scope.toggle=false;
                                        }
                                        if ($scope.items.length==0) {
                                             $scope.toggleheader = false;
                                             $scope.togglenotfound = true;
                                        }
                                        else {
                                            $scope.toggleheader = true;
                                            $scope.togglenotfound = false;
                                       }
                                      }, $scope.items);

                             } else
                             if($scope.pets_allowed!=undefined) {
                                    angular.forEach($scope.properties.results, function (property) {

                                        if  (property.type==$scope.type_name && 
                                             property.pets_allowed==$scope.pets_allowed) {
                                                 if  (property.pets_allowed)  {
                                                        property.pets_allowed='Yes';
                                                 }
                                                 else  {
                                                        property.pets_allowed='No';
                                                 }
                                                 $scope.items.push(property);
                                        }
                                        if  ($scope.items.length>10) {
                                           $scope.toggle=true;
                                        }
                                        else {
                                           $scope.toggle=false;
                                        }
                                        if ($scope.items.length==0) {
                                             $scope.toggleheader = false;
                                             $scope.togglenotfound = true;
                                        }
                                        else {
                                            $scope.toggleheader = true;
                                            $scope.togglenotfound = false;
                                       }
                                      }, $scope.items);

                             }

                }
                if(!all_set(prop) &&  all_empty(prop,3)) {
                   
                    angular.forEach($scope.properties.results, function (property) {

                        if  (property.pets_allowed)  {
                          property.pets_allowed='Yes';
                        }
                        else  {
                              property.pets_allowed='No';
                        }
                        if  (property.category==$scope.category_name) {
                                                 $scope.items.push(property);
                        }
                       if  ($scope.items.length>10) {
                            $scope.toggle=true;
                       }
                       else {
                            $scope.toggle=false;
                       }
                       if ($scope.items.length==0) {
                            $scope.toggleheader = false;
                            $scope.togglenotfound = true;
                       }
                       else {
                            $scope.toggleheader = true;
                            $scope.togglenotfound = false;
                       }
                    }, $scope.items);

                }

                if(!all_set(prop) &&  all_empty(prop,4)) {

                    angular.forEach($scope.properties.results, function (property) {

                        if  (property.pets_allowed)  {
                          property.pets_allowed='Yes';
                        }
                        else  {
                              property.pets_allowed='No';
                        }
                        if  (property.borough==$scope.borough_name) {
                                                 $scope.items.push(property);
                        }

                       if  ($scope.items.length>10) {
                            $scope.toggle=true;
                       }
                       else {
                            $scope.toggle=false;
                       }
                       if ($scope.items.length==0) {
                            $scope.toggleheader = false;
                            $scope.togglenotfound = true;
                       }
                       else {
                            $scope.toggleheader = true;
                            $scope.togglenotfound = false;
                       }

                    }, $scope.items);

                }
                if(!all_set(prop) &&  all_empty(prop,5)) {
                    angular.forEach($scope.properties.results, function (property) {
                        if  (property.pets_allowed)  {
                          property.pets_allowed='Yes';
                        }
                        else  {
                              property.pets_allowed='No';
                        }
                        if  (property.borough==$scope.borough_name) {
                                                 $scope.items.push(property);
                        }

                       if  ($scope.items.length>10) {
                            $scope.toggle=true;
                       }
                       else {
                            $scope.toggle=false;
                       }
                       if ($scope.items.length==0) {
                            $scope.toggleheader = false;
                            $scope.togglenotfound = true;
                       }
                       else {
                            $scope.toggleheader = true;
                            $scope.togglenotfound = false;
                       }
                    }, $scope.items);

                }


                if(!all_set(prop) && ($scope.borough_name!=undefined && $scope.neighborhood_name!=undefined)) {
                   angular.forEach($scope.properties.results, function (property) {
                        if  (property.pets_allowed)  {
                          property.pets_allowed='Yes';
                        }
                        else  {
                              property.pets_allowed='No';
                        }
                        if  (property.borough == $scope.borough_name)  {
                             if  (property.neighborhood == $scope.neighborhood_name) {
                                    $scope.items.push(property);
                             }
                        }


                       if  ($scope.items.length>10) {
                            $scope.toggle=true;
                       }
                       else {
                            $scope.toggle=false;
                       }
                       if ($scope.items.length==0) {
                            $scope.toggleheader = false;
                            $scope.togglenotfound = true;
                       }
                       else {
                            $scope.toggleheader = true;
                            $scope.togglenotfound = false;
                       }


                   }, $scope.items);


                }
                if(!all_set(prop) &&  all_empty(prop,6)) {
                    angular.forEach($scope.properties.results, function (property) {
                       if  (!property.pets_allowed && !$scope.prop.pets) {
                              property.pets_allowed='No';
                              $scope.items.push(property);
                       }
                       else if (property.pets_allowed && $scope.prop.pets) {
                              property.pets_allowed='Yes';
                              $scope.items.push(propertddy);
                       }

                       if  ($scope.items.length>10) {
                            $scope.toggle=true;
                       }
                       else {
                            $scope.toggle=false;
                       }
                       if ($scope.items.length==0) {
                            $scope.toggleheader = false;
                            $scope.togglenotfound = true;
                       }
                       else {
                            $scope.toggleheader = true;
                            $scope.togglenotfound = false;
                       }
                    }, $scope.items);
                }
 
                var in_data = { rooms: $scope.items[0].type };
                $scope.in_data = in_data;


            });
    }
  // pagination - decreasse the page
  $scope.prevPage = function() {
    if ($scope.currentPage > 0) {
      $scope.currentPage--;
    }
  };

  $scope.prevPageDisabled = function() {
    return $scope.currentPage === 0 ? "disabled" : "";
  };

  $scope.pageCount = function() {
    return Math.ceil($scope.items.length/$scope.itemsPerPage)-1;
  };

  $scope.nextPage = function() {
    if ($scope.currentPage < $scope.pageCount()) {
      $scope.currentPage++;
    }
  };

  $scope.nextPageDisabled = function() {
    return $scope.currentPage === $scope.pageCount() ? "disabled" : "";
  };


}

 // Helper function to check if all the filtering fields have been set
function all_set(obj) {
        if  (obj.rooms==undefined) return false;
        if  (obj.category==undefined) return false;
        if  (obj.type==undefined) return false;
        if  (obj.borough==undefined) return false;
        if  (obj.neighborhood==undefined) return false;
       // if  (obj.pets==undefined) return false;
        return true;
}

 // Helper function to check if all the filtering fields are empty
function all_empty(obj,val) {
    if (val==1) {
        if  (obj.category!=undefined && obj.category.length>0) return false;
        if  (obj.type!=undefined && obj.type.length>0) return false;
        if  (obj.borough!=undefined && obj.borough.length>0) return false;
        if  (obj.neighborhood!=undefined && obj.neighborhood.length>0) return false;
        if  (obj.pets!=undefined && obj.pets==true) return false; 
        return true;
    }
    else 
    if (val==2) {
        if  (obj.rooms!=undefined && obj.rooms.length>0) return false;
        if  (obj.category!=undefined &&  obj.category.length>0) return false;
        if  (obj.borough!=undefined && obj.borough.length>0) return false;
        if  (obj.neighborhood!=undefined && obj.neighborhood.length>0) return false;
        if  (obj.pets!=undefined && obj.pets==true) return false;
        return true;
    }
    else
    if (val==3) {
        if  (obj.rooms!=undefined && obj.rooms.length>0) return false;
        if  (obj.type!=undefined && obj.type.length>0) return false;
        if  (obj.borough!=undefined && obj.borough.length>0) return false;
        if  (obj.neighborhood!=undefined && obj.neighborhood.length>0) return false;
        if  (obj.pets!=undefined && obj.pets==true) return false;
        return true;
    }
    else
    if (val==4) {
        if  (obj.category!=undefined && obj.category.length>0) return false;
        if  (obj.type!=undefined && obj.type.length>0) return false;
        if  (obj.rooms!=undefined && obj.rooms.length>0) return false;
        if  (obj.neighborhood!=undefined && obj.neighborhood.length>0) return false;
        if  (obj.pets!=undefined && obj.pets==true) return false;
        return true;
    }
    else
    if (val==5) {
        if  (obj.category!=undefined && obj.category.length>0) return false;
        if  (obj.type!=undefined && obj.type.length>0) return false;
        if  (obj.borough!=undefined && obj.borough.length>0) return false;
        if  (obj.rooms!=undefined && obj.rooms.length>0) return false;
        if  (obj.pets!=undefined && obj.pets==true) return false;
        return true;
    }
    else
    if (val==6) {
        if  (obj.category!=undefined && obj.category.length>0) return false;
        if  (obj.type!=undefined && obj.type.length>0) return false;
        if  (obj.borough!=undefined && obj.borough.length>0) return false;
        if  (obj.neighborhood!=undefined && obj.neighborhood.length>0) return false;
        if  (obj.rooms!=undefined && obj.rooms.length>0) return false;
        return true;
    }




    return false;
}

/**
 * Stub for column sort
 */


function SortCtrl($scope) {
   $scope.sortColumn = function(column) {
           alert(columnt);
           if(column== 1) { alert('ID');}
           if(column== 2) { alert('Property');}
           if(column== 3) { alert('Type');}
           if(column== 4) { alert('Rooms');}
           if(column== 5) { alert('Baths');}
           if(column== 6) { alert('Size');}
           if(column== 7) { alert('Offer');}
           if(column== 8) { alert('Price');}
           if(column== 9) { alert('Location');}
           if(column== 10) { alert('Pets');}
   };
}

