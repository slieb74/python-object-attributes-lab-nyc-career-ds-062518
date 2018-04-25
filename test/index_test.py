import unittest2 as unittest
from ipynb.fs.full.index import *

class TestInstanceMethods(unittest.TestCase):

    def test_instance_types(self):
        self.assertEqual(type(meryl), type(Driver()))
        self.assertEqual(type(daniel), type(Driver()))
        self.assertEqual(type(niky), type(Passenger()))
        self.assertEqual(type(terrance), type(Passenger()))

    def test_variables(self):
        self.assertEqual(polite_greeting, "Hey, how are you?")
        self.assertEqual(no_time_to_talk, "Punch it! They're on our tail!")

    def test_instance_methods(self):
        self.assertEqual(daniel.greeting(), "Hey, how are you?")
        self.assertEqual(niky.in_a_hurry(), "Punch it! They're on our tail!")
