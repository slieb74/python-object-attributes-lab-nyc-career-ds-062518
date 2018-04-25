# define Passenger class and instance methods here

# Note: remember that our instance methods need to be defined with the an
# argument in order to be called on an instance of the class or else we will
# get a `TypeError` telling us that we gave one too many arguments to the
# function. We'll explain why that is soon.


class Passenger:

    def reply_greeting(self):
        return "I am doing well! Thanks for picking me up today!"

    def in_a_hurry(self):
        return "Punch it! They're on our tail!"
