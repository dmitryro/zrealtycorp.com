function MessageCtrl($scope,$http) {

    $scope.sent = false;
    $scope.invalid = false;

    $scope.contacts = []; // contact list array

    // Helper object for contact
    function Contact(name,phone) {
       this.name = name;
       this.phone = phone;
    }

    Contact.prototype.name = function() {
       return this.name;
    }

    Contact.prototype.phone = function() {
       return this.phone;
    }

    // Delete a contact
    $scope.deleteContact = function(item) {

        // Delete the contact from the list of contacts
        $scope.contacts = $scope.contacts.filter(function(contact) {
              return contact!=item;
        });


        $scope.contact_message = "A contact was removed";
        $scope.validcontact=true;
        $scope.invalidcontact=false;

    }
    // Add a new contact
    $scope.addContact = function(contact) {

          if (contact==undefined)  {    // the object is empty
              $scope.validcontact=false;  // hide the success message
              $scope.invalidcontact=true;  // show the failure message
          }
          else if  (contact.name==undefined || contact.phone==undefined) {  // the name or the phone is empty
              $scope.validcontact=false; // hide the success message
              $scope.invalidcontact=true; // show the failure message
          }
          else if  (contact.name=='' || contact.phone=='') {  // not empty but has zero length phone or name
              $scope.validcontact=false; // hide the success message
              $scope.invalidcontact=true;  // show the failure message
          }
          else  {
              $scope.contacts.push(new Contact(contact.name, contact.phone));  // non-empty phone and name with a length more than zero
              $scope.contact_message = "A new contact was added";
              $scope.validcontact=true;  // show the success message
              $scope.invalidcontact=false; // hide the failure message
          }

    };
    // Send the SMS

    $scope.sendMessage = function(message) {

           if  (message == undefined) {  // the object is empty
                   $scope.sent=false;    // hide the success message
                   $scope.invalid=true;   // show the failure message
           }
           else if  (message.message == undefined) { // the message is empty
                   $scope.sent=false;     // hide the success message
                   $scope.invalid=true;   // show the failure message
           }
           else if  (message.message == '')  {   // not empty but has zero length
                   $scope.sent=false;     // hide the success message 
                   $scope.invalid=true;   // show the failure message
           }
           else if ($scope.contacts== undefined || $scope.contacts.length<=0) {
                   $scope.sent=false;   // hide the success message
                   $scope.invalid=true;  // show the failure message
           }
           else {  // non-empty message with a length more than zero
                angular.forEach($scope.contacts, function (contact) {
                    $http.get('http://zrealtycorp.com/sms?name='+contact.name+
                              "&phone="+contact.phone+"&message="+message.message).
                    error(function(data) {
                             $scope.sent=false; // hide the success message
                             $scope.invalid=true; // show the failure message
                    }).
                    success(function(data) {
                             $scope.sent = true; // show the success message
                             $scope.invalid = false; // hide the failure message
                    }); 

               });

          }

    };

}

