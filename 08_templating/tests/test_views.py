import unittest
from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from tutorial.views import home

        request = testing.DummyRequest()
        response = home(request)

        self.assertEqual("Home view", response['name'])

    def test_hello(self):
        from tutorial.views import hello

        request = testing.DummyRequest()
        response = hello(request)

        self.assertEqual("Hello view", response['name'])


if __name__ == "__main__":
    unittest.main()
