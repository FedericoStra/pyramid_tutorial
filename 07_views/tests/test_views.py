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

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Visit', response.body)

    def test_hello(self):
        from tutorial.views import hello

        request = testing.DummyRequest()
        response = hello(request)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello World!', response.body)
        self.assertIn(b'Go back', response.body)


if __name__ == "__main__":
    unittest.main()
