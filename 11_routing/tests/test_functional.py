import unittest
from pyramid import testing


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/howdy/Jane/Doe', status=200)
        self.assertIn(b'Jane', res.body)
        self.assertIn(b'Doe', res.body)


if __name__ == "__main__":
    unittest.main()
