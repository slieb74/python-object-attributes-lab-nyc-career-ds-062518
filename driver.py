# define Driver class and instance methods here

# Note: remember that our instance methods need to be defined with the an
# argument in order to be called on an instance of the class or else we will
# get a `TypeError` telling us that we gave one too many arguments to the
# function. We'll explain why that is soon.

class Driver:

    def greeting(self):
        return "Hey, how are you?"

    def ask_for_destination(self):
        return "Where would you like to go today?"
