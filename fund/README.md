This solution to the FooBar funding

1. To run the application type python fund.py
2. Creating a new user
- typing

   >create user Jack
   will create a user named Jack

3. Creating a foo bar
   - typing
   >create Foobar raising 100000
   will initiate a new funding campaign (set to zero by default)

4. Wiring money for a user
   - typing
   >user Jack wires 1000 in Foobar
   will reserve a user for amount of 1000

5. Reserving money for a user
   - typing
    >user Jack wires 1000 in Foobar
    will wire the amount of 1000 for the user Jack


6. To exit
   - typing
   >quit
   will terminate the program

If the user does not exist or an attempt to wire or reserve
   is done before the actual user was created, an error will be reported


=================================================================================================================================================
The script uses Python 2.7 and raw_input to get the user input
from the console as the most straightforward and simple solution.

Objects used:
* User  - used to store the user data
* Foobar - used to create a Foobar


=================================================================================================================================================
Functions 
- function handle_input
- input parameters: foobar object, user dictionary (initially empty)
- this function runs as a loop until terminated by typing 'quit' in the console.


